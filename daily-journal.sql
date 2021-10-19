create table "Mood" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"label"	TEXT NOT NULL
);
drop table Entry
create table "Entry" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"concept"	TEXT NOT NULL,
	"entry"	TEXT NOT NULL,
    "moodId" INTEGER NOT NULL,
    "date" INTEGER NOT NULL,
    FOREIGN KEY("moodId") REFERENCES "Mood"("id")
);


create table "Tag" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"label"	TEXT NOT NULL
);

create table "EntryTag" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"tag_id" integer not null,
    "entry_id" integer not null,
    FOREIGN KEY("tag_id") REFERENCES "Tag"("id"),
    FOREIGN KEY("entry_id") REFERENCES "Entry"("id")
);

insert into "mood" values (null, "Happy");
insert into "mood" values (null, "Sad");
insert into "mood" values (null, "Angry");
insert into "mood" values (null, "Ok");
insert into "entry" values (null, "Javascript", "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.", 1, "Wed Sep 15 2021 10:11:33");
insert into "entry" values (null, "Python", "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", 4, "Wed Sep 15 2021 10:11:33");
insert into "entry" values (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", 1, "Wed Sep 15 2021 10:11:33");
insert into "entry" values (null, "Javascript", "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.", 3, "Wed Sep 15 2021 10:11:33");
insert into "tag" values (null, "Front End");
insert into "tag" values (null, "Back End");
insert into "tag" values (null, "Programming");

