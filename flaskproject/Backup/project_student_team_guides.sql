BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "student" (
	"id"	INTEGER NOT NULL,
	"team_id"	INTEGER,
	"name"	VARCHAR(50) NOT NULL UNIQUE,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"phone"	VARCHAR(10) NOT NULL UNIQUE,
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
	"name"	VARCHAR(50) NOT NULL UNIQUE,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "guide" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"username"	VARCHAR(8) NOT NULL UNIQUE,
	"password"	VARCHAR(8) NOT NULL,
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
INSERT INTO "student" VALUES (27,13,'Neha Ukrande','nehaukrande@gmail.com','9766648487','A');
INSERT INTO "student" VALUES (28,13,'Sampada Kapratwar','sampadakapratwar1999@gmail.com','8459848882','A');
INSERT INTO "student" VALUES (29,14,'Vaishnavi Lagaskar','vaishnavilagaskar2598@gmail.com','7558797605','A');
INSERT INTO "student" VALUES (30,14,'Avantika Rachchawar','avantirachchawar@gmail.com','7517881083','A');
INSERT INTO "student" VALUES (31,15,'Sanjivani Bodke','sanjivanibodke2110@gmail.com','9604335178','A');
INSERT INTO "student" VALUES (32,15,'Rutuja Ambekar','rutujaambekar28@gmail.com','7083491717','A');
INSERT INTO "student" VALUES (33,16,'Richa Jha','richajha903@gmail.com','7038551145','A');
INSERT INTO "student" VALUES (34,16,'Bhakti Janakwadeb','bhaktijanakwade134@gmail.com','8208459348','A');
INSERT INTO "student" VALUES (35,17,'Vedashree Pande','vedapande25@gmail.com','8180089409','A');
INSERT INTO "student" VALUES (36,17,'Chandana Motiwar','chandanagoud26@gmail.com','8329659237','A');
INSERT INTO "student" VALUES (38,19,'Snehal Damkondwar','snehaldamkondwar403@gmail.com','9403114937','A');
INSERT INTO "student" VALUES (39,19,'Pooja Bhanushali','poojabhanu04@gmail.com','9119482823','A');
INSERT INTO "student" VALUES (40,20,'Vasudha Kawtikwar','vasudhak99@gmail.com','8830185377','A');
INSERT INTO "student" VALUES (41,21,'Joshi Gargi Suresh','pj04763@gmail.com','9503189472','A');
INSERT INTO "student" VALUES (42,21,'Dhone P R','purvadhone@gmail.com','9130929072','A');
INSERT INTO "student" VALUES (43,22,'Supriya Bhadre','supriyabhadre21@gmail.com','9049565179','A');
INSERT INTO "student" VALUES (44,22,'Nikita Borwandkar','nikitaborwandkar24@gmil.com','7499688547','A');
INSERT INTO "student" VALUES (45,23,'Suraj Kawadkar','suraj.kawadkar14@gmail.com','9552299457','A');
INSERT INTO "student" VALUES (46,23,'Govinda Kankal','gkankal46@gmail.com','8888354142','A');
INSERT INTO "student" VALUES (47,24,'Shivani Vaidya','shivanip.vaidya@gmail.com','7757001963','A');
INSERT INTO "student" VALUES (48,24,'Pratiksha Walbe ','pratikshawalbe@gmail.com','7020944092','A');
INSERT INTO "student" VALUES (49,25,'Kartiki Shinde','kartikishinde23919@gmail.com','9421462107','A');
INSERT INTO "student" VALUES (50,25,'Vaishnavi Yerrawar','vaishnaviyerrawar14@gmail.com','8408843111','A');
INSERT INTO "student" VALUES (51,26,'Pooja Yerawar','poojayerawar2@gmail.com','7057808277','A');
INSERT INTO "student" VALUES (52,26,'Sakshi Tanurkar','sakshi.tanurkar@gmail.com','8208132873','A');
INSERT INTO "student" VALUES (53,27,'Ashwini Ambulgekar','ambulgekarashwini77@gmail.com','8624962112','A');
INSERT INTO "student" VALUES (54,27,'Chhaya Gadade','chhayagadade55@gmail.com','9146956981','A');
INSERT INTO "student" VALUES (55,28,'Aarti Bodewar','aartibodewar@gmail.com','9096094621','A');
INSERT INTO "student" VALUES (56,28,'Rohini Nalwad','rohininalwad@gmail.com','9765730197','A');
INSERT INTO "student" VALUES (57,29,'Mayuree Humbad ','mayureeh8@gmail.com','9156343064','A');
INSERT INTO "student" VALUES (58,29,'Shrutika Kasture ','shrutikakasture05@gmail.com','9011600378','A');
INSERT INTO "student" VALUES (59,30,'Sadichcha Kulkarni','sadichchakulkarni@gmail.com','9370337125','A');
INSERT INTO "student" VALUES (60,30,'Mandar Majalgaonkar','mandarm111@gmail.com','9405935482','A');
INSERT INTO "student" VALUES (61,31,'Swapnaja Moralwar','swapnaja.moral99@gmail.com','9422966757','A');
INSERT INTO "student" VALUES (62,31,'Shweta Manhale','manhaleshweta@gmail.com','9637333893','A');
INSERT INTO "student" VALUES (63,32,'Vishakha Padamwar','padamwarvishakha98@gmail.com','7558575150','A');
INSERT INTO "student" VALUES (64,32,'Nishi Varvante ','nishigandhavarvante@gmail.com','9284794520','A');
INSERT INTO "student" VALUES (65,33,'Parmeshwari Biyani','parmeshwaribiyani1998@gmail.com','7028332461','A');
INSERT INTO "student" VALUES (66,33,'Vaishnavi Kotgire','vaishnavikotgire1998@gmail.com','9404774211','A');
INSERT INTO "student" VALUES (67,34,'Shamali Gattani','shamaligattani@gmail.com','8668879508','A');
INSERT INTO "student" VALUES (68,34,'Soujanya Gandi','soujanyagandi701@gmail.com','7057461968','A');
INSERT INTO "student" VALUES (69,35,'Bacchewar Shivani','bacchewarshivani@gmail.com','7887738401','A');
INSERT INTO "student" VALUES (70,35,'Chalikwar Sonal ','chalikwarsonal2@gmail.com','7875596969','A');
INSERT INTO "student" VALUES (71,36,'Prem Agrawal','premagr28@gmail.com','8421416474','A');
INSERT INTO "student" VALUES (72,36,'Samiksha Kulkarni','samikshakulkarni912@gmail.com','9881597951','A');
INSERT INTO "student" VALUES (73,37,'Rushikesh Nigadge','rishikeshn69@gmail.com','8999508594','A');
INSERT INTO "student" VALUES (74,37,'Atharva Boralkar','atharvab5495@gmail.com','8379812608','A');
INSERT INTO "student" VALUES (75,38,'Narwade Nikita ','nikitanareade1996@gmail.com','9527770627','A');
INSERT INTO "student" VALUES (76,38,'Raghav Deshpande','raghavdeshpande1000@gmail.com','9284572518','A');
INSERT INTO "student" VALUES (78,40,'Rakshanda Shete','rakshandashete1997@gmail.com','7378726961','B');
INSERT INTO "student" VALUES (79,40,'Pratiksha Pawar','pratikshapawar1220@gmail.com','8552088463','B');
INSERT INTO "student" VALUES (80,41,'Bulbule Rakshanda','rakshandabulbule66@gmail.com','9175526402','B');
INSERT INTO "student" VALUES (81,41,'Khodke Geeta ','khodkegeeta1996@gmail.com','7083703402','B');
INSERT INTO "student" VALUES (82,42,'Gurhale Rushikesh','rushikesh.gurhale0@gmail.com','7387155696','B');
INSERT INTO "student" VALUES (83,42,'Trimale Priyanka','priyatrimale@gmail.com','7057826393','B');
INSERT INTO "student" VALUES (84,43,'Nilawar Shradha','nilawarshradha@gmail.com','9156959484','B');
INSERT INTO "student" VALUES (85,43,'Rushikesh Sandukwar','rushi.sandukwar701@gmail.com','9850701133','B');
INSERT INTO "student" VALUES (86,44,'Rohini Mangnale','rohinimangnale23@gmail.com','7385455145','B');
INSERT INTO "student" VALUES (87,44,'Sakshi  Darbastewar','darbastewarsakshi15@gmail.com','9067749809','B');
INSERT INTO "student" VALUES (88,45,'Chapule Akshata','akchapule@gmail.com','7709836200','B');
INSERT INTO "student" VALUES (89,45,'Bhange Rupali','rupalibhange98@gmail.com','9373807146','B');
INSERT INTO "student" VALUES (90,46,'Hallale Jyoti','jyotihallale12@gmail.com','7020958652','B');
INSERT INTO "student" VALUES (91,46,'Kulkarni Vaishnavi','kulkarnivaishu95@gmail.com','9970182738','B');
INSERT INTO "student" VALUES (92,47,'Awale Shubham','1awaleshubham1@gmail.com','9370136567','B');
INSERT INTO "student" VALUES (93,47,'Chincholkar Omkar','omchincholkar.sai.rob71@gmail.com','9766399733','B');
INSERT INTO "student" VALUES (94,48,'Deshmukh Shraddha','shraddhadeshmukh153@gmail.com','8605449633','B');
INSERT INTO "student" VALUES (95,48,'Dongare Pramodita','dongarepramodita@gmail.com','9860601357','B');
INSERT INTO "student" VALUES (96,49,'Bobde Neha','bobdeneha2@gmail.com','8446202894','B');
INSERT INTO "student" VALUES (97,49,'Gavhane Prajakta','prajaktagavhane9561@gmail.com','9545769561','B');
INSERT INTO "student" VALUES (98,50,'Chavan Ashwini','ashwinichavan303@gmail.com','9604327891','B');
INSERT INTO "student" VALUES (99,50,'Wandre Ankita','wandreankita97@gmail.com','8421100705','B');
INSERT INTO "student" VALUES (100,51,'Sangita Tekale','sangitatekale9075@gmail.com','7083021551','B');
INSERT INTO "student" VALUES (101,51,'Savita Tekale','savitatekale1234@gmail.com','7517273634','B');
INSERT INTO "student" VALUES (102,52,'Samiksha Mukhedkar ','mukhedkarsamiksha2409@gmail.com','7507837041','B');
INSERT INTO "student" VALUES (103,52,'Priyanka Kalaskar','priyanakalaskar@gmail.com','7888287523','B');
INSERT INTO "student" VALUES (104,53,'Waghmare Rupali','rupalikwaghmare@gmail.com','8888314462','B');
INSERT INTO "student" VALUES (105,53,'Shirse Mangaltai','mangal.shirse@gmail.com','9130914463','B');
INSERT INTO "student" VALUES (106,54,'Dhembre Shivam','ahivampatil201@gmail.com','9822185347','B');
INSERT INTO "student" VALUES (107,54,'Kharat Srikant','kharatsrikant@gmail.com','8007098117','B');
INSERT INTO "student" VALUES (108,55,'Pooja Pawar','poojapawar12866@gmail.com','9011727363','B');
INSERT INTO "student" VALUES (109,55,'Priyanka Populwar','populwarpriyanka@gmail.com','9673581510','B');
INSERT INTO "student" VALUES (110,56,'Waghraj Patil','waghrajpatil1699@gmail.com','8208895759','B');
INSERT INTO "student" VALUES (111,56,'Dipak Sabbanwar','sabbanwardipak@gmail.com','7350844378','B');
INSERT INTO "student" VALUES (112,57,'Kavita Chavan','kavita.ramesh.c18@gmail.com','7249647166','B');
INSERT INTO "student" VALUES (113,57,'Nikita Chavan','nikitachavan22446689@gmail.com','8483912321','B');
INSERT INTO "student" VALUES (114,58,'Khandare Pallavi','pallavikhandare910@gmail.com','8888290354','B');
INSERT INTO "student" VALUES (115,58,'Godbole Supriya','supriyagodbole1998@gmail.com','9172008715','B');
INSERT INTO "student" VALUES (116,59,'Surabhi Palkratwar','surabhip.sp@gmail.com','9130197159','B');
INSERT INTO "student" VALUES (117,59,'Trupti Choudhary','ctrupti56@gmail.com','8482890182','B');
INSERT INTO "student" VALUES (118,60,'Santosh Suryawanshi','san412tosh@gmail.com','9146922667','B');
INSERT INTO "student" VALUES (119,60,'Mayuresh Pophale','mmayur283@gmail.com','9028278080','B');
INSERT INTO "student" VALUES (120,61,'Ruchita Bagdiya','ruchitabagdiya@gmail.com','7038698669','B');
INSERT INTO "student" VALUES (121,61,'Anuja Tehra','anujaatehra@gmail.com','8378840293','B');
INSERT INTO "student" VALUES (122,62,'Mahesh Suryawanshi','m.surya1432@gmail.com','9923415862','B');
INSERT INTO "student" VALUES (123,62,'Siddiqui Sufyan','sufyansid1998@gmail.com','9960046168','B');
INSERT INTO "student" VALUES (124,63,'Thorat Rajjeet','rs.thorat143@gmail.com','9146268206','B');
INSERT INTO "student" VALUES (125,63,'Suryawanshi Sachin','suryawanshisns358@gmail.com','8669705667','B');
INSERT INTO "student" VALUES (126,64,'Sayyad Fahad','Sdfahad48@gmail.com','7719805166','B');
INSERT INTO "student" VALUES (127,64,'Sumit Kumar','14sumit06@gmail.com','8295668120','B');
INSERT INTO "student" VALUES (128,65,'Chaware Vishal','chaware.vishal358@gmail.com','9730322637','B');
INSERT INTO "student" VALUES (129,65,'Shinde Purushottam','purushottam.shinde55@gmail.com','9421815755','B');
INSERT INTO "student" VALUES (130,66,'Kamble Sonam','sonam31kambl@gmail.com','8806485901','B');
INSERT INTO "student" VALUES (131,66,'Namoshe Pragati','pragatinamoshe16@gmail.com','7721905465','B');
INSERT INTO "student" VALUES (132,67,'Shraddha Mundada','shradhamundada1505@gmail.com','7972863365','A');
INSERT INTO "student" VALUES (133,67,'Shweta Bhadke','bhadkeshweta5@gmail.com','8482878806','A');
INSERT INTO "student" VALUES (134,68,'Anuj Chourange','chourangeanuj@gmail.com','9146679986','A');
INSERT INTO "student" VALUES (135,68,'Vipul Chinnawar','vipulchinnawar4@gmail.com','9923903538','A');
INSERT INTO "student" VALUES (136,69,'Mrunali Joshi','joshimrunali22@gmail.com','9403097751','A');
INSERT INTO "student" VALUES (137,69,'Divya Bandewar','bandewardivya14@gmail.com','8483932525','A');
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
INSERT INTO "project" VALUES (13,'Online Movie Ticket Booking','013-ONLI-NEH','Not Submitted',1,5,13,13,'Web based applications/ Apps','2019-10-06 12:33:32.763704');
INSERT INTO "project" VALUES (14,'Clinic Management System','014-CLIN-VAI','Not Submitted ?',1,12,3,14,'Web based applications/ Apps','2019-10-06 12:33:32.763704');
INSERT INTO "project" VALUES (15,'Movie Ratings System','015-MOVI-SAN','Not Submitted?',1,12,7,15,'Web based applications/ Apps','2019-10-06 12:33:32.763704');
INSERT INTO "project" VALUES (16,'Restaurant','016-REST-RIC','Not Submitted?',1,16,10,16,'Web based applications/ Apps','2019-10-06 12:33:32.763704');
INSERT INTO "project" VALUES (17,'Online Medical Store','017-ONLI-VED','Not Submitted',1,13,11,17,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (19,'Doctor Patient Portal','019-DOCT-SNE','Not Submitted',1,13,8,19,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (20,'Student Management ','020-STUD-VAS','Not Submitted',1,17,16,20,'Python','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (21,'Coder-Clash','021-CODE-JOS','Not Submitted',1,7,6,21,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (22,'Feedback form','022-FEED-SUP','Not Submitted',1,17,4,22,'Python Project','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (23,'Online Notice Board','023-ONLI-SUR','Not Submitted',1,17,9,23,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (24,'Firewall Design','024-FIRE-SHI','Not Submitted',1,3,16,24,'Computer Network','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (25,'Tourism APP','025-TOUR-KAR','Not Submitted',1,3,11,25,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (26,'Smart Parking System using Android','026-SMAR-POO','Not Submitted',1,11,8,26,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (27,'Mobile Comparison Project','027-MOBI-ASH','Not Submitted',1,11,12,27,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (28,'Computer Assembly Website Project','028-COMP-AAR','Not Submitted',1,15,14,28,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (29,'Online Shopping System ','029-ONLI-MAY','Not Submitted',1,6,5,29,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (30,'Foodmaza-Online Food Ordering','030-FOOD-SAD','Not Submitted',1,6,14,30,'WEB DEVELOPMENT','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (31,'Grocery Store System','031-GROC-SWA','Not Submitted',1,14,15,31,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (32,'College management system','032-COLL-VIS','Not Submitted',1,4,15,32,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (33,'Chromism game using Tkinter in Python','033-CHRO-PAR','Not Submitted',1,9,5,33,'GUI Application(Game) using Tkinter','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (34,'Color Game','034-COLO-SHA','Not Submitted',1,10,4,34,'Game','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (35,'Online Blood Donation ','035-ONLI-BAC','Not Submitted',1,10,8,35,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (36,'Nanded Pharmasuticals','036-NAND-PRE','Not Submitted',1,15,6,36,'Web based applications/ Apps','2019-10-06 18:30:25.086670');
INSERT INTO "project" VALUES (37,'Society Management System','037-SOCI-RUS','Digital platform for a secretary in order to operate a society perfectly. it contains all the details of member living in society number of residents and also which utilities are required daily. this digital platform can be accessed by any electronic device which has internet connection so that given prospective idea can be followed and accepted by the societies to easement of the work. ',1,14,17,37,'Web based applications ','2019-10-06 21:17:28.781350');
INSERT INTO "project" VALUES (38,'Online Ration store','038-ONLI-NAR','Effective in shopping ration products online and maintain the exact record of products available to customers',1,10,13,38,'PHP , CSS, HTML','2019-10-06 21:17:28.781350');
INSERT INTO "project" VALUES (40,'Calculator using tkinter in Python','040-CALC-RAK','Not Submitted!!',1,12,15,40,'Python Project','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (41,'Doctor Appointment Booking System','041-DOCT-BUL','Not Submitted !',1,17,3,41,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (42,'Publication Site','042-PUBL-GUR','Not Submitted!',1,7,6,42,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (43,'Canteen Management System','043-CANT-NIL','Not Submitted !',1,4,14,43,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (44,'Online Jwellrey Shopping System','044-ONLI-ROH','Not Submitted!',1,15,13,44,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (45,'Online Shopping Website','045-ONLI-CHA','Not Submitted!',1,5,16,45,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (46,'Mail Server','046-MAIL-HAL','Not Submitted!',1,15,3,46,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (47,'E-Farming','047-E-FA-AWA','Not Submitted!',1,4,16,47,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (48,'Real Estate Project','048-REAL-DES','Not Submitted!',1,10,6,48,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (49,'Online Food Ordering System','049-ONLI-BOB','Not Submitted!',1,17,5,49,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (50,'Online Mobile Shopping','050-ONLI-CHA','Not Submitted!',1,8,15,50,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (51,'Blood Bank Management System','051-BLOO-SAN','Not Submitted!',1,14,4,51,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (52,'Tourist Management System','052-TOUR-SAM','Not Submitted!',1,9,13,52,'WEB DEVELOPMENT','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (53,'Online Staff Leave System','053-ONLI-WAG','Not Submitted',1,7,12,53,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (54,'Android App','054-ANDR-DHE','Not Submitted',1,8,9,54,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (55,'Online Voting System for College Student','055-ONLI-POO','Not Submitted',1,10,7,55,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (56,'Online Video Player App','056-ONLI-WAG','Not Submitted!',1,6,17,56,'WEB DEVELOPMENT','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (57,'Online Movie Booking System','057-ONLI-KAV','Not Submitted!',1,13,12,57,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (58,'Pick and Drop Courier Service','058-PICK-KHA','Not Submitted',1,16,4,58,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (59,'Placement Activity System','059-PLAC-SUR','Not Submitted',1,9,11,59,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (60,'College Social Network Web Project','060-COLL-SAN','Not Submitted',1,11,5,60,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (61,'Exam Seating Arrangement System','061-EXAM-RUC','Not Submitted',1,15,6,61,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (62,'Face Recognition','062-FACE-MAH','Not Submitted',1,5,15,62,'WEB DEVELOPMENT','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (63,'Computerization of Manufacturing Unit','063-COMP-THO','Not Submitted',1,6,16,63,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (64,'Library Management System','064-LIBR-SAY','Not Submitted',1,9,12,64,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (65,'QR Code Attendance System','065-QRC-CHA','Not Submitted',1,16,11,65,'Web based applications/ Apps','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (66,'ETL and Reporting using SSIS & Power BI.','066-ETL-KAM','Part 1: 
We will be performing the ETL task by connecting to multiple datasources like 
1. Flat File Source
2. Excel File
3. OLEDB
4. CSV
performing different transformation and validations from the staging layer to loading data to data warehouse.

Part 2:
Creation of report using Power BI by using the data from Part 1.

We are using both tools of Microsoft  (ETL: SSIS, Reporting: Power BI)',1,4,9,66,'Integration Services','2019-10-07 23:08:14.518557');
INSERT INTO "project" VALUES (67,'Travel Guide Monitoring','067-TRAV-SHR','Not submitted',1,7,17,67,'Web based application','2019-10-08 23:19:54.479311');
INSERT INTO "project" VALUES (68,'Online Home Service Provider System','068-ONLI-ANU','It is a web application that would provide platform and interaction between customers and different service providers where, customers can find appropriate services for their needs and demands such as house cleaning, car washing, event managements, photographers etc. on this platform. Customers can also view portfolio of different service providers for the same services. They would get to choose the best service provider within their region/area.
	It helps customers hire trusted professionals for their service needs. Customers can also be able to see quotation for their event and choose the suitable one for them. This platform eases finding professional service providers for users as well as increases the productivity of service provider companies. This platform makes a difference in the lives of people by catering to their service needs on their fingertips.
This application will be developed using Mysql, PHP for backend,HTML, CSS,javascript ,Jquery and Bootstrap for frontend technologies. 
',1,9,7,68,'PHP,MYSQL,JAVASCRIPT,HTML,CSS,BOOTSTRAP,JQUERY','2019-10-17 13:13:21.171116');
INSERT INTO "project" VALUES (69,'Online Banking','069-ONLI-MRU','Developing a real demonstration  transaction based offline banking system',1,4,14,69,'HTML,CSS,PHP','2019-10-17 13:13:21.171116');
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
INSERT INTO "team" VALUES (13,'Annihilators');
INSERT INTO "team" VALUES (14,'The Avengers ');
INSERT INTO "team" VALUES (15,'Bad to The Bone');
INSERT INTO "team" VALUES (16,'Black Panthers');
INSERT INTO "team" VALUES (17,'Black Widows');
INSERT INTO "team" VALUES (19,'Blitzkrieg ');
INSERT INTO "team" VALUES (20,'Braindead Zombies');
INSERT INTO "team" VALUES (21,'Brewmaster Crew');
INSERT INTO "team" VALUES (22,'Brute Force');
INSERT INTO "team" VALUES (23,'Butchers');
INSERT INTO "team" VALUES (24,'Arcana  ');
INSERT INTO "team" VALUES (25,'Ghost Riders');
INSERT INTO "team" VALUES (26,'High-Voltage');
INSERT INTO "team" VALUES (27,'Tech Warriors');
INSERT INTO "team" VALUES (28,'Terminators');
INSERT INTO "team" VALUES (29,'The Bulldogs');
INSERT INTO "team" VALUES (30,'The Enemy');
INSERT INTO "team" VALUES (31,'The Firing Squad');
INSERT INTO "team" VALUES (32,'The Frontline');
INSERT INTO "team" VALUES (33,'The House Thrashers');
INSERT INTO "team" VALUES (34,'The Intimidators');
INSERT INTO "team" VALUES (35,'The Pitbulls');
INSERT INTO "team" VALUES (36,'The Unredeemable');
INSERT INTO "team" VALUES (37,'Good_Boys');
INSERT INTO "team" VALUES (38,'Raghav Deshpande and Nikita Narwade');
INSERT INTO "team" VALUES (40,'Agony of De Feet');
INSERT INTO "team" VALUES (41,'Don''t Stop Believing');
INSERT INTO "team" VALUES (42,'Win or Booze');
INSERT INTO "team" VALUES (43,'Hoops I Did It Again');
INSERT INTO "team" VALUES (44,'Blood Bath and Beyond');
INSERT INTO "team" VALUES (45,'Game of Cones');
INSERT INTO "team" VALUES (46,'Case of the Runs');
INSERT INTO "team" VALUES (47,'Staff Infection');
INSERT INTO "team" VALUES (48,'Free-Range Chickens');
INSERT INTO "team" VALUES (49,'Single Belles');
INSERT INTO "team" VALUES (50,'Dill With It');
INSERT INTO "team" VALUES (51,'Jesus Lizard');
INSERT INTO "team" VALUES (52,'No More Debt');
INSERT INTO "team" VALUES (53,'Hungry Hippos');
INSERT INTO "team" VALUES (54,'Smells like Team Spirit');
INSERT INTO "team" VALUES (55,'Nacho Average Squad');
INSERT INTO "team" VALUES (56,'Lord of the Rims');
INSERT INTO "team" VALUES (57,'Furious George');
INSERT INTO "team" VALUES (58,'The Beastie Balls');
INSERT INTO "team" VALUES (59,'Slam Dunkers');
INSERT INTO "team" VALUES (60,'Triple By Pass');
INSERT INTO "team" VALUES (61,'Here Comes the Run');
INSERT INTO "team" VALUES (62,'Mudder Runners');
INSERT INTO "team" VALUES (63,'Hell on Heels');
INSERT INTO "team" VALUES (64,'The Dementors');
INSERT INTO "team" VALUES (65,'Freakin'' Awesomes');
INSERT INTO "team" VALUES (66,'----');
INSERT INTO "team" VALUES (67,'Software Chasers');
INSERT INTO "team" VALUES (68,'PowerGrammers');
INSERT INTO "team" VALUES (69,'Mind Benders');
INSERT INTO "guide" VALUES (1,'Dr. Mrs. A. M. Rajurkar','rajurkar_am@mgmcen.ac.in','rajurkar_am','Pass@1234');
INSERT INTO "guide" VALUES (2,'Ms. Jyoti H. Patil','patil_jh@mgmcen.ac.in','patil_jh','Pass@1234');
INSERT INTO "guide" VALUES (3,'Dr. Mrs. Manisha Y. Joshi','joshi_my@mgmcen.ac.in','joshi_my','$2b$12$bhbtQ4XB.RFZk2ZlSbEwL.EWxbHU4Bj1ZUmBbsP9.A3b0uIOf9BiW');
INSERT INTO "guide" VALUES (4,'Mr. Salve Suhas G','salve_sg@mgmcen.ac.in','salve_sg','$2b$12$p1cuuN3zcgzyB1/K4qt80OthSVs138Vy7AEEpmXpWKWFLP5a4Avse');
INSERT INTO "guide" VALUES (5,'Ms. Kapre Bhagyashri Sudhakarrao','kapre_bs@mgmcen.ac.in','kapre_bs','$2b$12$tF/VcMtBD2aJH/pErf6b8uais6rTOGnbdyLGJkrR6DFd1.LYGKsOm');
INSERT INTO "guide" VALUES (6,'Mr. Pankaj P. Pawar','pawar_pankaj@mgmcen.ac.in','pawar_pankaj','Pass@1234');
INSERT INTO "guide" VALUES (7,'Mr. Mohammed Aijaz Ahmed','mohd_aijaz@mgmcen.ac.in','mohd_aijaz','Pass@1234');
INSERT INTO "guide" VALUES (8,'Mr. Mohseen Ahmed','mohseen_ahmed@mgmcen.ac.in','mohseen_ahmed','Pass@1234');
INSERT INTO "guide" VALUES (9,'Mr. Titare Shivprasad Indrajitsing','titare_si@mgmcen.ac.in','titare_si','Pass@1234');
INSERT INTO "guide" VALUES (10,'Ms. Wagre Savita Sambhaji','wagre_savita@mgmcen.ac.in','wagre_savita','Pass@1234');
INSERT INTO "guide" VALUES (11,'Ms. Nitu L. Pariyal','pariyal_nitu@mgmcen.ac.in','pariyal_nitu','pASS@1234');
INSERT INTO "guide" VALUES (12,'Mr. Chennoji M. R.','chennoji_mr@mgmcen.ac.in','chennoji_mr','pASS@1234');
INSERT INTO "guide" VALUES (13,'Ms. Kale Jyoti S.','kale_js@mgmcen.ac.in','kale_jyoti','$2b$12$5Ycf1rMKRDbSosJeecVwOuPE6zR6AWkPYtcyyzribHHXFNLVHOkeG');
INSERT INTO "guide" VALUES (14,'Mr. Rahulsingh G. Bisen','bisen_rg@mgmcen.ac.in','bisen_rg','$2b$12$XWpvcUSa.HQDfz8Or4Lq8eVFCkYuOL5obBEdYTFpXW.57zpzLLajO');
INSERT INTO "guide" VALUES (15,'Ms. Nikita S. Pande','pande_ns@mgmcen.ac.in','pande_ns','$2b$12$tIsABIK139spIKj2hQ5r0uqEb.e285GRzLNNFV1N1aM3VFZ7AXsgW');
INSERT INTO "guide" VALUES (16,'Mr. Juned Khan','junad_jk@mgmcen.ac.in','junad_jk','Pass@1234');
INSERT INTO "guide" VALUES (17,'Mr. Bhandare Mangesh Nagnath','bhandare_mn@mgmcen.ac.in','bhandare_mn','Pass@1234');
INSERT INTO "guide" VALUES (18,'Prashant Deshmukh','deshmukh_pk@mgmcen.ac.in','pkdeshmukh','scan@1234');
INSERT INTO "guide" VALUES (19,'Developer','mgms.projects@gmail.com','dev_abhiom','$2b$12$xa1Jo8FKKXsZSF411Cwcr.d8ME/a2hBz2BcednOvU6FokLj.Kjjp.');
COMMIT;
