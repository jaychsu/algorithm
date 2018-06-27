SQL (Structured Query Language)
======

**SQL** is used to access and manipulate a **database**.

**MySQL** is a program that understands **SQL**.

SQL can:

- insert, update, or delete records in a database.
- create new databases, table, stored procedures, views.
- retrieve data from a database, etc.

SQL is an ANSI (American National Standards Institute) standard, but there are different versions of the SQL language.

Most SQL database programs have their own proprietary extensions in addition to the SQL standard, but all of them support the major commands.

## Concept

A **database** is a collection of data that is organized in a manner that facilitates ease of access, as well as efficient management and updating.

A database is made up of **tables** that store relevant information.

A table stores and displays data in a structured format consisting of **columns** and **rows** that are similar to those seen in Excel spreadsheets.

### Primary Key

A primary key is a field in the table that uniquely identifies the table records.

The primary key's main features:

- It must contain a **unique value** for each row.
- It cannot contain `NULL` values.

Note that,

- Tables are limited to **ONE** primary key each.
- The primary key's value must be different for each row.

## Syntax

### Logical Operators

Note that, to compare with a text value, you need to surround the text that appears in the statement with **single quotation marks (')**.

| Operators         | Notes                                                        |
| ----------------- | ------------------------------------------------------------ |
| `=`               | Equal                                                        |
| `!=`              | Not equal                                                    |
| `>`               | Greater than                                                 |
| `<`               | Less than                                                    |
| `>=`              | Greater than or equal                                        |
| `<=`              | Less than or equal                                           |
| `BETWEEN a AND b` | Between an inclusive range, that is, `a <= x <= b`           |
| `AND`             | True if **both** expressions are True                        |
| `OR`              | True if **either** expressions is True                       |
| `a IN (b, c, d)`  | True if the operand is equal to one of a list of expressions |
| `NOT`             | Returns True if expression is not True                       |
| `a LIKE pattern`  | SQL **pattern** matching enables you to use `_` to match any single character and `%` to match an arbitrary number of characters (including zero characters). |

### Arithmetic Operators

| Operators | Notes          |
| --------- | -------------- |
| `+`       | addition       |
| `-`       | subtraction    |
| `*`       | multiplication |
| `/`       | division       |

### Data Types

| Type           | Category      | Notes                                                        |
| -------------- | ------------- | ------------------------------------------------------------ |
| `int`          | Numeric       | A normal-sized integer that can be signed or unsigned.       |
| `float(n, d)`  | Numeric       | A floating-point number that cannot be unsigned. You can optionally define the display length (`n`) and the number of decimals (`d`). |
| `double(n, d)` | Numeric       | A double precision floating-point number that cannot be unsigned. You can optionally define the display length (`n`) and the number of decimals (`d`). |
| `date`         | Date and Time | A date in `YYYY-MM-DD` format.                               |
| `datetime`     | Date and Time | A date and time combination in `YYYY-MM-DD HH:MM:SS` format. |
| `time`         | Date and Time | A time in `HH:MM:SS` format.                                 |
| `timestamp`    | Date and Time | A timestamp, calculated from midnight, January 1, 1970.      |
| `char(n)`      | String        | Fixed-length (`n`) character string. Size is specified in parenthesis. Max 255 bytes. |
| `varchar(n)`   | String        | Variable-length(`n`)character string. Max size is specified in parenthesis. |
| `blob`         | String        | **Binary Large Objects** and are used to store large amounts of binary data, such as images or other types of files. |
| `text`         | String        | Large amount of text data.                                   |

### Multiple Queries

SQL allows to run multiple queries or commands at the same time.

Remember to end each SQL statement with a **semicolon** to indicate that the statement is complete and ready to be interpreted.

In this tutorial, we will use **semicolon** at the end of each SQL statement.

```sql
SELECT FirstName FROM customers;
SELECT City FROM customers;
```

### Case Sensitivity

SQL is case **insensitive**.

It is common practice to write all SQL commands in **upper-case**.

### Separator

A single SQL statement can be placed on one or more text lines. In addition, multiple SQL statements can be combined on a single text line.

White spaces and multiple lines are ignored in SQL. However, it is recommended to avoid unnecessary white spaces and lines.

Combined with proper spacing and indenting, breaking up the commands into logical lines will make your SQL statements much easier to read and maintain.

## Command

### Database

| Commands         | Notes                                     |
| ---------------- | ----------------------------------------- |
| `SHOW DATABASES` | list the databases managed by the server. |

### Table

#### SQL constraints

- `NOT NULL` - Indicates that a column cannot contain any NULL value.
- `UNIQUE` - Does not allow to insert a duplicate value in a column. The `UNIQUE` constraint maintains the uniqueness of a column in a table. More than one `UNIQUE` column can be used in a table.
- `AUTO_INCREMENT` - Auto-increment allows a unique number to be generated when a new record is inserted into a table. By default, the starting value for `AUTO_INCREMENT` is 1, and it will increment by 1 for each new record.
- `PRIMARY KEY` - Enforces the table to accept unique data for a specific column and this constraint create a unique index for accessing the table faster.
- `CHECK` - Determines whether the value is valid or not from a logical expression.
- `DEFAULT` - While inserting data into a table, if no value is supplied to a column, then the column gets the value set as `DEFAULT`.

#### Views

In SQL, a VIEW is a **virtual table** that is based on the result-set of an SQL statement.

A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

A view always shows up-to-date data! The database engine uses the view's SQL statement to recreate the data each time a user queries a view.

Views allow us to:

- Structure data in a way that users or classes of users find natural or intuitive.
- Restrict access to the data in such a way that a user can see and (sometimes) modify exactly what they need and no more.
- Summarize data from various tables and use it to generate reports.

| Commands                                                     | Notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `SHOW TABLES`                                                | display all of the tables in the currently selected MySQL database. |
| `CREATE TABLE Users ( UserID int NOT NULL AUTO_INCREMENT, FirstName varchar(40) NOT NULL, LastName varchar(40) NOT NULL, PRIMARY KEY(UserID) )` | Note the **parentheses** in the syntax. When inserting a new record into the Users table, it's not necessary to specify a value for the `UserID` column; a unique new value will be added automatically. |
| `DROP TABLE table`                                           | delete the entire table                                      |
| `RENAME TABLE table TO new_name`                             | rename the entire table                                      |
| `CREATE VIEW view AS (SELECT col FROM table WHERE condition)` | The `SELECT` query can be as complex as you need it to be. It can contain multiple JOINS and other commands. |
| `CREATE OR REPLACE VIEW view AS (subquery)`                  | update a view                                                |
| `DROP VIEW view`                                             | delete a view                                                |

### Column

| Commands                                        | Notes                                                        |
| ----------------------------------------------- | ------------------------------------------------------------ |
| `SHOW COLUMNS FROM table`                       | display information about the columns in a given table.      |
| `SELECT col AS col2 FROM table`                 | assign a custom name to the resulting column using the `AS` keyword. |
| `ALTER TABLE table ADD new_col int`             | add columns in an existing table. All rows will have the default value in the newly added column, which, in this case, is `NULL`. |
| `ALTER TABLE table DROP COLUMN col`             | delete the column named col in the table. The column, along with all of its data, will be completely removed from the table. |
| `ALTER TABLE table CHANGE col new_name type(n)` | rename the column called col to new_name                     |

### Basic Query

| Commands                                                     | Notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `SELECT col FROM table`                                      | select data from a given table.                              |
| `SELECT col1, col2 FROM table`                               | select data from a given table. Do not put a comma after the **last** column name. |
| `SELECT table.col FROM table`                                | you can provide the table name prior to the column name, by separating them with a **dot**. The term for the above-mentioned syntax is called the **fully qualified name** of that column. This form of writing is especially useful when working with multiple tables that may share the same column names. |
| `SELECT * FROM table`                                        | retrieve all of the information contained in your table, place an **asterisk (\*)** sign after the `SELECT` command, rather than typing in each column names separately. |
| `SELECT col FROM table WHERE col > (SELECT AVG(col) FROM table)` | A single subquery will return the same result more easily.   |

### WHERE

| Commands                              | Notes                                                        |
| ------------------------------------- | ------------------------------------------------------------ |
| `SELECT * FROM table WHERE condition` | extract only those records that fulfill a specified criterion. |

### DISTINCT and LIMIT

| Commands                                        | Notes                                                        |
| ----------------------------------------------- | ------------------------------------------------------------ |
| `SELECT DISTINCT col1, col2 FROM table`         | conjunction with `SELECT` to eliminate all duplicate records and return only unique ones |
| `SELECT col1, col2 FROM table LIMIT cnt`        | retrieve the first `cnt` records from the table              |
| `SELECT col1, col2 FROM table LIMIT start, cnt` | pick up `cnt` records, starting from the `start` position. the position is **zero-based** counting, so the position 3 == the fourth record. |

### ORDER BY

| Commands                                  | Notes                                                        |
| ----------------------------------------- | ------------------------------------------------------------ |
| `SELECT * FROM table ORDER BY col1, col2` | **sort** the returned data. By default, the ORDER BY keyword sorts the results in **ascending** order. |
| `SELECT * FROM table ORDER BY col1 DESC`  | The `DESC` keyword sorts results in **descending** order. Similarly, `ASC` sorts the results in **ascending** order. |

### JOIN

| Commands                                                     | Notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `SELECT tb1.a, tb2.a FROM tb1, tb2 WHERE tb1.a = tb2.a`      | Specify multiple table names in the FROM by comma-separating them. |
| `SELECT tb1.col1, tb2.col1 FROM tb1 INNER JOIN tb2 ON tb1.col1 = tb2.col1` | `INNER JOIN` is equivalent to `JOIN`. It returns rows when there is a match between the tables. Note the `ON` keyword for specifying the inner join condition. |
| `SELECT customers.Name, items.Name FROM customers LEFT OUTER JOIN items ON customers.ID = items.Seller_id` | The `OUTER` keyword is optional, and can be omitted. The `LEFT JOIN` returns all rows from the left table, even if there are no matches in the right table. This means that if there are no matches for the `ON` clause in the table on the right, the join will still return the rows from the first table in the result. If no match is found for a particular row, `NULL` is returned. |
| `SELECT col1 FROM tb1 UNION SELECT col2 FROM tb2`            | `UNION` combines multiple datasets into a single dataset, and removes any existing duplicates. `UNION ALL` combines multiple datasets into one dataset, but does not remove duplicate rows. `UNION ALL` is faster than `UNION`, as it does not perform the duplicate removal operation over the data set.<br>The `UNION` operator is used to combine the result-sets of two or more `SELECT` statements. All `SELECT` statements within the `UNION` must have the **same number of columns**. The columns must also have the same **data types**. Also, the columns in each `SELECT` statement must be **in the same order**.<br>If your columns don't match exactly across all queries, you can use a NULL (or any other) value. |

### INSERT/UPDATE/DELETE

| Commands                                                    | Notes                                                        |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| `INSERT INTO table VALUES (val1, val2, ...)`                | add **new rows** of data to a table in the database. Make sure the order of the values is in the same order as the columns in the table. When inserting records into a table using the SQL `INSERT` statement, you must provide a value for every column that does not have a default value, or does not support `NULL`. |
| `INSERT INTO table (col2, col1) VALUES (val2, val1)`        | You can specify your own column order, as long as the values are specified in the same order as the columns. The **missing** column for that row automatically became its default value. |
| `UPDATE table SET col1 = val1, col2 = val2 WHERE condition` | allows us to alter data in the table. You specify the column and its new value in a comma-separated list after the `SET` keyword. If you omit the `WHERE` clause, **ALL records** in the table will be updated! |
| `DELETE FROM table WHERE condition`                         | remove data from your table. If you omit the `WHERE` clause, **ALL records** in the table will be deleted! The `DELETE` statement removes the data from the table permanently. |

### Functions

| Commands                                                     | Notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `SELECT CONCAT(a, ',', b) FROM table`                        | concatenate two or more text values and returns the concatenating string. |
| `SELECT FirstName, UPPER(LastName) AS LastName FROM employees` | The `UPPER` function converts all letters in the specified string to uppercase. The `LOWER` function converts the string to lowercase. If there are characters in the string that are not letters, this function will have no effect on them. |
| `SELECT Salary, SQRT(Salary) FROM employees`                 | calculate the square root of each Salary                     |
| `SELECT AVG(Salary) FROM employees`                          | returns the average value of a numeric column                |
| `SELECT SUM(Salary) FROM employees`                          | get the sum of all of the salaries in the employees table    |
| `SELECT MIN(Salary) AS Salary FROM employees`                | return the minimum value of an expression                    |
