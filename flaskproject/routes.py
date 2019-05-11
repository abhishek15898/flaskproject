from flask import render_template, url_for, redirect, flash, Markup
from flaskproject import app, db, mail
from flaskproject.models import Project, Guide
from flaskproject.forms import projectRegister, guideRegister, trackProject
from sqlalchemy import asc, desc, select
from flask_mail import Mail, Message

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
                          techUsed=form.teamLeaderName.data,
                          reason=form.reason.data,
                          member1=form.teamMember1Name.data,
                          member2=form.teamMember2Name.data,
                          member3=form.teamMember3Name.data,
                          member4=form.teamMember4Name.data)
        db.session.add(project)
        db.session.commit()
        unique_id = Markup('<b>'+str("{0:03}".format(project.id))+'-'+project.title[:4].replace(" ", "").upper()+'-'+project.leader[:3].upper()+'</b>')
        template = f"<b>Hi {project.leader}!</b><br /> &nbsp;&nbsp;&nbsp;&nbsp;You have successfully registerd your Project - {project.title}. Please note this ID: {unique_id} to track your Project status. You will be soon assigned with a guide!"
        msg = Message(subject='Project Registration Successful | Department of CSE | MGM College of Engineering | Nanded', sender='hello@gmail.com', recipients=[form.teamLeaderEmail.data], html=template)
        # Can also access this way:
        # msg.subject=""
        # msg.body=""
        # msg.html=""
        # msg.add_recipient('fvs@gmail.com')
        mail.send(msg)
        # bulk emails also possible
        flash('You have successfully registered your Project! Please note this ID: ' + unique_id + ' to track your Project status.', 'success')
        return redirect(url_for('home'))
    return render_template('ProjectRegistration.html', title='Project Registration', form=form)


@app.route("/guideRegister", methods=['GET', 'POST'])
def GuideRegistration():
    form = guideRegister()
    if form.validate_on_submit():
        guide = Guide(name=form.guideName.data, email=form.guideEmail.data, interest=form.guideInterest.data)
        db.session.add(guide)
        db.session.commit()
        flash('You have registered successfully! Please check your email', 'success')
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

@app.route("/trackProject", methods=['GET', 'POST'])
def trackProjects():
    trackForm = trackProject()
    id=(trackForm.project_id.data).split("-")
    p=int(id[0])
    project = db.session.query(Project).get(p)
    return render_template('progress.html', title="Project Progress", project=project, id=id, p=p)
