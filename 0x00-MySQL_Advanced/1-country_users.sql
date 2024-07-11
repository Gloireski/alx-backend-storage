/* create table users with

id: int, not null, auto inc pk
email: string 255, not null, unique
name: string 255,
country: enum US CO TN, not null, default US
*/
-- create users(id, email, name, country)
CREATE TABLE IF NOT EXISTS users
(
	id INT NOT NULL UNIQUE  AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US','CO','TN') DEFAULT 'US'
);
