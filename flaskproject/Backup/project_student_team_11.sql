BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "student" (
	"id"	INTEGER NOT NULL,
	"team_id"	INTEGER,
	"name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(120) NOT NULL,
	"phone"	VARCHAR(10) NOT NULL,
	"cls"	VARCHAR(7) NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("team_id") REFERENCES "team"("id")
);
CREATE TABLE IF NOT EXISTS "project" (
	"id"	INTEGER NOT NULL,
	"title"	VARCHAR(50) NOT NULL UNIQUE,
	"code"	VARCHAR(50),
	"desc"	TEXT NOT NULL,
	"status"	INTEGER,
	"guide_id"	INTEGER,
	"external_id"	INTEGER,
	"team_id"	INTEGER,
	"techUsed"	TEXT,
	"date_created"	DATETIME NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("guide_id") REFERENCES "guide"("id"),
	FOREIGN KEY("external_id") REFERENCES "guide"("id"),
	FOREIGN KEY("team_id") REFERENCES "team"("id")
);
CREATE TABLE IF NOT EXISTS "team" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "student" VALUES (1,1,'Omkar Deshpande','edu.omkar@gmail.com','7798576939','A');
INSERT INTO "student" VALUES (2,1,'Abhishek Bagate','abhishekbagate15898@gmail.com','9511681791','A');
INSERT INTO "student" VALUES (3,2,'Furkhan Shaikh','29furkhanshaikh@gmail.com','9763118461','B');
INSERT INTO "student" VALUES (4,2,'Prashant Phulari','prashantphulari21@gmail.com','7038497133','B');
INSERT INTO "student" VALUES (5,3,'Ashok Mange','ashokmange00@gmail.com','9284715329','B');
INSERT INTO "student" VALUES (6,3,'Ravikumar Lakshatwar','ravilakshatwar77@gmail.com','7350632078','B');
INSERT INTO "student" VALUES (7,4,'Suchitra Choudhante ','suchitrachoudhante@gmail.com','9168396358','A');
INSERT INTO "student" VALUES (8,4,'Vaibhavi Pariyal','vaibhavipariyal01@gmail.com','8412899976','A');
INSERT INTO "student" VALUES (9,5,'Ravi Dhamne','ravid1904@gmail.com','9158724772','A');
INSERT INTO "student" VALUES (10,5,'Sachin Belkhede','sachin20695@gmail.com','9767085445','A');
INSERT INTO "student" VALUES (11,6,'Minal Kaminwar','monukamin3997@gmail.com','8600356644','A');
INSERT INTO "student" VALUES (12,6,'Julur Shweta','julurshweta13@gmail.com','7875036494','A');
INSERT INTO "student" VALUES (13,7,'Bilman Shira','s16_shira_bilman@mgmcen.ac.in','6009457900','A');
INSERT INTO "student" VALUES (14,7,'Shubham Rai','s16_rai_shubham@mgmcen.ac.in','9673904405','A');
INSERT INTO "student" VALUES (15,8,'Syeda Saniya','Syedasaniya44@gmail.com','8669321159','A');
INSERT INTO "student" VALUES (16,8,'Nikita Bandewar','nikitabandewar123@gmail.com','8698103377','A');
INSERT INTO "student" VALUES (17,9,'Pooja Shivankar','shivankarpooja42@gmail.com','9960941272','A');
INSERT INTO "student" VALUES (19,9,'Snehal Matalkar','snehalmatalkar27@gmail.com','9511894166','A');
INSERT INTO "student" VALUES (20,10,'Snehal Mahajan','snehalmahajan21@gmail.com','8888505961','A');
INSERT INTO "student" VALUES (21,10,'Sameeksha Medewar','samumedewar@gmail.com','8381084719','A');
INSERT INTO "student" VALUES (23,11,'Pradeep Gaware','gawarepradeep1999@gmail.com','9284673396','A');
INSERT INTO "student" VALUES (25,11,'Mohammed Sajjad','mohammedsajjad0901@gmail.com','9028179905','A');
INSERT INTO "project" VALUES (1,'Project Management System','001-PROJ-OMK','Our project aims at solving the manual procedure of project submission using the software. This software manages student projects, abstracts, demos and final reports. The objective of this project is to inform guides and students with every step in the project submission.',1,3,17,1,'Python, Flask, HTML, CSS, JS, Jinja and Bootstrap','2019-10-03 22:38:45.193215');
INSERT INTO "project" VALUES (2,'Training And Placement Management System','002-TRAI-FUR','The main objective of Training And Placement Management System is to develop a
software which manages placement activities in college makes an interactive GUI where TPO
can manages details of all students on his console, he can send mails to students informing
about placement activities.
Although such project has a very wide scope , this project contains the most important part i.e.
displaying the personal and academic information of a student and company. Students and
TPO are also provided with the facility of editing some fields like username and
password. TPO can also delete the student and company information after placement is over from
the main database.',1,1,9,2,'HTML, CSS, JavaScript, PHP, Parsley.js, JQuery, Bootstrap, Laravel, Ajax','2019-10-04 13:58:14.264799');
INSERT INTO "project" VALUES (3,'House Rental','003-HOUS-ASH','House rental portal is a webpage where house owners, clients, customers can exchange information effectively and inexpensively.

Provides user-friendly interface, satisfying the needs of the consumers.

Employs a new strategy that facilitates easy management of rental houses.
Online rental house portal is designed to meet every aspect of the consumers.
Features commercial and residential properties for the sale and rent properties.
To simplify work for the rental managers so that work can be efficient and effective.',1,12,7,3,'html,css,sql','2019-10-04 14:11:14.264799');
INSERT INTO "project" VALUES (4,'Hostel management software','004-HOST-SUC','It''s a hostel management software designed to create online database of hostel admission and details. It provides a detailed structure of hostel and it''s members including fees details.',1,5,17,4,'HTML and JAVA SCRIPT ','2019-10-04 14:11:14.264799');
INSERT INTO "project" VALUES (5,'Grocery store management system ','005-GROC-RAV','this project is develop in python in that we can add item ,delete  item & update item .  and second module is billing in that we can create a bill of customer. in this project use database is a SQL Lite. ',1,7,6,5,'python,SQL Lite','2019-10-04 14:37:14.264799');
INSERT INTO "project" VALUES (6,'Pycoder','006-PYCO-MIN','The purpose of our project is to provide more interactive and hustle free learning platform for Python programming language. This platform will divide the language into different modules or levels in order to learn the language in steps and in an efficient and effective manner. Ultimately, this will result in better understanding of basic concepts of language which eventually develop the logic. First of all, the user has to watch a video based on a concept then, he/she will be thrown by some questions based on the video. Then based on how he/she responds to the questions the system will analyze how much he/she has understood and will take next relevant step.At the end of lesson, he/she will be given an assignment which has to be solved and marks will be given according to the completeness and correctness of the code ',1,1,5,6,'HTML, CSS, JS, Flask, Python, Bootstrap, JINJA2','2019-10-04 15:20:14.264799');
INSERT INTO "project" VALUES (7,'IT Sector Stock Market','007-ITS-BIL','This Project aims to study, construct and evaluate the investment strategies of various companies in order to analyse past stock exchanges and give the viewers a clear idea about which companies or organisations will be earning more profit.',1,8,13,7,'XAMPP, HTML, php, MySql, CSS, Bootstrap','2019-10-04 15:28:14.264799');
INSERT INTO "project" VALUES (8,'online notice board','008-ONLI-SYE','online notice board is a place where you will get all the important updates of your academic as well as another important notices . This is a  website.',1,16,3,8,'Python,Bootstrap,css,html.','2019-10-04 15:34:14.264799');
INSERT INTO "project" VALUES (9,'Online Quiz Website','009-ONLI-POO','online quiz website is where you get various questions on different subjects to test your subject knowledge. It will help to quickly revise your concepts.',1,13,3,9,'PYTHON,HTML,CSS,BOOTSTRAP','2019-10-04 15:36:26.629484');
INSERT INTO "project" VALUES (10,'Contact Management System for MGM','010-CONT-SNE','Contact Management System project is written in Python. This is a simple GUI based project which is very easy to understand and use. It contains all the required functions which include adding, viewing, deleting and updating contact lists. While adding the contact of a person, he/she has to provide first name, last name, gender, address and contact details. The user can also update the contact list if he/she wants to. For this, the user has to double-click on a record that he/she wishes to edit. The system shows the contact details in a list view. And also the user easily delete any contact details.',1,8,9,10,'Python','2019-10-04 16:26:26.629484');
INSERT INTO "project" VALUES (11,'Online MGM Magazine','011-ONLI-PRA','Basically Online MGM magazine , is which  represents all the events which are occurred during academics .This magazine is basically divided into 3 section . First one for Events section,Second is for Article section and Third section is for the Posts .The Post section includes the day to day news.',1,15,12,11,'HTML, PHP, MYSQL .','2019-10-04 19:05:11.131150');
INSERT INTO "team" VALUES (1,'MGM Project Management Team');
INSERT INTO "team" VALUES (2,'Prefix');
INSERT INTO "team" VALUES (3,'Rambling Masters');
INSERT INTO "team" VALUES (4,'Error 404 ');
INSERT INTO "team" VALUES (5,'HexaNovate');
INSERT INTO "team" VALUES (6,'Pycoder developers');
INSERT INTO "team" VALUES (7,'Stock Market MGM');
INSERT INTO "team" VALUES (8,'dreamers');
INSERT INTO "team" VALUES (9,'WINNERS');
INSERT INTO "team" VALUES (10,'Dreamers');
INSERT INTO "team" VALUES (11,'Team magazine developers');
COMMIT;
