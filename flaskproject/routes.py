from flask import render_template, url_for, redirect, flash, Markup, abort, request, jsonify
from flaskproject import app, db, mail, bcrypt, admin
from flaskproject.models import Project, Guide, Student, Team, ProjectGuideDemo, Marks, Demo, Grades
from flaskproject.forms import doubtForm, notificationForm, projectRegister, guideRegister, trackProject, GuideLoginForm, membersForm, DemoForm, passwordReset, subscription_form, abstractForm
from sqlalchemy import asc, desc, update
from flask_mail import Mail, Message
from flask_login import login_user, current_user, logout_user, login_required
from flaskproject.global_variables import *
from flaskproject.email_templates import *
from flask_admin.contrib.sqla import ModelView
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Guide, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(ProjectGuideDemo, db.session))
admin.add_view(ModelView(Marks, db.session))
admin.add_view(ModelView(Demo, db.session))
admin.add_view(ModelView(Grades, db.session))
@app.context_processor
def inject_sidebar_trackForm():
    trackForm = trackProject()
    return dict(trackForm=trackForm)

@app.route("/")
@app.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    projects = Project.query.filter_by(status=1).order_by(desc(Project.id)).paginate(page=page, per_page=6)
    total_projects = Project.query.order_by(desc(Project.id)).all()
    guides=Guide.query.all()
    return render_template('home.html', projects=projects, guides=guides, title='MGM Projects',total_projects=total_projects, stages=stages)
@app.route("/about")
def about():
    form = subscription_form()
    return render_template('underConstruction.html', title='About Us', form=form)

@app.route("/guidelines", methods=['GET', 'POST'])
def guidelines():
    form=doubtForm()
    # if request.method=="POST":
    #     print(request.form.get('name'))
    if form.validate_on_submit():
        print("We are here")
        name = form.name.data
        email = form.Email.data
        query = form.Query.data
        template = f"Name: {name} <br/> Email: {email} <br/> Query: {query}"
        msg = Message(subject='Form submission - MGM Projects', sender='mgms.projects@gmail.com', recipients=['edu.omkar@gmail.com'], html=template)
        mail.send(msg)
        flash('Your Query has been received. We will soon get in touch with you!', 'success')
        return redirect(url_for('guidelines'))
    return render_template('guidelines.html', title='Guidelines', form=form)

@app.route("/timeline")
def timeline():
    form = subscription_form()
    return render_template('underConstruction.html', title='About Us', form=form)

@app.route("/faqs")
def faqs():
    form = subscription_form()
    return render_template('underConstruction.html', title='About Us', form=form)



@app.route("/guide")
def guide():
    page=request.args.get('page',1,type=int)
    guides=Guide.query.paginate(page=page, per_page=10)
    return render_template('guides.html', guides=guides, title='Project Guide')

@app.route("/contactus")
def contactus():
    form = subscription_form()
    return render_template('underConstruction.html', title='About Us', form=form)

