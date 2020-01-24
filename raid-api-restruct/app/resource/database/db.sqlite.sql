BEGIN TRANSACTION;
DROP TABLE IF EXISTS "party_user";
CREATE TABLE IF NOT EXISTS "party_user" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"partyId"	INTEGER NOT NULL,
	"userId"	INTEGER NOT NULL,
	"status"	TEXT,
	"leader"	BOOLEAN NOT NULL,
	FOREIGN KEY("partyId") REFERENCES "party_user"("id"),
	FOREIGN KEY("userId") REFERENCES "user"("id")
);
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"steamId"	TEXT UNIQUE,
	"password"	TEXT NOT NULL,
	"displayName"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"timeCreated"	DATETIME NOT NULL
);
DROP TABLE IF EXISTS "party";
CREATE TABLE IF NOT EXISTS "party" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"sherpa"	BOOLEAN NOT NULL,
	"timeCreated"	DATETIME NOT NULL
);
DROP TABLE IF EXISTS "raid";
CREATE TABLE IF NOT EXISTS "raid" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"image"	TEXT
);
DROP TABLE IF EXISTS "phase";
CREATE TABLE IF NOT EXISTS "phase" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"raidId"	INTEGER,
	"order"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	FOREIGN KEY("raidId") REFERENCES "raid"("id")
);
DROP TABLE IF EXISTS "game";
CREATE TABLE IF NOT EXISTS "game" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"raidId"	INTEGER,
	"partyId"	INTEGER,
	"status"	TEXT,
	"timeCreated"	DATETIME,
	FOREIGN KEY("raidId") REFERENCES "raid"("id"),
	FOREIGN KEY("partyId") REFERENCES "party"("id")
);
INSERT INTO "user" VALUES (1,'1234','$5$rounds=535000$rNuIBuJqUmUO6WlJ$q.lpwDGBY0oCnMWJ9HvfwddMwmR/tLbOUf8HM4ZxFS1','TEST','test@test.com','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (2,'2222','$5$rounds=535000$J4zZVYrIRAU.nhAB$Wma6idBL9HYs9E9AJiJ5tPZPFeTHwjQwe1uZJlZ2Ab0','TEST2','test@2','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (3,'3333','$5$rounds=535000$viorPghlBVU7ONDm$lKHUsDHJQNiqXG1CKInmWiTy6z71LRMiXr9u3.jdeN.','TEST3','test@3','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (4,'4444','$5$rounds=535000$Y0JbPp/b4jP1UnMv$/mgj5i6aQp.Vf4nXsWVC0AxdJDoYH/MPoTjmBChps16','TEST4','test@4','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (5,'5555','$5$rounds=535000$QcCypl9GQ7/CTsUy$QDKTgnJiZxzN29iYQ7JxPhS34vwyo6V3qWrw5kMEXp4','TEST5','test@5','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (6,'6666','$5$rounds=535000$ZAPjqpezSuPcb82S$I6wWUQtcliXBpgtOAvjyqZtGIxo26kuHvDZs0tp3ey3','TEST6','test@6','2020-01-19 14:34:16');
INSERT INTO "user" VALUES (7,'7777','$5$rounds=535000$JIYUHvLASUAvpEke$0tNYRgYCwsuOzFm2sZ75Aqnen5Soone5cxO2bDeVk75','TEST7','test@7','2020-01-19 14:34:11');
INSERT INTO "raid" VALUES (1,'Leviathan','https://stats.bungie.net/img/destiny_content/pgcr/raid_gluttony.jpg');
INSERT INTO "raid" VALUES (2,'Eater of Worlds','https://stats.bungie.net/img/destiny_content/pgcr/raids_leviathan_eater_of_worlds.jpg');
INSERT INTO "raid" VALUES (3,'Spire of Stars','https://stats.bungie.net/img/destiny_content/pgcr/raid_greed.jpg');
INSERT INTO "raid" VALUES (4,'The Last Wish','https://stats.bungie.net/img/destiny_content/pgcr/raid_beanstalk.jpg');
INSERT INTO "raid" VALUES (5,'Scourge of the Past','https://stats.bungie.net/img/destiny_content/pgcr/raids.1305rh0093145r13t5hn10tnz.raid_sunset.jpg');
INSERT INTO "raid" VALUES (6,'Crown of Sorrow','https://stats.bungie.net/img/destiny_content/pgcr/raid_eclipse.jpg');
INSERT INTO "raid" VALUES (7,'Garden of Salvation','https://stats.bungie.net/img/destiny_content/pgcr/raid_garden_of_salvation.jpg');
INSERT INTO "phase" VALUES (1,1,1,'Castellum');
INSERT INTO "phase" VALUES (2,1,2,'Royal Pools');
INSERT INTO "phase" VALUES (3,1,2,'Pleasure Gardens');
INSERT INTO "phase" VALUES (4,1,2,'Gauntlet');
INSERT INTO "phase" VALUES (5,1,3,'Throne Room');
INSERT INTO "phase" VALUES (6,2,1,'Leviathan Reactor');
INSERT INTO "phase" VALUES (7,2,2,'Engine Room');
INSERT INTO "phase" VALUES (8,2,3,'Argos'' Barrier');
INSERT INTO "phase" VALUES (9,2,4,'Argos');
INSERT INTO "phase" VALUES (10,3,1,'Statue Garden');
INSERT INTO "phase" VALUES (11,3,2,'Power Conduit');
INSERT INTO "phase" VALUES (12,3,3,'Celestial Observatory');
INSERT INTO "phase" VALUES (13,3,4,'Val Ca’our');
INSERT INTO "phase" VALUES (14,4,1,'Kalli the Corrupted');
INSERT INTO "phase" VALUES (15,4,2,'Shuro Chi the Corrupted');
INSERT INTO "phase" VALUES (16,4,3,'Morgeth the Spirekeeper');
INSERT INTO "phase" VALUES (17,4,4,'The Vault');
INSERT INTO "phase" VALUES (18,4,5,'Riven of a Thousand Voices');
INSERT INTO "phase" VALUES (19,4,6,'Queenswalk');
INSERT INTO "phase" VALUES (20,5,1,'Botza District');
INSERT INTO "phase" VALUES (21,5,2,'Botza Underground');
INSERT INTO "phase" VALUES (22,5,3,'Vault Access');
INSERT INTO "phase" VALUES (23,5,4,'Insurrection Prime');
INSERT INTO "phase" VALUES (24,6,1,'Witch''s Ritual');
INSERT INTO "phase" VALUES (25,6,2,'The Bridge');
INSERT INTO "phase" VALUES (26,6,3,'Gahlran''s Deception');
INSERT INTO "phase" VALUES (27,6,4,'Gahlran, The Sorrow-Bearer');
INSERT INTO "phase" VALUES (28,7,1,'Embrace');
INSERT INTO "phase" VALUES (29,7,2,'Undergrowth');
INSERT INTO "phase" VALUES (30,7,3,'The Consecrated Mind');
INSERT INTO "phase" VALUES (31,7,4,'The Sanctified Mind');
COMMIT;
