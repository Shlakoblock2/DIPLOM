
create table ClientData(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    surname varchar(50),
    address varchar(50),
    phone_number varchar(50)
);

create table Post(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    power_level integer
);

create table Personal(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    surname varchar(50),
    post_id integer,
    foreign key (post_id) references Post(id)
);

create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    personal_id integer,
    foreign key (personal_id) references Personal(id)
);

create table ItemType(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table Item(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    price real,
    type_id integer,
    foreign key (type_id) references ItemType(id)
);

create table Deposit(
	id integer PRIMARY KEY autoincrement,
	item_id integer,
	metal varchar(50),
	test varchar(50),
	item_weight real,
	ClientData_id integer,
	Personal_id integer,
	foreign key (item_id) references Item(id),
	foreign key (ClientData_id) references ClientData(id),
	foreign key (Personal_id) references Personal(id)
);
