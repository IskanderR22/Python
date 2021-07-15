SELECT * FROM dojo_ninjas_schema.dojos;
SET SQL_SAFE_UPDATES = 0; -- ICE insert this and run it once
INSERT INTO dojos (name) 
VALUES ("Coding Dojo"),
("Cobra Kai Dojo"),
("Ice cream Dojo");
SELECT * FROM dojos;

DELETE FROM dojos;
SELECT * FROM dojos;

INSERT INTO dojos (name) 
VALUES ("Coding Dojo"),
("Cobra Kai Dojo"),
("Ice cream Dojo");
SELECT * FROM dojos;

INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (4,  "Ice", "Rangel", 26),
(4, "Chris", "Engel", 28),
(4, "Rashad", "Naime", 23);
SELECT * FROM ninjas;
SELECT * FROM ninjas WHERE dojo_id = 4;

INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (5,  "2ndIce", "Rangel", 26),
(5, "2ndChris", "Engel", 28),
(5, "2ndRashad", "Naime", 23);
SELECT * FROM ninjas;
SELECT * FROM ninjas WHERE dojo_id = 5;

INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (6,  "3rdIce", "Rangel", 26),
(6, "3rdChris", "Engel", 28),
(6, "3rdRashad", "Naime", 23);
SELECT * FROM ninjas;
SELECT * FROM ninjas WHERE dojo_id = 6;


SELECT * FROM ninjas WHERE dojo_id = 4; -- This is the ninjas in the first Dojo
SELECT * FROM ninjas WHERE dojo_id = 6; -- This is the ninjas in the third Dojo

SELECT name FROM dojos WHERE id = 6;
SELECT dojos.* FROM ninjas JOIN dojos ON dojo_id = dojos.id ORDER BY ninjas.id DESC limit 1;   	-- JOIN method!

