BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Feedback" (
	"id"	INTEGER NOT NULL,
	"user_Id"	INTEGER NOT NULL,
	"poem_Id"	INTEGER NOT NULL,
	"qualifications"	INTEGER NOT NULL,
	"comment"	VARCHAR(100) NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_Id") REFERENCES "User"("id"),
	FOREIGN KEY("poem_Id") REFERENCES "Poem"("id")
);
CREATE TABLE IF NOT EXISTS "Poem" (
	"id"	INTEGER NOT NULL,
	"title"	VARCHAR(100) NOT NULL,
	"content"	VARCHAR(100) NOT NULL,
	"user_Id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_Id") REFERENCES "User"("id")
);
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(100) NOT NULL,
	"email"	VARCHAR(100) NOT NULL,
	"password"	VARCHAR(100) NOT NULL,
	"admin"	BOOLEAN NOT NULL,
	PRIMARY KEY("id")
);
COMMIT;