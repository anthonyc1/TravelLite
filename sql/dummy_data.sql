INSERT INTO travellite_location VALUES (1, 'New York City', 'NY', 'NewYorkCity.jpg');
INSERT INTO travellite_location VALUES (2, 'Chicago', 'IL', 'Chicago.jpg');
INSERT INTO travellite_location VALUES (3, 'Los Angeles', 'CA', 'LosAngeles.jpg');
INSERT INTO travellite_location VALUES (4, 'Boston', 'MA', 'Boston.jpg');
INSERT INTO travellite_location VALUES (5, 'Las Vegas', 'NV', 'LasVegas.jpg');
INSERT INTO travellite_location VALUES (6, 'Atlanta', 'GA', 'Atlanta.jpg');


-- 3 flights NY -> LA on 5/29
-- 3 flights NY -> LA on 5/30
-- 5 flights LA -> NY on 6/04
-- 3 flights Atlanta -> Las Vegas on 07/03
-- 2 flights Las Vegas -> Atlanta on 07/11
-- 1 flights NY -> Boston on 09/19
-- 2 flights Boston -> Chicago on 09/22
-- 1 flights Chicago -> NY on 09/27

INSERT INTO travellite_flight VALUES (1, 'Delta Air Lines', 'New York City', 'Los Angeles', '2018-05-29', '09:00:00', 111.00, 238.50, 577.00, 50, 19, 5);
INSERT INTO travellite_flight VALUES (2, 'JetBlue', 'New York City', 'Los Angeles', '2018-05-29', '11:30:00', 109.00, 305.00, 462.50, 47, 22, 10);
INSERT INTO travellite_flight VALUES (3, 'Delta Air Lines', 'New York City', 'Los Angeles', '2018-05-29', '15:30:00', 115.50, 283.00, 501.50, 69, 15, 8);
INSERT INTO travellite_flight VALUES (4, 'Delta Air Lines', 'New York City', 'Los Angeles', '2018-05-30', '10:30:00', 102.00, 287.50, 560.00, 66, 20, 3);
INSERT INTO travellite_flight VALUES (5, 'JetBlue', 'New York City', 'Los Angeles', '2018-05-30', '12:45:00', 99.00, 254.50, 490.00, 62, 12, 9);
INSERT INTO travellite_flight VALUES (6, 'Delta Air Lines', 'New York City', 'Los Angeles', '2018-05-30', '17:00:00', 103.50, 273.00, 522.00, 50, 18, 11);
INSERT INTO travellite_flight VALUES (7, 'American Airlines', 'Los Angeles', 'New York City', '2018-06-04', '05:30:00', 140.00, 302.00, 630.00, 10, 0, 1);
INSERT INTO travellite_flight VALUES (8, 'American Airlines', 'Los Angeles', 'New York City', '2018-06-04', '10:00:00', 137.00, 300.00, 623.00, 5, 2, 0);
--book the one below?
INSERT INTO travellite_flight VALUES (9, 'Delta Air Lines', 'Los Angeles', 'New York City', '2018-06-04', '12:45:00', 122.00, 297.00, 580.00, 1, 0, 0);
INSERT INTO travellite_flight VALUES (10, 'Delta Air Lines', 'Los Angeles', 'New York City', '2018-06-04', '14:30:00', 129.50, 296.50, 620.00, 18, 7, 6);
INSERT INTO travellite_flight VALUES (11, 'JetBlue', 'Los Angeles', 'New York City', '2018-06-04', '16:45:00', 148.00, 312.50, 640.50, 10, 4, 4);
INSERT INTO travellite_flight VALUES (12, 'JetBlue', 'Atlanta', 'Las Vegas', '2018-07-03', '12:30:00', 99.00, 205.00, 392.50, 67, 21, 10);
INSERT INTO travellite_flight VALUES (13, 'American Airlines', 'Atlanta', 'Las Vegas', '2018-07-03', '19:30:00', 105.50, 203.00, 410.00, 69, 16, 4);
INSERT INTO travellite_flight VALUES (14, 'Delta Air Lines', 'Atlanta', 'Las Vegas', '2018-07-03', '22:30:00', 94.00, 187.50, 460.00, 58, 20, 12);
INSERT INTO travellite_flight VALUES (15, 'JetBlue', 'Las Vegas', 'Atlanta', '2018-07-11', '12:15:00', 90.00, 154.00, 410.50, 72, 16, 9);
INSERT INTO travellite_flight VALUES (16, 'Delta Air Lines', 'Las Vegas', 'Atlanta', '2018-07-11', '16:00:00', 93.50, 172.00, 422.00, 61, 18, 14);
INSERT INTO travellite_flight VALUES (17, 'American Airlines', 'New York City', 'Boston', '2018-09-19', '12:30:00', 95.50, 203.00, 422.00, 79, 16, 4);
INSERT INTO travellite_flight VALUES (18, 'Delta Air Lines', 'Boston', 'Chicago', '2018-09-22', '12:30:00', 94.00, 187.50, 436.00, 78, 10, 12);
INSERT INTO travellite_flight VALUES (19, 'JetBlue', 'Boston', 'Chicago', '2018-09-22', '23:15:00', 93.00, 154.00, 410.50, 72, 16, 3);
INSERT INTO travellite_flight VALUES (20, 'Delta Air Lines', 'Chicago', 'New York City', '2018-09-27', '16:30:00', 93.50, 172.00, 422.00, 69, 19, 14);


