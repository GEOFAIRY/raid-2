BEGIN TRANSACTION;
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"steamId"	VARCHAR UNIQUE,
	"password"	VARCHAR NOT NULL,
	"displayName"	VARCHAR NOT NULL,
	"email"	VARCHAR UNIQUE,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "raids";
CREATE TABLE IF NOT EXISTS "raids" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR,
	"image"	VARCHAR,
	"phases"	VARCHAR,
	PRIMARY KEY("id")
);
INSERT INTO "users" ("id","steamId","password","displayName","email") VALUES (1,'812929198329389201','$5$rounds=535000$YQ/5FfjgizbaPs5l$vQT7T/FZwrSpLzAt42Vj0fCUzEqF1y2s9ubjn8BG0M5','GEOFAIRY','krs19@live.com');
INSERT INTO "users" ("id","steamId","password","displayName","email") VALUES (2,'7337473742382249','$5$rounds=535000$A0fYziRIEnMjkXLG$n0BKeIQky1Ijh08AfqbjKyj6vnAemPTGrWBimP1.Am/','kyrans19','kyrans19@gmail.com');
INSERT INTO "raids" ("id","name","image","phases") VALUES (1,'Leviathan','https://stats.bungie.net/img/destiny_content/pgcr/raid_gluttony.jpg','Royal Pools, Pleasure Gardens, The Gauntlet, Emperor Calus');
INSERT INTO "raids" ("id","name","image","phases") VALUES (2,'Eater of Worlds','https://stats.bungie.net/img/destiny_content/pgcr/raids_leviathan_eater_of_worlds.jpg','Eater of Worlds: Lair, Eater of Worlds: Argos');
INSERT INTO "raids" ("id","name","image","phases") VALUES (3,'Spire of Stars','https://stats.bungie.net/img/destiny_content/pgcr/raid_greed.jpg','Power Conduits, Celestial Observatory, Val Ca’our');
INSERT INTO "raids" ("id","name","image","phases") VALUES (4,'The Last Wish','https://stats.bungie.net/img/destiny_content/pgcr/raid_beanstalk.jpg','Shuro Chi, Morgeth, The Vault, Riven, The Queenswalk');
INSERT INTO "raids" ("id","name","image","phases") VALUES (5,'Scourge of the Past','https://stats.bungie.net/img/destiny_content/pgcr/raids.1305rh0093145r13t5hn10tnz.raid_sunset.jpg','Servitor Chase, Insurection Prime: Tanks, Insurection Prime');
INSERT INTO "raids" ("id","name","image","phases") VALUES (6,'Crown of Sorrow','https://stats.bungie.net/img/destiny_content/pgcr/raid_eclipse.jpg','The Bridge, Gahlran''s Deception, Gahlran The Sorrow Bearer');
INSERT INTO "raids" ("id","name","image","phases") VALUES (7,'Garden of Salvation','https://stats.bungie.net/img/destiny_content/pgcr/raid_garden_of_salvation.jpg','Summon The Consecrated Mind, Defeat The Consecrated Mind, Deafeat The Sanctified Mind');
COMMIT;
