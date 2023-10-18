-- Inserting Users
INSERT INTO Users (Name, Email) VALUES ('Alice', 'alice@example.com');
INSERT INTO Users (Name, Email) VALUES ('Bob', 'bob@example.com');

-- Inserting Classes
INSERT INTO Classes (ClassName, Schedule, Capacity) VALUES ('Yoga', 'Monday 10:00', 15);
INSERT INTO Classes (ClassName, Schedule, Capacity) VALUES ('Zumba', 'Wednesday 18:00', 20);

-- Inserting Bookings
INSERT INTO Bookings (UserID, ClassID) VALUES (1, 1);
INSERT INTO Bookings (UserID, ClassID) VALUES (2, 2);

-- Inserting Attendance
INSERT INTO Attendance (UserID, ClassID, AttendanceDate) VALUES (1, 1, '2023-10-10');
INSERT INTO Attendance (UserID, ClassID, AttendanceDate) VALUES (2, 2, '2023-10-09');
