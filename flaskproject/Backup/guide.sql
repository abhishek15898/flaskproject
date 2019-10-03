BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "guide" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"username"	VARCHAR(8) NOT NULL UNIQUE,
	"password"	VARCHAR(8) NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "guide" VALUES (1,'Dr. Mrs. A. M. Rajurkar','rajurkar_am@mgmcen.ac.in','rajurkar_am','Pass@1234');
INSERT INTO "guide" VALUES (2,'Ms. Jyoti H. Patil','patil_jh@mgmcen.ac.in','patil_jh','Pass@1234');
INSERT INTO "guide" VALUES (3,'Dr. Mrs. Manisha Y. Joshi','joshi_my@mgmcen.ac.in','joshi_my','Pass@1234');
INSERT INTO "guide" VALUES (4,'Mr. Salve Suhas G','salve_sg@mgmcen.ac.in','salve_sg','Pass@1234');
INSERT INTO "guide" VALUES (5,'Ms. Kapre Bhagyashri Sudhakarrao','kapre_bs@mgmcen.ac.in','kapre_bs','Pass@1234');
INSERT INTO "guide" VALUES (6,'Mr. Pankaj P. Pawar','pawar_pankaj@mgmcen.ac.in','pawar_pankaj','Pass@1234');
INSERT INTO "guide" VALUES (7,'Mr. Mohammed Aijaz Ahmed','mohd_aijaz@mgmcen.ac.in','mohd_aijaz','Pass@1234');
INSERT INTO "guide" VALUES (8,'Mr. Mohseen Ahmed','mohseen_ahmed@mgmcen.ac.in','mohseen_ahmed','Pass@1234');
INSERT INTO "guide" VALUES (9,'Mr. Titare Shivprasad Indrajitsing','titare_si@mgmcen.ac.in','titare_si','Pass@1234');
INSERT INTO "guide" VALUES (10,'Ms. Wagre Savita Sambhaji','wagre_savita@mgmcen.ac.in','wagre_savita','Pass@1234');
INSERT INTO "guide" VALUES (11,'Ms. Nitu L. Pariyal','pariyal_nitu@mgmcen.ac.in','pariyal_nitu','pASS@1234');
INSERT INTO "guide" VALUES (12,'Mr. Chennoji M. R.','chennoji_mr@mgmcen.ac.in','chennoji_mr','pASS@1234');
INSERT INTO "guide" VALUES (13,'Ms. Kale Jyoti S.','kale_js@mgmcen.ac.in','kale_jyoti','Pass@1234');
INSERT INTO "guide" VALUES (14,'Mr. Rahulsingh G. Bisen','bisen_rg@mgmcen.ac.in','bisen_rg','Pass@1234');
INSERT INTO "guide" VALUES (15,'Ms. Nikita S. Pande','pande_ns@mgmcen.ac.in','pande_ns','Pass@1234');
INSERT INTO "guide" VALUES (16,'Mr. Juned Khan','junad_jk@mgmcen.ac.in','junad_jk','Pass@1234');
INSERT INTO "guide" VALUES (17,'Mr. Bhandare Mangesh Nagnath','bhandare_mn@mgmcen.ac.in','bhandare_mn','Pass@1234');
INSERT INTO "guide" VALUES (18,'Prashant Deshmukh','deshmukh_pk@mgmcen.ac.in','pkdeshmukh','scan@1234');
COMMIT;
