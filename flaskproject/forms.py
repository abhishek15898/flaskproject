from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SelectField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class membersForm(FlaskForm):
    class Meta:
        csrf = False
    memberName = StringField('Team Member',
                        validators=[Length(min=0, max=50)])
    memberEmail = StringField('Email: ',
                        validators=[Email(), Optional()])
    memberClass = SelectField(u'Class', choices=[('','Select Class'),('A', 'BE-CSE-A'), ('B', 'BE-CSE-B')])
    memberPhone = StringField('Phone: ',
                        validators=[Length(min=10, max=10), Optional()])

class projectRegister(FlaskForm):
    class Meta:
        csrf = True
    projectTitle = StringField('Project Title',
                        validators=[DataRequired(), Length(min=2, max=50)])
    projectDescription = TextAreaField('Project Description',
                        validators=[DataRequired()])
    teamName = StringField('Team Name',
                        validators=[DataRequired(), Length(min=2, max=50)])
    members = FieldList(FormField(membersForm), min_entries=4)
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
    username = StringField('Username ',
                        validators = [DataRequired(), Length(min=2)])
    password= PasswordField('Password: ',
                        validators = [DataRequired(), Length(min=2)])
    guideInterest = TextAreaField('Your Area of Interest: ',
                        validators=[DataRequired(), Length(min=2, max=50)])
    registerGuide = SubmitField('Register Guide')

class trackProject(FlaskForm):
    project_id = StringField('Track Your Project: ',
                        validators = [DataRequired(), Length(min=7)])
    track = SubmitField('Track')

class GuideLoginForm(FlaskForm):
    username = StringField('Username ',
                        validators = [DataRequired(), Length(min=2)])
    password= PasswordField('Password: ',
                        validators = [DataRequired(), Length(min=2)])
    submit = SubmitField('Submit')


# department = SelectField(u'Select Your Department',
#                     choices=[('ce', 'Civil Engineering'), ('cse', 'Computer Science & Engineering'), ('it', 'Information Technology'),('entc', 'Electonics and Telecommunication Engineering'), ('me', 'Mechanical Engineering')],
#                     validators=[DataRequired()])
