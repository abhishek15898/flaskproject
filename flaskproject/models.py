from datetime import datetime, timedelta
from flaskproject import db, login_manager
from flask_login import UserMixin

# we write this decorator to let this extension know that
# this is the function to get a guide by an id.
@login_manager.user_loader
def load_guide(guide_id):
    return Guide.query.get(int(guide_id))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    code = db.Column(db.String(50), nullable=True)
    desc = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=True, default=0)
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=True)
    external_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    techUsed = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now()+timedelta(hours=5, minutes=30))
    ext_relation = db.relationship('Guide', foreign_keys=[external_id], backref='external')
    int_relation = db.relationship('Guide', foreign_keys=[guide_id], backref='mentor')
    # projectDemo = db.relationship('ProjectGuideDemo', backref="projectDemoDetails", lazy=True)
    def __repr__(self):
        return f"Project('{self.title}', '{self.status}', '{self.guide_id}', '{self.date_created}' )"

class Guide(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(8), nullable=False, unique=True)
    password = db.Column(db.String(8), nullable=False)
    # guideDemo = db.relationship('ProjectGuideDemo', backref="guideDemoDetails", lazy=True)
    def __repr__(self):
        return f"Guide('{self.name}', '{self.email}', '{self.username}')"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    cls = db.Column(db.String(7), nullable=False)
    def __repr__(self):
        return f"Student('{self.name}', '{self.email}', '{self.phone}', '{self.cls}')"

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    members = db.relationship('Student', backref='team', lazy=True)
    project_team = db.relationship('Project', backref='team', lazy=True)
    def __repr__(self):
        return f"Team('{self.name}','{self.members}')"

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    demo_date = db.Column(db.DateTime, nullable=False, default=datetime.now()+timedelta(hours=5, minutes=30))
    remark = db.Column(db.Text, nullable=True)
    marks_id = db.Column(db.Integer, db.ForeignKey('marks.id'), nullable=True)
    progress = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"""Demo('{self.demo_date}', '{self.remark}', '{self.progress}', '{self.marks_id}')"""
    # demo = db.relationship('ProjectGuideDemo', backref="eachDemoDetails", lazy=True)

class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter = db.Column(db.Integer, nullable=False)
    demoMarks = db.relationship('Demo', backref="marks", lazy=True)
    def __repr__(self):
        return f"Marks('{self.parameter}', '{self.demoMarks}')"

class ProjectGuideDemo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=True)
    demo_id = db.Column(db.Integer, db.ForeignKey('demo.id'), nullable=True)
    project = db.relationship('Project', backref="demoDetails", lazy=True )
    guide = db.relationship('Guide', backref="demoDetails", lazy=True )
    demo = db.relationship('Demo', backref="demoDetails", lazy=True)

class Grades(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    aPlus = db.Column(db.Integer, nullable=False)
    a = db.Column(db.Integer, nullable=False)
    bPlus = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    cPlus = db.Column(db.Integer, nullable=False)
    c = db.Column(db.Integer, nullable=False)
    dPlus = db.Column(db.Integer, nullable=False)
    d = db.Column(db.Integer, nullable=False)
    f = db.Column(db.Integer, nullable=False)

class Abstract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    abs_desc = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    acceptance_date = db.Column(db.DateTime, nullable=False, default=datetime.now()+timedelta(hours=5, minutes=30))
    project = db.relationship('Project', backref='abstract', lazy=True)

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    completed_stage = db.Column(db.Integer, nullable=False, default=0)
    started_time = db.Column(db.DateTime, default=datetime.now()+timedelta(hours=5, minutes=30))
    completion_time = db.Column(db.DateTime, nullable=False, default=datetime.now()+timedelta(hours=5, minutes=30))
    project = db.relationship('Project', backref='stage', lazy=True)
