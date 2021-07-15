SELECT * FROM users_schema.users;

INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ("Chris", "Engel", "chris@dojo.com", NOW(), NOW()),
("Rashad", "Naime", "rashad@dojo.com", NOW(), NOW()),
("Samer", "Yahia", "samer@dojo.com", NOW(), NOW());

SELECT * FROM users;

SELECT * FROM users WHERE email = "chris@dojo.com";
SELECT * FROM users where id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id =3;
SELECT * FROM users;

DELETE FROM users WHERE id = 2;
SELECT * FROM users;

SELECT * FROM users ORDER BY first_name;

SELECT * FROM users ORDER BY first_name DESC;


