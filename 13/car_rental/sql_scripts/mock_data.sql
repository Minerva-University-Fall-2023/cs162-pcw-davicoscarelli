-- Cars
INSERT INTO Cars (make, model, year, status) VALUES 
('Toyota', 'Camry', 2020, 'Available'),
('Honda', 'Civic', 2019, 'Rented'),
('Ford', 'Mustang', 2021, 'Maintenance');

-- Customers
INSERT INTO Customers (name, license_number, email) VALUES 
('John Doe', 'LIC12345', 'john.doe@example.com'),
('Jane Smith', 'LIC67890', 'jane.smith@example.com');

-- Rentals
INSERT INTO Rentals (car_id, customer_id, start_date, end_date) VALUES 
(1, 1, '2023-01-01', '2023-01-10'),
(2, 2, '2023-01-05', '2023-01-15');

-- Maintenance
INSERT INTO Maintenance (car_id, description, date) VALUES 
(3, 'Oil Change', '2023-01-07');
