-- Jules McCurry
-- CYBR 410
-- WhatABook Scripts
-- August 12, 2022


-- drop database if exists --

DROP DATABASE IF EXISTS whatabook;

-- create database --
CREATE DATABASE whatabook;

-- use database --

USE whatabook;

-- drop user if exists 
DROP USER 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
create user 'whatabook_user'@'localhost' identified with mysql_native_password by 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- CREATING TABLES --

-- Drop tables if exists--
drop table if exists store;
drop table if exists book;
drop table if exists wishlist;

-- create table Book --
CREATE TABLE book (
  book_id int NOT NULL AUTO_INCREMENT,
  book_name varchar(200) NOT NULL,
  details varchar(500) DEFAULT NULL,
  author varchar(200) NOT NULL,
  PRIMARY KEY (book_id)
);

-- create table Store --
CREATE TABLE store (
  store_id int NOT NULL AUTO_INCREMENT,
  locale varchar(500) NOT NULL,
  hours varchar(500) NOT NULL,
  PRIMARY KEY (store_id)
);

-- create table User --
CREATE TABLE user (
  user_id int NOT NULL AUTO_INCREMENT,
  first_name varchar(75) NOT NULL,
  last_name varchar(75) NOT NULL,
  PRIMARY KEY (user_id)
);

-- create table Wishlist --
CREATE TABLE wishlist (
	wishlist_id int not null auto_increment,
	user_id int not null, 
	book_id int not null,
	primary key (wishlist_id)
);

-- POPULATING TABLES --

-- populate table Store --
INSERT INTO Store(store_id, locale, hours)
   VALUES(1,'Genitivi\'s. Located in Ferelden in Denerim\'s Market District.', 'Open dawn to dusk.');
   
-- populate table Book --
INSERT INTO book(book_id, book_name, details, author)
   VALUES(1,'Aveline, Knight of Orlais','Obtained from a book found in Redcliffe','Lord Francois Maigny');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(2,'Meditations and Odes to Bees','Obtained from a book found in the Redcliffe Estate','Anonymous');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(3,'Adventures of the Black Fox','Obtained from a book found in the Lothering Chantry','Gaston Gerrault');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(4,'The Holy Brazier','Obtained in the Ruined Temple','Father Kolgrim');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(5,'The Journal of Caridin','Obtained from a book found in Ortan Thaig','Caridin');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(6,'The Tale of Iloren','Obtained in the Dalish Camp','Zathrian');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(7,'Dane and the Werewolf','Obtained in the Pearl','Minstrel Uccam');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(8,'Death of a Templar','Obtained from a book found in the Village of Haven','Ser Andrew');

INSERT INTO book(book_id, book_name, details, author)
   VALUES(9,'A Very Chewed and Moist Book','Randomly found by Dog','Unknown');

-- populate table User --
INSERT INTO User(user_id, first_name, last_name)
   VALUES(1, 'Alistair', 'Therin');

INSERT INTO User(user_id, first_name, last_name)
   VALUES(2, 'Varric', 'Tethras');

INSERT INTO User(user_id, first_name, last_name)
   VALUES(3, 'Dorian', 'Pavus');

-- populate table Wishlist --
insert into wishlist (user_id, book_id)
 	values((select user_id from user where first_name = 'Alistair'),(select book_id from book where book_name = 'Aveline, Knight of Orlais'));

insert into wishlist (user_id, book_id)
 	values((select user_id from user where first_name = 'Varric'),(select book_id from book where book_name = 'The Holy Brazier'));

insert into wishlist (user_id, book_id)
 	values((select user_id from user where first_name = 'Dorian'),(select book_id from book where book_name = 'The Tale of Iloren'));

-- add foreign keys to Wishlist --
ALTER TABLE Wishlist
   ADD FOREIGN KEY (user_id) REFERENCES User(user_id);

ALTER TABLE Wishlist
   ADD FOREIGN KEY (book_id) REFERENCES Book(book_id);