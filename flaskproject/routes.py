from flask import render_template, url_for, redirect, flash, Markup, abort, request
from flaskproject import app, db, mail, bcrypt
from flaskproject.models import Project, Guide, Student, Team
from flaskproject.forms import projectRegister, guideRegister, trackProject, GuideLoginForm, membersForm
from sqlalchemy import asc, desc, update
from flask_mail import Mail, Message
from flask_login import login_user, current_user, logout_user, login_required

total_members=4

@app.context_processor
def inject_sidebar_trackForm():
    trackForm = trackProject()
    return dict(trackForm=trackForm)

@app.route("/")
@app.route("/home")
def home():
    projects = Project.query.order_by(desc(Project.id)).all()
    guides=Guide.query.all()
    return render_template('home.html', projects=projects, guides=guides, title='MGM Projects')

@app.route("/about")
def about():
    return render_template('about.html', title='About MGM')

@app.route("/guides")
def guide():
    guides=Guide.query.all()
    return render_template('guides.html', guides=guides, title='Project Guide')

@app.route("/projectRegister", methods=['GET', 'POST'])
def ProjectRegistration():
    global status
    status=0
    form = projectRegister()
    if form.validate_on_submit():
        entries = form.members.data
        membersList = []
        # entries.pop(2)
        flash(form.members.data)
        membersList=validate_on_submit_members(entries)
        status=membersList.pop()
        flash(membersList)
        flash(status)
        if len(membersList)>=1 and status==1:
            flash("check", 'success')
            project = Project(
                        title=form.projectTitle.data,
                        desc=form.projectDescription.data,
                        techUsed=form.technologyUsed.data,
                        reason=form.reason.data
                        )
            db.session.add(project)
            db.session.flush()
            project.code = str("{0:03}".format(project.id))+'-'+project.title[:4].replace(" ", "").upper()+'-'+"omk".upper()
            team = Team(name=form.teamName.data)
            db.session.add(team)
            db.session.flush()
            project.team_id = team.id
            for index, entry in enumerate(membersList):
                    student = Student(
                                team_id=project.team_id,
                                name=entry['memberName'],
                                email=entry['memberEmail'],
                                phone=entry['memberPhone'],
                                cls=entry['memberClass']
                                )
                    db.session.add(student)
            db.session.flush()
            db.session.commit()
            template = f"<b>Hi {project.team.members[0].name}!</b><br /> &nbsp;&nbsp;&nbsp;&nbsp;You have successfully registerd your Project - {project.title}. Please note this ID: <b>{project.code}</b> to track your Project status. You will be soon assigned with a guide!"
            msg = Message(subject='Project Registration Successful | Department of CSE | MGM College of Engineering | Nanded', sender='hello@gmail.com', recipients=[project.team.members[0].email], html=template)
            mail.send(msg)
            flash('You have successfully registered your Project! Please note this ID: ' + project.code + ' to track your Project status.', 'success')
            return redirect(url_for('home'))
    return render_template('ProjectRegistration.html', title='Project Registration', form=form)

@app.route("/guideRegister", methods=['GET', 'POST'])
def GuideRegistration():
    form = guideRegister()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password   .data).decode('utf-8')
        guide = Guide(name=form.guideName.data, username = form.username.data, password = hashed_password, email=form.guideEmail.data, interest=form.guideInterest.data)
        db.session.add(guide)
        db.session.commit()
        flash('Your account has been created. You can now login as a guide.', 'success')
        template = f"Hi {guide.name}! You have been successfully registerd as a Guide. Your Interests: {guide.interest}. You will be informed via mail, when students will be are assigned to you."
        msg = Message(subject='Guide Registration Successful | Department of CSE | MGM College of Engineering | Nanded', sender='hello@gmail.com', recipients=[guide.email], body=template)
        mail.send(msg)
        return redirect(url_for('guide'))
    return render_template('GuideRegistration.html', title='Guide Registration', form=form)

