CREATE DATABASE IF NOT EXISTS web_app;
USE web_app;


create table if not exists user (
	id int	not null auto_increment,
	username varchar(45) not null,
	password varchar(45) not null,
    primary key(id),
	unique(username)
);

create table if not exists contact (
	id int	not null auto_increment,
	type varchar(45) not null,
	name varchar(45) not null,
	surname varchar(45) not null,
	value varchar(45) not null,
	user_id int not null,
    primary key(id),
    foreign key(user_id) references user(id)
);
