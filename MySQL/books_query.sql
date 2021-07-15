SELECT * FROM books_schema.authors;
SET SQL_SAFE_UPDATES = 0;

INSERT INTO authors (name)
VALUES ("Jane Austen"),
 ("Emily Dickinson"),
 ("Fyodor Dostoevsky"),
 ("William Shakespeare"), 
 ("Lau Tzu");
 SELECT * FROM authors;
 
 INSERT INTO books (title, number_of_pages)
 VALUES ("C Sharp", 50),
("Java", 100),
("Python", 150),
("PHP", 200),
("Ruby", 250);
 SELECT * FROM books;
 UPDATE books SET title = "C#"  WHERE title = "C Sharp";
 
 UPDATE authors SET name = "Bill"  WHERE id = 4;
 SELECT * FROM authors;
 
 INSERT INTO favorites (author_id, book_id)
 VALUES (1, 1),
 (1, 2);
 
INSERT INTO favorites (author_id, book_id)
 VALUES (2, 1),
 (2, 2),
 (2, 3);
 
 
 INSERT INTO favorites (author_id, book_id)
 VALUES (3, 1),
 (3, 2),
 (3, 3),
 (3, 4);
 
 
 INSERT INTO favorites (author_id, book_id)
 VALUES (4, 1),
 (4, 2),
 (4, 3),
 (4, 4),
 (4, 5);
 
 SELECT * FROM favorites;
 
 SELECT author_id FROM favorites WHERE book_id = 3; 
 
 DELETE FROM favorites WHERE author_id = 2 AND book_id = 3;
 
 INSERT INTO favorites (author_id, book_id)
 VALUES (5, 2);
 
 SELECT * FROM favorites WHERE author_id = 3;
 
 SELECT * FROM favorites WHERE book_id = 5;