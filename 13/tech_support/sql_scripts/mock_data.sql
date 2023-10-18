-- Customers
INSERT INTO Customers (name, email) VALUES 
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

-- Products
INSERT INTO Products (name, description) VALUES 
('Laptop', '15-inch screen, 256GB SSD'),
('Mobile Phone', '6-inch screen, 64GB storage');

-- Tickets
INSERT INTO Tickets (customer_id, product_id, issue, status) VALUES 
(1, 1, 'Screen flickering issue', 'Open'),
(2, 2, 'Battery draining quickly', 'In Progress');

-- Responses
INSERT INTO Responses (ticket_id, response_text, date) VALUES 
(1, 'Please ensure your drivers are updated.', '2023-01-10'),
(2, 'Have you tried resetting the phone?', '2023-01-11');
