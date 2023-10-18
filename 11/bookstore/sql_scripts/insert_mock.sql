-- Inserting Authors
INSERT INTO Authors (Name) VALUES ('J.K. Rowling');
INSERT INTO Authors (Name) VALUES ('George Orwell');
INSERT INTO Authors (Name) VALUES ('Jane Austen');

-- Inserting Books
INSERT INTO Books (Title, AuthorID, Price, InventoryCount) VALUES ('Harry Potter', 1, 20.00, 10);
INSERT INTO Books (Title, AuthorID, Price, InventoryCount) VALUES ('1984', 2, 15.00, 5);
INSERT INTO Books (Title, AuthorID, Price, InventoryCount) VALUES ('Pride and Prejudice', 3, 12.00, 0);

-- Inserting Customers
INSERT INTO Customers (Name, Email) VALUES ('John Doe', 'john.doe@example.com');
INSERT INTO Customers (Name, Email) VALUES ('Jane Doe', 'jane.doe@example.com');

-- Inserting Orders
INSERT INTO Orders (CustomerID, OrderDate) VALUES (1, '2023-10-10');
INSERT INTO Orders (CustomerID, OrderDate) VALUES (2, '2023-10-09');

-- Inserting OrderDetails
INSERT INTO OrderDetails (OrderID, BookID, Quantity) VALUES (1, 1, 2);
INSERT INTO OrderDetails (OrderID, BookID, Quantity) VALUES (2, 3, 1);
