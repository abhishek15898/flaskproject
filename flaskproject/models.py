from datetime import datetime
from flaskproject import db, login_manager

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    leader = db.Column(db.String(50), nullable=False)
    leaderEmail = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=True, default='NotPublished')
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=True)
    techUsed = db.Column(db.Text, nullable=True)
    reason = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    member1 = db.Column(db.String(50), nullable=True)
    member2 = db.Column(db.String(50), nullable=True)
    member3 = db.Column(db.String(50), nullable=True)
    member4 = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"Project('{self.title}', '{self.leader}', '{self.status}', '{self.guide_id}', '{self.date_created}')"

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    # unique=True <- Put this in email field
    username = db.Column(db.String(8), nullable=False)
    password = db.Column(db.String(8), nullable=False)
    interest = db.Column(db.Text, nullable=False)
    projects = db.relationship('Project', backref='mentees', lazy=True)

    def __repr__(self):
        return f"Guide('{self.name}', '{self.email}', '{self.interest}')"
