-- Users
INSERT INTO Users (username, password) VALUES ('john_doe', 'password123');
INSERT INTO Users (username, password) VALUES ('jane_doe', 'password456');

-- Accounts
INSERT INTO Accounts (user_id, account_name, balance) VALUES (1, 'Checking', 5000);
INSERT INTO Accounts (user_id, account_name, balance) VALUES (2, 'Savings', 10000);

-- Transactions
INSERT INTO Transactions (account_id, amount, transaction_date, category) VALUES (1, -100, '2023-10-01', 'Groceries');
INSERT INTO Transactions (account_id, amount, transaction_date, category) VALUES (1, -200, '2023-10-02', 'Utilities');
INSERT INTO Transactions (account_id, amount, transaction_date, category) VALUES (1, 1000, '2023-10-03', 'Salary');

-- Budgets
INSERT INTO Budgets (user_id, category, amount) VALUES (1, 'Groceries', 400);
INSERT INTO Budgets (user_id, category, amount) VALUES (1, 'Utilities', 150);
