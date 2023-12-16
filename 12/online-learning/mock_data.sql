-- Insert Courses
INSERT INTO Courses (name, description) VALUES ('Mathematics', 'Basic Math Course');
INSERT INTO Courses (name, description) VALUES ('Physics', 'Introduction to Physics');

-- Insert Students
INSERT INTO Students (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO Students (name, email) VALUES ('Jane Smith', 'jane@example.com');

-- Insert Enrollments
INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (1, 1, '2023-01-01');
INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (2, 2, '2023-01-02');

-- Insert Assignments
INSERT INTO Assignments (course_id, title, due_date) VALUES (1, 'Algebra Assignment', '2023-02-01');
INSERT INTO Assignments (course_id, title, due_date) VALUES (2, 'Physics Lab', '2023-02-15');
