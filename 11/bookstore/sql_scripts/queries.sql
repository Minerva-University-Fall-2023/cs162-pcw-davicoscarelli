-- 1. Books low in inventory
SELECT Title FROM Books WHERE InventoryCount < 5;

-- 2. Total spending per customer
SELECT Customers.Name, SUM(Books.Price * OrderDetails.Quantity)
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
JOIN Books ON OrderDetails.BookID = Books.BookID
GROUP BY Customers.CustomerID;

-- 3. Books ordered by a specific customer (CustomerID = 1)
SELECT Books.Title
FROM Books
JOIN OrderDetails ON Books.BookID = OrderDetails.BookID
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
WHERE Orders.CustomerID = 1;
