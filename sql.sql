-- Important commands
SELECT -- Extracts data from a database
UPDATE -- Updates data in a database
DELETE -- Deletes data from a database
INSERT INTO -- Inserts new data into a database
CREATE DATABASE -- Creates a new database
ALTER DATABASE -- Modifies a database
CREATE TABLE -- Creates a new table
ALTER TABLE -- Modifies a table
DROP TABLE -- Deletes a table
CREATE INDEX -- Creates an index (search key)
DROP INDEX -- Deletes an index

-- SELECT: extracts data from a database
-- Select all columns
SELECT * FROM tableName;
-- Select only certain columns
SELECT column1, column2 FROM tableName;
-- Select only one of each unique element
SELECT DISTINCT Country FROM Customers;

-- WHERE: filters results by a condition
SELECT * FROM Customers WHERE Country='USA';
-- Using IN
SELECT * FROM Customers WHERE Country IN ('USA', 'Switzerland');
-- AND, OR, and NOT can also be used
SELECT * FROM Customers WHERE Country='USA' OR Country='UK' AND NOT id>1000;
-- Can also group conditions
SELECT * FROM Customers WHERE Country='Germany' AND (City='Berlin' OR City='Dresden');

-- ORDER BY: determines the result order (ascending by default)
SELECT * FROM tableName ORDER BY column1;
-- To sort by descending order
SELECT * FROM Customers ORDER BY Country DESC;

-- INSERT INTO: add new records to a table
INSERT INTO tableName (column1, column2) VALUES (value1, value2);
-- If adding values to all columns in order, you can shorthand it
INSERT INTO tableName VALUES (value1, value2);

-- UPDATE: allows you to change an existing record
UPDATE Customers SET Name = 'Sam', City= 'Lexington' WHERE CustomerID = 1;

-- DELETE FROM: remove an entire entry from a table
DELETE FROM table_name WHERE condition;
DELETE FROM Sales WHERE Sales is NULL;

-- TOP: allows you to peak the first N entries of a result
SELECT TOP 3 * FROM Customers;
-- Can still use clauses too
SELECT TOP 3 * FROM Customers WHERE Country='USA';

-- MIN() & MAX(): returns minimum or maximum entry
SELECT MIN(columnName) FROM tableName WHERE condition;
SELECT MAX(columnName) FROM tableName WHERE condition;

-- COUNT(), SUM(), AVG(): return single value
SELECT COUNT(columnName) FROM tableName WHERE condition;
SELECT SUM(columnName) FROM tableName WHERE condition;
SELECT AVG(columnName) FROM tableName WHERE condition;

-- LIKE: looks for a pattern match
-- %:  zero, one, or multiple characters
-- _:  single character
-- []: represents any single character within the brackets [abc]
-- ^:  represents any character not in the brackets [^abc]
-- -:  represents a range of characters [a-Z]
SELECT * FROM tableName WHERE column LIKE pattern;
... LIKE 'a%'   -- Finds any values that start with "a"
... LIKE '%a'   -- Finds any values that end with "a"
... LIKE '%or%' -- Finds any values that have "or" in any position
... LIKE '_r%'  -- Finds any values that have "r" in the second position
... LIKE 'a__%' -- Finds any values that start with "a" and are at least 3 characters in length
... LIKE 'a%o'  -- Finds any values that start with "a" and ends with "o"

-- CREATE DATABASE: makes a new database
CREATE DATABASE dbName;

-- CREATE TABLE: adds a new table to a database
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    FOREIGN KEY (Address) REFERENCES Customers(ID)
);
