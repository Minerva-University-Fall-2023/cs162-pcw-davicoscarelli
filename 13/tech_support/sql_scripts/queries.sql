-- How many tickets are currently open?
SELECT COUNT(*) 
FROM Tickets 
WHERE status = 'Open';

-- Which products have the most tickets raised against them?
SELECT p.name, COUNT(t.ticket_id) AS ticket_count 
FROM Products p
JOIN Tickets t ON p.product_id = t.product_id
GROUP BY p.product_id
ORDER BY ticket_count DESC
LIMIT 1;

-- What was the last response to a specific ticket?
SELECT r.response_text 
FROM Responses r
WHERE r.ticket_id = 1
ORDER BY r.date DESC
LIMIT 1;
