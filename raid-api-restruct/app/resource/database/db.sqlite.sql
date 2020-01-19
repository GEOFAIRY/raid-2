BEGIN TRANSACTION;
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
DROP TABLE IF EXISTS "phase";
CREATE TABLE IF NOT EXISTS "phase" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"raidId"	INTEGER,
	"order"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	FOREIGN KEY("raidId") REFERENCES "raid"("id")
);
DROP TABLE IF EXISTS "raid";
CREATE TABLE IF NOT EXISTS "raid" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT,
	"image"	TEXT
);
DROP TABLE IF EXISTS "partyUser";
CREATE TABLE IF NOT EXISTS "partyUser" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"partyId"	INTEGER NOT NULL,
	"userId"	INTEGER NOT NULL,
	"status"	TEXT,
	"leader"	BOOLEAN NOT NULL,
	FOREIGN KEY("partyId") REFERENCES "partyUser"("id"),
	FOREIGN KEY("userId") REFERENCES "user"("id")
);
DROP TABLE IF EXISTS "party";
CREATE TABLE IF NOT EXISTS "party" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"sherpa"	BOOLEAN NOT NULL,
	"timeCreated"	DATETIME NOT NULL
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
COMMIT;
