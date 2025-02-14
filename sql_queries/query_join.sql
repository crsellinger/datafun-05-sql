-- use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
SELECT DISTINCT *
FROM books
FULL JOIN authors on authors.author_id = books.author_id
ORDER BY books.year_published