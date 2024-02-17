-- Computes the score average of all records in the table
SELECT * FROM second_table
WHERE score (SELECT AVG(score)) FROM second_table;