@app.route("/projectRegister", methods=['GET', 'POST'])
def ProjectRegistration():
    global status
    status=0
    guides=Guide.query.all()
    guide_list=[(i.id, i.name) for i in guides]
    form = projectRegister()
    form.internalGuides.choices = form.externalGuides.choices =  guide_list
    if form.validate_on_submit():
        entries = form.members.data
        # print(form.internalGuides.data)
        membersList = []
        membersList=validate_on_submit_members(entries)
        status=membersList.pop()
        if len(membersList)>=1 and status==1:
            project = Project(
                        title=form.projectTitle.data,
                        desc=form.projectDescription.data,
                        techUsed=form.technologyUsed.data,
                        guide_id = form.internalGuides.data,
                        external_id = form.externalGuides.data,
                        )
            db.session.add(project)
            db.session.flush()
            team = Team(name=form.teamName.data)
            db.session.add(team)
            db.session.flush()
            project.team_id = team.id
            student_emails=[]
            for index, entry in enumerate(membersList):
                    student = Student(
                                team_id=project.team_id,
                                name=entry['memberName'].title(),
                                email=entry['memberEmail'],
                                phone=entry['memberPhone'],
                                cls=entry['memberClass']
                                )
                    student_emails.append(entry['memberEmail'])
                    db.session.add(student)
            project.code = str("{0:03}".format(project.id))+'-'+project.title[:4].replace(" ", "").upper()+'-'+project.team.members[0].name[:3].upper()
            db.session.flush()
            db.session.commit()
            template_student_body=f"""
             Hey <b>{project.team.members[0].name}!</b><br/><br/>
             We are super-excited to have you, your team and your amazing project - <b>{project.title}</b> on board in our <b>Project Management System.</b><br/><br/>
             Your project will be verified by Project Incharges. Once verified, it will be accepted for further stages. <br/><br/>
             We will email you once your project has been accepted. Meanwhile stay rest assured and explore new projects on our portal!<br/><br/>
             &emsp;<b>Project-Code:</b> {project.code}<br/>
             &emsp;<b>Internal Guide:</b> {project.int_relation.name} ({project.int_relation.email})<br/>
             &emsp;<b>External Guide:</b> {project.ext_relation.name} ({project.ext_relation.email})<br/>
             (<small>If you find the above guide details incorrect, please immediately report us at mgms.projects@gmail.com</small>)<br/><br/>
             All the very best!<br/><br/>
             <div style=\"background: rgb(255,255,204); padding:5px;\">
             <small><b>Need Help for your project?</b> You may find projects similar to your project on our <a href="http://mgmprojects.pythonanywhere.com">website</a>. They may have come with the same issue as you are facing now, and together you can figure out a solution! We encourage you to also help other teams in need! Afterall, sharing our knowledge is a great way to grow!</small>
             </div><br/>
            """
            template = email_header+template_student_body+email_footer
            msg = Message(subject='Project Registration Successful | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=student_emails, html=template)
            mail.send(msg)
            flash('You have successfully registered your Project! Please note this ID: ' + project.code + ' to track your Project status. Also check your Registered Email Id for more details.', 'success')
            return redirect(url_for('home'))
    return render_template('ProjectRegistration.html', title='Project Registration', form=form)

@app.route("/guideRegister", methods=['GET', 'POST'])
def GuideRegistration():
    form = guideRegister()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        guide = Guide(name=form.guideName.data, username = form.username.data, password = form.password.data, email=form.guideEmail.data)
        db.session.add(guide)
        db.session.commit()
        flash(Markup('Your account has been created. You can now login as a guide <a href="/guideLogin" class="alert-link" style="color:blue"> here</a>.'), 'success')
        template = email_header+f"""
        Respected <b>{guide.name},<br/><br/></b> You are successfully registered as a Guide on our <b>Project Management System</b> Portal. <br/><br/>
        We will inform you (via e-mail) when students are assigned to you.<br/><br/>
        The following are your credentials:<br/>
        <b>Username</b>:{guide.username}<br/>
        <b>Password</b>:{guide.password}<br/><br/>
        Please <a href=mgmprojects.pythonanywhere.com/password_reset>Click Here</a> to Reset your Password using the temporary Username and Password provided above.<br/>
        <small>(If the above link doesn't work, please copy this link - mgmprojects.pythonanywhere.com/password_reset and paste it in the address field of your browser.)</small><br/><br/>
        Please <a href=mgmprojects.pythonanywhere.com/guideLogin>Click Here</a> to Login to the website.<br/>
        <small>(If the above link doesn't work, please copy this link - mgmprojects.pythonanywhere.com/guideLogin and paste it in the address field of your browser.)</small><br/>
        """+email_footer
        msg = Message(subject='Guide Registration Successful | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=[guide.email], html=template)
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
    if not project:
        flash('Incorrect Project Code:' + str(data),'danger')
        return redirect(url_for('home'))
    internal_guide_demos = ProjectGuideDemo.query.filter_by(guide_id=project.int_relation.id, project_id=project.id)
    external_guide_demos = ProjectGuideDemo.query.filter_by(guide_id=project.ext_relation.id, project_id=project.id)
    return render_template('progress.html', title="Project Progress", project=project, i_demos=internal_guide_demos, e_demos=external_guide_demos )


@app.route("/guideLogin", methods=['GET', 'POST'])
def guideLogin():
    form = GuideLoginForm()
    if form.validate_on_submit():
        guide = Guide.query.filter_by(username=form.username.data).first()
        if guide and bcrypt.check_password_hash(guide.password, form.password.data):
            login_user(guide)
            return redirect(url_for('home'))
        else:
            # flash(Markup('Login Unsuccessful. Please Contact the Admin or try resetting the password <a href="/password_reset" class="alert-link">here</a>', 'danger'))
            flash(Markup('Incorrect Username or Password. <br>(1) Please Contact the Admin.<br>(2)<a href="/password_reset" class="alert-link" style="color:blue"> Click here</a> to reset your password.'), 'danger')
    return render_template('guideLogin.html', title='Guide Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/dashboard")
@login_required
def dashboard():
    project_internal = Project.query.filter_by(guide_id=current_user.id)
    project_external = Project.query.filter_by(external_id=current_user.id)
    return render_template('dashboard.html', title="Dashboard", projects=project_internal, proj_external=project_external)

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
    project = Project.query.filter_by(id=data).first()
    form = DemoForm()
    if form.validate_on_submit():
        # project.demo.marks.parameter1=form.data.para1
        # flash(form.data['para1'])
        marks = Marks(
            parameter=form.parameter.data
            # total=form.data['para1']+form.data['para2']+form.data['para3']+form.data['para4']+form.data['para5']
        )
        db.session.add(marks)
        db.session.flush()
        current_demo = Demo(
            remark = form.data['remarks'],#as per form validation remark is optional, but we have set nullable=false in db
            marks_id = marks.id,
            progress = form.data['progress']
        )
        db.session.add(current_demo)
        db.session.flush()
        demo_guide_project_table = ProjectGuideDemo(
            project_id = project.id,
            guide_id = current_user.id,
            demo_id = current_demo.id
        )
        db.session.add(demo_guide_project_table)
        db.session.commit()
        flash('Marks have been successfully assigned to '+ str(project.title) , 'success')
        return redirect(url_for('dashboard'))
    return render_template('assignMarks.html', title="Assign Marks", project=project, form=form)

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
@app.route("/password_reset", methods=['GET', 'POST'])
def password_reset():
    form = passwordReset()
    if form.validate_on_submit():
        username = form.data['username']
        print(username)
        guide = Guide.query.filter_by(username=username)
        if guide:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            guide[0].password = hashed_password
            db.session.commit()
            template = email_header+f"""
            Respected <b>{guide[0].name}</b>,
            <br/><br/>You have successfully reset your password.<br/><br/>
            <b>Not you? </b>If it was not you, please <b>immediately report us</b> by replying the issue on this email.<br/><br/>
            """+email_footer
            msg = Message(subject='[ALERT!] Password Reset Done | Department of CSE | MGM\'s College of Engineering', sender='mgms.projects@gmail.com', recipients=[guide[0].email], html=template)
            mail.send(msg)
            flash('Password Reset Successful!','success')
        else:
            flash('The entered username doesnot exist. Please register as a Guide.','danger')
        return redirect(url_for('guideLogin'))
    return render_template('password-reset.html', title="Reset Password", form=form)

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500
@app.route("/confirm", methods=['GET', 'POST'])
def confirmProjects():
    projects = Project.query.filter_by(status=0)
    count = Project.query.filter_by(status=0).count()
    return render_template('temporary.html', title="ConfirmProjects", projects=projects, count=count)
@app.route('/confirmedProject/<id>')
def confirmedProject(id):
    project = Project.query.filter_by(code=id).first()
    project.status=1
    db.session.commit()
    student_emails=[]
    student_email_ids=Student.query.filter_by(team_id=project.team_id).with_entities(Student.email).all()
    for email in student_email_ids:
        student_emails.append(email[0])
    template_guide_body=f"""
    We have received a project that has been assigned under your guidance:<br/>
    &emsp;<b>Project Name</b>:{project.title}<br/>
    &emsp;<b>Project Leader</b>: {project.team.members[0].name}<br/>
    &emsp;<b>Technologies used</b>: {project.techUsed}<br/>
    &emsp;<b>Project Internal Guide</b>: {project.int_relation.name}<br/>
    &emsp;<b>Project External Guide</b>: {project.ext_relation.name}<br/>
    <br/>
    We will keep informing you as we get other projects from students.<br/><br/>
    To view more details of your projects and to conduct demos or assign marks to these projects, please login to our portal at mgmprojects.pythonanywhere.com/guideLogin<br/><br/>
    """

    template_int_body = email_header+f"""
    Respected <b>{project.int_relation.name}</b>,<br/><br/>
    """+template_guide_body+email_footer
    msg = Message(subject='[Project Assigned] Internal Guide | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=[project.int_relation.email], html=template_int_body)
    mail.send(msg)

    template_ext_body = email_header+f"""
    Respected <b>{project.ext_relation.name}</b>,<br/><br/>
    """+template_guide_body+email_footer
    msg = Message(subject='[Project Assigned] External Guide | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=[project.ext_relation.email], html=template_ext_body)
    mail.send(msg)

    template_student_body=f"""
     Hey <b>{project.team.members[0].name}!</b><br/><br/>
     We are glad to inform you that your project - <b>{project.title}</b> has been accepted by Admin/Project-Incharge.</b><br/><br/>
     Note the following details for future references:<br/>
     &emsp;<b>Project-Code:</b> {project.code}<br/>
     &emsp;<b>Internal Guide:</b> {project.int_relation.name} ({project.int_relation.email})<br/>
     &emsp;<b>External Guide:</b> {project.ext_relation.name} ({project.ext_relation.email})<br/>
     (<small>If you find the above guide details incorrect, please immediately report us at mgms.projects@gmail.com</small>)<br/><br/>
         That's it for now! We are delighted to see your project taking every step of its success with the dedicated efforts of your team and guides!<br/><br/>
     All the very best!<br/><br/>
     <div style=\"background: rgb(255,255,204); padding:5px;\">
     <small><b>Need Help for your project?</b> You may find projects similar to your project on our <a href="http://mgmprojects.pythonanywhere.com">website</a>. They may have come with the same issue as you are facing now, and together you can figure out a solution! We encourage you to also help other teams in need! Afterall, sharing our knowledge is a great way to grow!</small>
     </div><br/>
    """
    template = email_header+template_student_body+email_footer
    msg = Message(subject='[Project-Accepted] Congratulations! | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=student_emails, html=template)
    mail.send(msg)

    projects = Project.query.filter_by(status=0)
    count = Project.query.filter_by(status=0).count()
    flash('Project Confirmed Successfully!', 'success')
    return render_template('temporary.html', title="ConfirmProjects", projects=projects, count=count)

@app.route('/deleteProject/<id>')
def deleteProject(id):
    project = Project.query.filter_by(code=id).first()
    student_emails=[]
    student_email_ids=Student.query.filter_by(team_id=project.team_id).with_entities(Student.email).all()
    for email in student_email_ids:
        student_emails.append(email[0])
    template_student_body=f"""
     Hi <b>{project.team.members[0].name}!</b><br/><br/>
     You project - <b>{project.title}</b> has been rejected by Admin/Project-Incharge.</b><br/><br/>
     Please contact the Project Incharge or consider submitting another Project Application.<br/><br/>
     All the very best!<br/><br/>
     <div style=\"background: rgb(255,255,204); padding:5px;\">
     <small><b>Need Help for your project?</b> You may find projects similar to your project on our <a href="http://mgmprojects.pythonanywhere.com">website</a>. They may have come with the same issue as you are facing now, and together you can figure out a solution! We encourage you to also help other teams in need! Afterall, sharing our knowledge is a great way to grow!</small>
     </div><br/>
    """
    template = email_header+template_student_body+email_footer
    msg = Message(subject='[Project-Rejected] | Department of CSE | MGM\'s College of Engineering | Nanded', sender='mgms.projects@gmail.com', recipients=student_emails, html=template)
    mail.send(msg)

    team_id=project.team.id
    Student.query.filter_by(team_id=team_id).delete()
    # db.session.delete(students) doesnot take effect
    db.session.delete(project)
    team=Team.query.filter_by(id=team_id).delete()
    db.session.delete(project)
    db.session.commit()

    projects = Project.query.filter_by(status=0)
    count = Project.query.filter_by(status=0).count()
    flash('Project Deleted Successfully', 'danger')
    return render_template('temporary.html', title="ConfirmProjects", projects=projects, count=count)


@app.route('/fetchProject', methods = ['POST'])
def fetchProject():
    form = abstractForm()
    if form.validate_on_submit():
        project = Project.query.filter_by(code=form.code.data).first()
        if project:
            flag = 1
            flash('Successfully fetched your project details.', 'success')
        else:
            flag = 0
            flash('Please enter a valid code.', 'danger')
        return render_template('addAbstract.html', title="Add Abstract", form=form, project=project, flag=flag)

@app.route('/getAbstract', methods = ['GET','POST'])
def getAbstract():
    if request.method == 'POST':
        abstractData = request.form.get('editordata')
        # preview = request.args.get('preview')
        print(abstractData)
        # if preview is None:
        # return render_template('previewAbstract.html', title="Preview", data=abstractData)
        # else:
        flash('Your abstract has been successfully submitted!', 'success')
    elif request.method == 'GET':
        abstractData = request.args.get('editordata')
        preview = request.args.get('preview')
        print(abstractData, preview)
        if preview==1:
            return render_template('previewAbstract.html', title="Preview", data=abstractData)
    else:
        flash(abstractData)
        flash('Oops! There seems to be some error here. Try submitting the abstract again.', 'danger')
    return redirect(url_for('addAbstract'))

@app.route('/addAbstract', methods=['GET','POST'])
def addAbstract():
    form = abstractForm()
    flag = request.args.get('flag')
    project = None
    # print(str(request.args[0][0][1]))
    return render_template('addAbstract.html', title="Add Abstract", form=form, project=project, flag=flag)

@app.route('/addNotifications', methods=['GET','POST'])
def addNotifications():
    if request.method=="POST":
        email_from = request.form.get('email_from')
        email_to = request.form.get('email_to')
        body = request.form.get('editordata')
        print(email_from, email_to, body)
        flash('Messange Sent', 'success')
    return render_template('addNotifications.html', title="Add Notifications")

@app.route('/sendAllStudentsEmail', methods=['GET','POST'])
def sendAllStudentsEmail():
    pass
