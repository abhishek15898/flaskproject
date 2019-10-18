from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SelectField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, NumberRange

class membersForm(FlaskForm):
    class Meta:
        csrf = False
    memberName = StringField('Team Member',
                        validators=[Length(min=0, max=20)])
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
                        validators=[DataRequired(), Length(min=150)])
    teamName = StringField('Team Name',
                        validators=[DataRequired(), Length(min=2, max=50)])
    members = FieldList(FormField(membersForm), min_entries=4)
    technologyUsed = StringField('Technology Used',
                        validators=[Length(min=0, max=100)])
    internalGuides = SelectField(u'Select your Internal Guide', coerce=int)
    externalGuides = SelectField(u'Select your Enternal Guide', coerce=int)
    submitProject = SubmitField('Register Project')

class guideRegister(FlaskForm):
    guideName = StringField('Your Name: ',
                        validators=[DataRequired(), Length(min=2, max=50)])
    guideEmail = StringField('Your Email: ',
                        validators=[DataRequired(), Email()])
    username = StringField('Username ',
                        validators = [DataRequired(), Length(min=8)])
    password= PasswordField('Password: ',
                        validators = [DataRequired(), Length(min=8)])
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

class DemoForm(FlaskForm):
    csrf = True
    parameter= IntegerField('Marks: ',
                        validators=[DataRequired(), NumberRange(min=0, max=10, message="Please enter marks between 0 to 10 only.")])
    progress= IntegerField('Progress: ',
                        validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter progress of project between 0 to 100 only.")])
    remarks = TextAreaField('Remarks: (if any)',
                        validators=[Optional()])
    submit = SubmitField('Add Demo')
# department = SelectField(u'Select Your Department',
#                     choices=[('ce', 'Civil Engineering'), ('cse', 'Computer Science & Engineering'), ('it', 'Information Technology'),('entc', 'Electonics and Telecommunication Engineering'), ('me', 'Mechanical Engineering')],
#                     validators=[DataRequired()])

class passwordReset(FlaskForm):
    username = StringField('Username ',
                        validators = [DataRequired(), Length(min=2)])
    password= PasswordField('Password: ',
                        validators = [DataRequired(), Length(min=2)])
    confirmPassword = PasswordField('Confirm Password: ',
                        validators = [DataRequired(), Length(min=2), EqualTo('password', message='Passwords must match')])
    registerGuide = SubmitField('Register Guide')

class subscription_form(FlaskForm):
    name = StringField('Your Name', validators = [DataRequired(), Length(min=2)])
    email = StringField('Your Email: ',
                        validators=[DataRequired(), Email()])
    subscribe = SubmitField('Subscribe')

class abstractForm(FlaskForm):
    code = StringField('Enter Code', validators = [DataRequired()])
    submit = SubmitField('Add Abstract')


class notificationForm(FlaskForm):
    email_from = SelectField(u'Email From', validators = [DataRequired()], choices=[('','Select your Designation'),(1, 'Project Incharge - 1'), (2, 'Project Incharge - 2'), (3, 'Project Management Team'), (4, 'Developers')])
    email_to = SelectField(u'Email To', validators = [DataRequired()], choices=[('','Your Designation'),(1, 'To all the Guides'),(2, 'To all the Students'), (3, 'To all the BE-CSE-A Students'), (4, 'To all the BE-CSE-B Students')])
    submit = SubmitField('Add Abstract')
