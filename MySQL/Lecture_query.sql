-- query is a set of instructions written in SQL
-- 4 basic commands
-- SQL convention is that SQL commands are in all caps
-- all queries MUST end in a semi colon
-- This is how you comment, using --


-- CRUD: Create, Read, Update, Delete


-- Create
-- SQL command is: INSERT
-- This command adds data to the database
-- INSERT INTO <name of table> (<fieldname1>, <fieldname2>) VALUES (<fieldname1>, <fieldname2>);
-- id field is auto generated for us, assuming we checked off auto incremented
-- MUST provide data for created_at and updated_at. You can use NOW() function works fine.alter

INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ("Iskander", "Rangel", "icerangel@outlook.com", NOW(), NOW());


-- READ
-- SQL command is: SELECT
-- SELECT <what field to grab> FROM <table name>

SELECT * FROM users; -- Star or wild character. It means to grab all fields.

SELECT first_name, last_name from users; -- When this runs it would show only first and last name.

-- WHERE command to get data based on a condition.
SELECT * FROM users WHERE first_name LIKE "I%" AND  id > 2; -- We are looking for only first names that start with a Capital I
															-- AND if the id is greater than 2
SELECT * FROM users WHERE id = 3; -- Will show the information in the users where the id is 3


-- ORDER BY
-- default order is ascending, we can use DESC to start with the great values
SELECT * FROM users ORDER BY first_name; -- This would start at A - z
SELECT * FROM users ORDER BY first_name DESC; -- This would start at the end of the alphabet Z - A

-- We can combine multiple commands together
SELECT * FROM users
WHERE id > 2
ORDER BY last_name; -- We put the semi colon at the end of the commands

-- UPDATE
-- SQL command is: UPDATE
-- UPDATE <table name> SET <fieldname> = <fieldvaule>, <fieldname> = <fieldvalue> WHERE <field> = <vaule>;
SELECt * FROM users;
UPDATE users SET email = "new_email@dojo.com", updated_at = NOW() WHERE id = 2;

SELECT * FROM orders;
UPDATE orders SET amount = 999.99, updated_at = NOW() WHERE id = 1;


-- DELETE	
-- SQL command is: DELETE
-- DELETE FROM <tablename> WHERE id = <value>;
DELETE FROM orders; -- This would delete ALL ORDERS, careful we don't want that.
-- We need to set an action in our ERD, either SET NULL, CASCADE.
-- Proper DELETE vvvvvvvvvvvvvvvv
DELETE FROM orders WHERE id = 3;


-- FUNCTIONS 
-- NOW()
-- Don't need to memorize functions, we can always look them up.
-- AS command allows us to rename fields to something else.

SELECT CONCAT(first_name, " ", last_name) AS full_name FROM users; 
-- We are merging first_name and last_name with a space " ", AS changes the title from CONCAT to full_name
SELECT LOWER(first_name) FROM users; -- This shows the first names in lower case.