CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE Accounts (
    account_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    account_name TEXT NOT NULL,
    balance REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    amount REAL NOT NULL,
    transaction_date DATE NOT NULL,
    category TEXT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE Budgets (
    budget_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
