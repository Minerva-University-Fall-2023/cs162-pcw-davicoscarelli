-- Which cars are currently available for rent?
SELECT make, model, year 
FROM Cars 
WHERE status = 'Available';

-- Which customers have rented cars in the last month?
SELECT DISTINCT c.name 
FROM Customers c
JOIN Rentals r ON c.customer_id = r.customer_id
WHERE r.start_date BETWEEN date('now', '-1 month') AND date('now');

-- What maintenance activities were performed on a specific car in the last year?
SELECT m.description, m.date 
FROM Maintenance m
WHERE m.car_id = 3 AND m.date BETWEEN date('now', '-1 year') AND date('now');