@app.route("/assignGuide", methods=['GET', 'POST'])
def guideAssignment():
    projects = Project.query.filter_by(status='NotPublished')
    guides=Guide.query.all()
    return render_template('assignGuide.html', projects=projects, guides=guides, title='MGM Projects')

@app.route("/trackProject/<data>", methods=['GET', 'POST'])
@app.route("/trackProject", methods=['GET', 'POST'])
def trackProjects(data=None):
    trackForm = trackProject()
    if not data:
        data = trackForm.project_id.data
    project = Project.query.filter_by(code=data).first()
    if project:
        return render_template('progress.html', title="Project Progress", project=project)
    flash('Incorrect Project Code.' + str(data),'danger')
    return redirect(url_for('home'))

@app.route("/guideLogin", methods=['GET', 'POST'])
def guideLogin():
    form = GuideLoginForm()
    if form.validate_on_submit():
        guide = Guide.query.filter_by(username=form.username.data).first()
        if guide and bcrypt.check_password_hash(guide.password, form.password.data):
            login_user(guide)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful...'+form.password.data, 'danger')
    return render_template('guideLogin.html', title='Guide Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/dashboard")
@login_required
def dashboard():
    projects = Project.query.filter_by(guide_id=current_user.id)
    return render_template('dashboard.html', title="Dashboard", projects=projects)

@app.route("/updateProject/<project_id>", methods=['GET', 'POST'])
@login_required
def updateProject(project_id):
    project = Project.query.get_or_404(project_id)
    if project.guide_id!=current_user.id:
        abort(403)
    form = projectRegister()
    students = Student.query.filter_by(team_id=project.team_id)
    if form.validate_on_submit():
        project.title = form.projectTitle.data
        project.desc = form.projectDescription.data
        project.techUsed = form.technologyUsed.data
        project.reason = form.reason.data
        db.session.commit()
        flash('Updated Post', 'success')
        return redirect(url_for('trackProjects', data=project.code))
    elif request.method == 'GET':
        form.projectTitle.data = project.title
        form.projectDescription.data = project.desc
        form.teamName.data = project.team.name
        l=[]
        for i in range(total_members):
                form.members.pop_entry()
        for student in students:
            member = {
            'memberName':student.name,
            'memberEmail':student.email,
            'memberClass':student.cls,
            'memberPhone':student.phone
            }
            l.append(member)
            form.members.append_entry(member)
        length=len(form.members)
        for i in range(0,total_members-length):
            member = {
            'memberName':None,
            'memberEmail':None,
            'memberClass':None,
            'memberPhone':None
            }
            form.members.append_entry(member)
        form.technologyUsed.data= project.techUsed
        form.reason.data= project.reason
    return render_template('ProjectRegistration.html', title='Update Project', form=form)

@app.route("/assignMarks/<data>", methods=['GET', 'POST'])
@login_required
def assignMarks(data):
    project = Project.query.filter_by(code=data).first()
    if project:
        return render_template('assignMarks.html', title="Project Progress", project=project)
    flash('Project Marks for '+ str(data)+' is Not Available. Kindly contact Project Incharge/Developers.','danger')
    return redirect(url_for('dashboard'))

def validate_on_submit_members(entries):
    membersList=[]
    for index, entry in enumerate(entries):
        flag=0
        for key, value in entry.items():
            if bool(value) and flag==0:
                if entry['memberName']!='':
                    membersList.append(entry)
                    flag=1
                    status=1
                    continue
                else:
                    if index==0:
                        flash("Enter valid Leader Name.", 'danger')
                    else:
                        flash("Enter valid Member-"+str(index)+" Name.", 'danger')
                    status=0
                    break
            if flag==1 and bool(value)==False:
                membersList.remove(entry)
                if index==0:
                    flash("Enter valid Leader "+key[6:]+" Details ", 'danger')
                else:
                    flash("Enter valid Member-"+str(index)+" "+ key[6:]+ " Details ", 'danger')
                status=0
                break
            if index==0 and bool(value)==False:
                status=0
                flash("Enter valid Leader "+key[6:], 'danger')
                break
        if status==0:
            break
    membersList.append(status)
    return membersList