-- 4 trains NY -> Boston on 06/04
-- 2 trains NY -> Boston on 06/05
-- 3 trains Boston -> NY on 06/14
-- 3 trains LA -> Las Vegas on 08/03
-- 5 trains Las Vegas -> LA on 08/10

INSERT INTO travellite_train VALUES (1, 'Amtrak', 'New York City', 'Boston', '2018-06-04', '07:30:00', 88.50, 103.00, 202.00, 240, 112, 45);
INSERT INTO travellite_train VALUES (2, 'Amtrak', 'New York City', 'Boston', '2018-06-04', '12:30:00', 101.00, 118.50, 213.00, 312, 162, 53);
INSERT INTO travellite_train VALUES (3, 'Norfolk Southern', 'New York City', 'Boston', '2018-06-04', '15:30:00', 54.00, 100.50, 183.00, 412, 62, 20);
INSERT INTO travellite_train VALUES (4, 'Amtrak', 'New York City', 'Boston', '2018-06-04', '19:45:00', 93.50, 103.50, 200.00, 0, 6, 10);
INSERT INTO travellite_train VALUES (5, 'Amtrak', 'New York City', 'Boston', '2018-06-05', '09:45:00', 87.50, 105.50, 190.00, 40, 6, 10);
INSERT INTO travellite_train VALUES (6, 'Norfolk Southern', 'New York City', 'Boston', '2018-06-05', '11:30:00', 64.00, 90.50, 176.00, 412, 62, 20);
INSERT INTO travellite_train VALUES (7, 'Amtrak', 'Boston', 'New York City', '2018-06-14', '10:30:00', 103.00, 128.00, 210.00, 299, 78, 52);
INSERT INTO travellite_train VALUES (8, 'Norfolk Southern', 'Boston', 'New York City', '2018-06-14', '14:30:00', 85.00, 128.00, 203.50, 232, 42, 36);
INSERT INTO travellite_train VALUES (9, 'Amtrak', 'Boston', 'New York City', '2018-06-14', '16:45:00', 110.00, 132.00, 213.00, 287, 62, 59);
INSERT INTO travellite_train VALUES (10, 'Union Pacific', 'Los Angeles', 'Las Vegas', '2018-08-03', '08:45:00', 74.00, 100.50, 193.00, 412, 62, 21);
INSERT INTO travellite_train VALUES (11, 'Virgin Trains', 'Los Angeles', 'Las Vegas', '2018-08-03', '09:30:00', 54.00, 105.00, 183.00, 400, 72, 13);
INSERT INTO travellite_train VALUES (12, 'Union Pacific', 'Los Angeles', 'Las Vegas', '2018-08-03', '12:45:00', 83.00, 113.00, 203.00, 382, 59, 20);
INSERT INTO travellite_train VALUES (13, 'Union Pacific', 'Las Vegas', 'Los Angeles', '2018-08-10', '09:00:00', 78.00, 109.50, 188.00, 388, 60, 19);
INSERT INTO travellite_train VALUES (14, 'Virgin Trains', 'Las Vegas', 'Los Angeles', '2018-08-10', '12:45:00', 61.00, 99.50, 163.00, 409, 80, 17);
INSERT INTO travellite_train VALUES (15, 'Union Pacific', 'Las Vegas', 'Los Angeles', '2018-08-10', '15:00:00', 80.00, 100.00, 179.00, 394, 59, 30);
INSERT INTO travellite_train VALUES (14, 'Virgin Trains', 'Las Vegas', 'Los Angeles', '2018-08-10', '16:45:00', 73.00, 96.00, 163.00, 419, 80, 18);
INSERT INTO travellite_train VALUES (15, 'Union Pacific', 'Las Vegas', 'Los Angeles', '2018-08-10', '20:00:00', 79.00, 108.00, 176.00, 382, 78, 22);


-- 3 hotels in NYC
-- 4 hotels in Boston
-- 3 hotels in LA

