-- 1. Classes with available spots
SELECT ClassName, Capacity - COUNT(Bookings.BookingID) AS AvailableSpots
FROM Classes
LEFT JOIN Bookings ON Classes.ClassID = Bookings.ClassID
GROUP BY Classes.ClassID
HAVING AvailableSpots > 0;

-- 2. Users who attended a specific class (ClassID = 1) on a particular date ('2023-10-10')
SELECT Users.Name
FROM Attendance
JOIN Users ON Attendance.UserID = Users.UserID
WHERE Attendance.ClassID = 1 AND Attendance.AttendanceDate = '2023-10-10';

-- 3. Attendance rate of a user (UserID = 1)
SELECT (CAST(COUNT(Attendance.AttendanceID) AS REAL) / (SELECT COUNT(*) FROM Classes)) * 100 AS AttendanceRate
FROM Attendance
WHERE Attendance.UserID = 1;
