BEGIN TRANSACTION;
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"id" INTEGER NOT NULL, 
	"steamId" VARCHAR, 
	"password" VARCHAR NOT NULL, 
	"displayName" VARCHAR NOT NULL, 
	"email" VARCHAR, 
	"timeCreated" DATETIME, 
	PRIMARY KEY ("id"), 
	UNIQUE ("steamId"), 
	UNIQUE ("email")
);
DROP TABLE IF EXISTS "raids";
CREATE TABLE IF NOT EXISTS "raids" (
	"id" INTEGER NOT NULL, 
	"name" VARCHAR, 
	"image" VARCHAR, 
	"phases" VARCHAR, 
	PRIMARY KEY ("id")
);
DROP TABLE IF EXISTS "parties";
CREATE TABLE 'parties' (
	"partyId" INTEGER NOT NULL, 
	"raidId" INTEGER NOT NULL, 
	"status" VARCHAR NOT NULL, 
	"user1Id" INTEGER NOT NULL, 
	"user2Id" INTEGER, 
	"user3Id" INTEGER, 
	"user4Id" INTEGER, 
	"user5Id" INTEGER, 
	"user6Id" INTEGER, 
	"phase" INTEGER NOT NULL, 
	"sherpa" BOOLEAN NOT NULL, 
	"timeCreated" DATETIME, 
	PRIMARY KEY ("partyId"), 
	FOREIGN KEY("raidId") REFERENCES "raids" ("id"), 
	FOREIGN KEY("user1Id") REFERENCES "users" ("id"), 
	FOREIGN KEY("user2Id") REFERENCES "users" ("id"), 
	FOREIGN KEY("user3Id") REFERENCES "users" ("id"), 
	FOREIGN KEY("user4Id") REFERENCES "users" ("id"), 
	FOREIGN KEY("user5Id") REFERENCES "users" ("id"), 
	FOREIGN KEY("user6Id") REFERENCES "users" ("id"), 
	CHECK ("sherpa" IN (0, 1))
);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (1,'1234','$5$rounds=535000$rNuIBuJqUmUO6WlJ$q.lpwDGBY0oCnMWJ9HvfwddMwmR/tLbOUf8HM4ZxFS1','TEST','test@test.com', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (2,'2222','$5$rounds=535000$J4zZVYrIRAU.nhAB$Wma6idBL9HYs9E9AJiJ5tPZPFeTHwjQwe1uZJlZ2Ab0','TEST2','test@2', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (3,'3333','$5$rounds=535000$viorPghlBVU7ONDm$lKHUsDHJQNiqXG1CKInmWiTy6z71LRMiXr9u3.jdeN.','TEST3','test@3', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (4,'4444','$5$rounds=535000$Y0JbPp/b4jP1UnMv$/mgj5i6aQp.Vf4nXsWVC0AxdJDoYH/MPoTjmBChps16','TEST4','test@4', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (5,'5555','$5$rounds=535000$QcCypl9GQ7/CTsUy$QDKTgnJiZxzN29iYQ7JxPhS34vwyo6V3qWrw5kMEXp4','TEST5','test@5', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (6,'6666','$5$rounds=535000$ZAPjqpezSuPcb82S$I6wWUQtcliXBpgtOAvjyqZtGIxo26kuHvDZs0tp3ey3','TEST6','test@6', CURRENT_TIMESTAMP);
INSERT INTO "users" ("id","steamId","password","displayName","email", "timeCreated") VALUES (7,'7777','$5$rounds=535000$JIYUHvLASUAvpEke$0tNYRgYCwsuOzFm2sZ75Aqnen5Soone5cxO2bDeVk75','TEST7','test@7', CURRENT_TIMESTAMP);

INSERT INTO "raids" ("id","name","image","phases") VALUES (1,'Leviathan','https://stats.bungie.net/img/destiny_content/pgcr/raid_gluttony.jpg','Royal Pools, Pleasure Gardens, The Gauntlet, Emperor Calus');
INSERT INTO "raids" ("id","name","image","phases") VALUES (2,'Eater of Worlds','https://stats.bungie.net/img/destiny_content/pgcr/raids_leviathan_eater_of_worlds.jpg','Eater of Worlds: Lair, Eater of Worlds: Argos');
INSERT INTO "raids" ("id","name","image","phases") VALUES (3,'Spire of Stars','https://stats.bungie.net/img/destiny_content/pgcr/raid_greed.jpg','Power Conduits, Celestial Observatory, Val Ca’our');
INSERT INTO "raids" ("id","name","image","phases") VALUES (4,'The Last Wish','https://stats.bungie.net/img/destiny_content/pgcr/raid_beanstalk.jpg','Shuro Chi, Morgeth, The Vault, Riven, The Queenswalk');
INSERT INTO "raids" ("id","name","image","phases") VALUES (5,'Scourge of the Past','https://stats.bungie.net/img/destiny_content/pgcr/raids.1305rh0093145r13t5hn10tnz.raid_sunset.jpg','Servitor Chase, Insurection Prime: Tanks, Insurection Prime');
INSERT INTO "raids" ("id","name","image","phases") VALUES (6,'Crown of Sorrow','https://stats.bungie.net/img/destiny_content/pgcr/raid_eclipse.jpg','The Bridge, Gahlran''s Deception, Gahlran The Sorrow Bearer');
INSERT INTO "raids" ("id","name","image","phases") VALUES (7,'Garden of Salvation','https://stats.bungie.net/img/destiny_content/pgcr/raid_garden_of_salvation.jpg','Summon The Consecrated Mind, Defeat The Consecrated Mind, Deafeat The Sanctified Mind');
COMMIT;