INSERT INTO travellite_hotel VALUES (1, 254.99, 'West 46th St. & Broadway', 'New York City', 'NY Marriott Marquis');
INSERT INTO travellite_hotel VALUES (2, 202.00, 'East 94th St. & 2nd Ave.', 'New York City', 'Marmara Manhattan Hotel');
INSERT INTO travellite_hotel VALUES (3, 239.99, 'Gansevoort St. & 9th Ave.', 'New York City', 'Hotel Gansevoort');
INSERT INTO travellite_hotel VALUES (4, 150.00, '500 Commonwealth Ave.', 'Boston', 'Hotel Commonwealth');
INSERT INTO travellite_hotel VALUES (5, 138.99, '107 Merrimac St.', 'Boston', 'The Boxer');
INSERT INTO travellite_hotel VALUES (6, 95.99, '50 Park Plaza', 'Boston', 'Boston Park Plaza');
INSERT INTO travellite_hotel VALUES (7, 216.00, '510 Atlantic Ave.', 'Boston', 'InterContinental Boston');
INSERT INTO travellite_hotel VALUES (8, 101.00, 'West 8th St. & South Olive St.', 'Los Angeles', 'Freehand Los Angeles');
INSERT INTO travellite_hotel VALUES (9, 192.99, '7th St. & South Olive St.', 'Los Angeles', 'The Los Angeles Athletic Club');
INSERT INTO travellite_hotel VALUES (10, 136.00, '6th St. & South Westlake Ave.', 'Los Angeles', 'Holiday Inn Express & Suites Los Angeles');


-- 3 attractions in NYC
-- 3 attractions in Chicago

INSERT INTO travellite_attraction VALUES (1, 'New York City', 'Empire State Building', 'Located in the center of Midtown Manhattan, its 86th and 102nd floor observatories provide unforgettable 360-degree views of New York City and beyond. Whether you’re in town for a week or a day, no visit to NYC is complete without experiencing the top of the Empire State Building.', 'NewYorkCity1.jpg');
INSERT INTO travellite_attraction VALUES (2, 'New York City', 'World Trade Center', 'Bigger.  Bolder.  Better than ever.  The revitalized World Trade Center is Manhattan’s new center of gravity - a vision of tomorrow, realized today.', 'NewYorkCity2.jpg');
INSERT INTO travellite_attraction VALUES (3, 'New York City', 'Central Park', 'Set in the middle of bustling Manhattan, Central Park’s grounds serve as a safe haven, not only for athletes, daydreamers, musicians, and strollers, but also for teems of migratory birds each year.', 'NewYorkCity3.jpg');
INSERT INTO travellite_attraction VALUES (4, 'Chicago', 'Willis Tower', 'Standing tall above every other skyscraper in Chicago, Willis Tower (formerly known as the Sears Tower) is a 110-story building in the heart of downtown. One of the tallest buildings in the world and the tallest building in America, it is impossible to miss when appreciating the skyline.', 'Chicago1.jpg');
INSERT INTO travellite_attraction VALUES (5, 'Chicago', 'John Hancock Center', 'Known locally as ’Big John’, the John Hancock Center is one of the Chicagoans’ favorite skyscrapers. The observation deck at the top of the John Hancock Center - known as 360 Chicago - offers one of the best views you can have of the Loop, Chicago’s downtown area.', 'Chicago2.jpg');
INSERT INTO travellite_attraction VALUES (6, 'Chicago', 'Millenium Park', 'Discover a state-of-the-art collection of architecture, landscape design and art that provide the backdrop for hundreds of programs such as concerts, exhibitions, and family activities.  Located in the heart of the city, it is a destination for Chicagoans and visitors alike.', 'Chicago3.jpg');
INSERT INTO travellite_attraction VALUES (7, 'Los Angeles', 'Wilshire Grand Center', 'todo', 'LosAngeles1.jpg');
INSERT INTO travellite_attraction VALUES (8, 'Los Angeles', 'Rose Bowl', 'todo', 'LosAngeles2.jpg');
INSERT INTO travellite_attraction VALUES (9, 'Los Angeles', 'Staples Center', 'todo', 'LosAngeles3.jpg');
INSERT INTO travellite_attraction VALUES (10, 'Boston', 'Massachusetts State House', 'todo', 'Boston1.jpg');
INSERT INTO travellite_attraction VALUES (11, 'Boston', 'Harvard University', 'todo', 'Boston2.jpg');
INSERT INTO travellite_attraction VALUES (12, 'Boston', 'Faneiul Hall', 'todo', 'Boston3.jpg');
INSERT INTO travellite_attraction VALUES (13, 'Las Vegas', 'Caesars Palace', 'todo', 'LasVegas1.jpg');
INSERT INTO travellite_attraction VALUES (14, 'Las Vegas', 'High Roller', 'todo', 'LasVegas2.jpg');
INSERT INTO travellite_attraction VALUES (15, 'Las Vegas', 'MGM Grand', 'todo', 'LasVegas3.jpg');
INSERT INTO travellite_attraction VALUES (16, 'Atlanta', 'World of Coca Cola', 'todo', 'Atlanta1.jpg');
INSERT INTO travellite_attraction VALUES (17, 'Atlanta', 'CNN Center', 'todo', 'Atlanta2.jpg');
INSERT INTO travellite_attraction VALUES (18, 'Atlanta', 'Olympic Park', 'todo', 'Atlanta3.jpg');
