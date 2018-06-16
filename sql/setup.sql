CREATE DATABASE travel_agency
go


/* ENTITIES */

CREATE TABLE user (
       email VARCHAR(35) NOT NULL,
       username VARCHAR(40),
       password VARCHAR(20) NOT NULL,
       PRIMARY KEY (email)
       );

CREATE TABLE review (
       id INT NOT NULL AUTO_INCREMENT,
       numStars INT NOT NULL,
       detailedReview VARCHAR(1000),
       submissionDate DATETIME NOT NULL,
       author VARCHAR(35) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (author) REFERENCES user(email),
       CHECK (numStars >= 1 AND numStars <= 5)
       );

CREATE TABLE location (
       id INT NOT NULL AUTO_INCREMENT,
       city VARCHAR(30) NOT NULL,
       region VARCHAR(2) NOT NULL,
       country VARCHAR(2) NOT NULL DEFAULT 'US',
       PRIMARY KEY (id),
       UNIQUE (city, region, country)
       );

CREATE TABLE booking (
       id INT NOT NULL AUTO_INCREMENT,
       startDate DATE NOT NULL,
       PRIMARY KEY (id)
       );       

CREATE TABLE transportation (
       id INT NOT NULL,
       departureTime TIME NOT NULL,
       sourceLocation INT NOT NULL,
       destinationLocation INT NOT NULL,
       fareEconomy DECIMAL(6,2) NOT NULL,
       fareBusiness DECIMAL(6,2) NOT NULL,
       fareFirst DECIMAL(6,2) NOT NULL,
       numSeatsRemainingEconomy INT NOT NULL,
       numSeatsRemainingBusiness INT NOT NULL,
       numSeatsRemainingFirst INT NOT NULL,
       FOREIGN KEY (id) REFERENCES booking(id),
       FOREIGN KEY (sourceLocation) REFERENCES location(id),
       FOREIGN KEY (destinationLocation) REFERENCES location(id),
       CHECK (fare > 0)
       );

CREATE TABLE flight (
       id INT NOT NULL,
       airline VARCHAR(30) NOT NULL,
       FOREIGN KEY (id) REFERENCES transportation(id)
       );

CREATE TABLE train (
       id INT NOT NULL,
       railroad VARCHAR(30),
       FOREIGN KEY (id) REFERENCES transportation(id)
       );

CREATE TABLE hotel (
       id INT NOT NULL,
       endDate DATE NOT NULL,
       dailyCost DECIMAL(6,2) NOT NULL,
       address VARCHAR(30),
       location INT NOT NULL,
       FOREIGN KEY (id) REFERENCES booking(id),
       FOREIGN KEY (location) REFERENCES location(id),
       CHECK (dailyCost > 0)
       );

CREATE TABLE payment (
       id INT NOT NULL AUTO_INCREMENT,
       amount DECIMAL(6,2) NOT NULL,
       paymentType ENUM('debit', 'credit'),
       cardNo VARCHAR(16) NOT NULL,
       PRIMARY KEY (id),
       CHECK (amount > 0)
       );

CREATE TABLE attraction (
       id INT NOT NULL AUTO_INCREMENT,
       location INT NOT NULL,
       name VARCHAR(30) NOT NULL,
       description VARCHAR(1000),
       image VARCHAR(200) NOT NULL DEFAULT 'tmp.jpg',
       PRIMARY KEY (id),
       FOREIGN KEY (location) REFERENCES location(id)
       );



/* RELATIONSHIPS */

CREATE TABLE purchase (
       userID VARCHAR(35),
       bookingID INT,
       paymentID INT,
       transactionDate DATETIME,
       PRIMARY KEY (userID, bookingID, paymentID),
       FOREIGN KEY (userID) REFERENCES user(email),
       FOREIGN KEY (bookingID) REFERENCES booking(id),
       FOREIGN KEY (paymentID) REFERENCES payment(id)
       );
