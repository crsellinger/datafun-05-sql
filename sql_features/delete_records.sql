-- Deletes rows from books where authors.last is Tolkien
DELETE FROM books
WHERE author_id IN
-- Sub-query to selects author_id from authors where last is Tolkien
(SELECT authors.author_id
FROM authors
-- Joins books and authors tables where author_id matches
INNER JOIN books ON authors.author_id = books.author_id
WHERE last = 'Tolkien')