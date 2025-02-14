-- use WHERE to filter data based on conditions.
SELECT title
FROM books
-- Joins books and authors tables where author_id matches
INNER JOIN authors ON authors.author_id = books.author_id
WHERE last = 'Tolkien'