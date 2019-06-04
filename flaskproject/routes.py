from flask import render_template, url_for, redirect, flash, Markup, abort, request
from flaskproject import app, db, mail, bcrypt
from flaskproject.models import Project, Guide
from flaskproject.forms import projectRegister, guideRegister, trackProject, GuideLoginForm
from sqlalchemy import asc, desc, update
from flask_mail import Mail, Message
from flask_login import login_user, current_user, logout_user, login_required

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
    form = projectRegister()
    if form.validate_on_submit():
        project = Project(title=form.projectTitle.data,
                          desc=form.projectDescription.data,
                          leader=form.teamLeaderName.data,
                          techUsed=form.technologyUsed.data,
                          reason=form.reason.data,
                          member1=form.teamMember1Name.data,
                          member2=form.teamMember2Name.data,
                          member3=form.teamMember3Name.data,
                          member4=form.teamMember4Name.data,
                          leaderEmail=form.teamLeaderEmail.data)
        db.session.add(project)
        db.session.flush()
        project.code = str("{0:03}".format(project.id))+'-'+project.title[:4].replace(" ", "").upper()+'-'+project.leader[:3].upper()
        db.session.commit()
        template = f"<b>Hi {project.leader}!</b><br /> &nbsp;&nbsp;&nbsp;&nbsp;You have successfully registerd your Project - {project.title}. Please note this ID: <b>{project.code}</b> to track your Project status. You will be soon assigned with a guide!"
        msg = Message(subject='Project Registration Successful | Department of CSE | MGM College of Engineering | Nanded', sender='hello@gmail.com', recipients=[form.teamLeaderEmail.data], html=template)
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
    if form.validate_on_submit():
        project.title = form.projectTitle.data
        project.desc = form.projectDescription.data
        project.leader = form.teamLeaderName.data
        project.leaderEmail = form.teamLeaderEmail.data
        project.member1 = form.teamMember1Name.data
        project.member2 = form.teamMember2Name.data
        project.member3 = form.teamMember3Name.data
        project.member4 = form.teamMember4Name.data
        project.techUsed = form.technologyUsed.data
        project.reason = form.reason.data
        db.session.commit()
        flash('Updated Post', 'success')
        return redirect(url_for('trackProjects', data=project.code))
    elif request.method == 'GET':
        form.projectTitle.data = project.title
        form.projectDescription.data = project.desc
        form.teamLeaderName.data= project.leader
        form.teamLeaderEmail.data= project.leaderEmail
        form.teamMember1Name.data= project.member1
        form.teamMember2Name.data= project.member2
        form.teamMember3Name.data= project.member3
        form.teamMember4Name.data= project.member4
        form.technologyUsed.data= project.techUsed
        form.reason.data= project.reason
    return render_template('ProjectRegistration.html', title='Update Project', form=form)
