from datetime import datetime
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
    status = db.Column(db.String(20), nullable=True, default='NotPublished')
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    techUsed = db.Column(db.Text, nullable=True)
    reason = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Project('{self.title}', '{self.leader}', '{self.status}', '{self.guide_id}', '{self.date_created}')"

class Guide(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    # unique=True <- Put this in email field
    username = db.Column(db.String(8), nullable=False)
    password = db.Column(db.String(8), nullable=False)
    interest = db.Column(db.Text, nullable=False)
    projects = db.relationship('Project', backref='mentor', lazy=True)
    def __repr__(self):
        return f"Guide('{self.name}', '{self.email}', '{self.interest}')"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    cls = db.Column(db.String(7), nullable=False)
    def __repr__(self):
        return f"Student('{self.name}', '{self.email}', '{self.phone}', '{self.cls}')"

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    members = db.relationship('Student', backref='team', lazy=True)
    project_team = db.relationship('Project', backref='team', lazy=True)
    def __repr__(self):
        return f"Team('{self.name}')"
