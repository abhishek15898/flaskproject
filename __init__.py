from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'edu.omkar@gmail.com',
    # s16_deshpande_omkar@mgmcen.ac.in
    "MAIL_PASSWORD": 'omnewton1'
}

app.config.update(mail_settings)
mail = Mail(app)

app.config['SECRET_KEY'] = '75083a4f96853215ceb516a0d62506a7'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'guideLogin'
login_manager.login_message_category = 'info'
from flaskproject import routes
