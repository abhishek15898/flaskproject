from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class projectRegister(FlaskForm):
    projectTitle = StringField('Project Title',
                        validators=[DataRequired(), Length(min=2, max=50)])
    projectDescription = TextAreaField('Project Description',
                        validators=[DataRequired()])
    teamLeaderName = StringField('Team Leader Name',
                        validators=[DataRequired(), Length(min=2, max=50)])
    teamLeaderEmail = StringField('Team Leader Email',
                        validators=[DataRequired(), Email()])
    teamMember1Name = StringField('Team Member - 1',
                        validators=[Length(min=0, max=50)])
    teamMember2Name = StringField('Team Member - 2',
                        validators=[ Length(min=0, max=50)])
    teamMember3Name = StringField('Team Member - 3',
                        validators=[ Length(min=0, max=50)])
    teamMember4Name = StringField('Team Member - 4',
                        validators=[ Length(min=0, max=50)])
    technologyUsed = StringField('Technology Used',
                        validators=[ Length(min=0, max=100)])
    reason = TextAreaField('Why this Project?',
                        validators=[DataRequired()])
    submitProject = SubmitField('Register Project')


class guideRegister(FlaskForm):
    guideName = StringField('Your Name: ',
                        validators=[DataRequired(), Length(min=2, max=50)])
    guideEmail = StringField('Your Email: ',
                        validators=[DataRequired(), Email()])
    guideInterest = TextAreaField('Your Area of Interest: ',
                        validators=[DataRequired(), Length(min=2, max=50)])
    registerGuide = SubmitField('Register Guide')

class trackProject(FlaskForm):
    project_id = StringField('Track Your Project: ',
                        validators = [DataRequired(), Length(min=1)])
    track = SubmitField('Track')


# department = SelectField(u'Select Your Department',
#                     choices=[('ce', 'Civil Engineering'), ('cse', 'Computer Science & Engineering'), ('it', 'Information Technology'),('entc', 'Electonics and Telecommunication Engineering'), ('me', 'Mechanical Engineering')],
#                     validators=[DataRequired()])
