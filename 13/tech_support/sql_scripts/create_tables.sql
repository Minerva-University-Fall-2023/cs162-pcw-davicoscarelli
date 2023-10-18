CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE Tickets (
    ticket_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    issue TEXT,
    status TEXT -- Open, Closed, In Progress
);

CREATE TABLE Responses (
    response_id INTEGER PRIMARY KEY,
    ticket_id INTEGER,
    response_text TEXT,
    date DATE,
    FOREIGN KEY(ticket_id) REFERENCES Tickets(ticket_id)
);