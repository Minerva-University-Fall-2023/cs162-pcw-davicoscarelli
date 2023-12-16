-- Transaction for Student Enrollment
-- To ensure that the creation of a student record and their enrollment in a course are fully synchronized. This guarantees that either both actions occur, or neither does, preventing any inconsistencies in student enrollment data.
BEGIN TRANSACTION;

INSERT INTO Students (name, email) VALUES ('Alice Brown', 'alice@example.com');
INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES ((SELECT id FROM Students WHERE email = 'alice@example.com'), 1, '2023-01-03');

COMMIT;

-- Transaction for Assignment Submission
-- To ensure that the submission of an assignment and any related updates (like changing the due date) are treated as a single operation. This maintains consistency in the assignment and submission records, ensuring that all changes are reflected accurately and simultaneously.

BEGIN TRANSACTION;

INSERT INTO Submissions (assignment_id, student_id, submission_date, grade) VALUES (1, 1, '2023-01-15', NULL);
UPDATE Assignments SET due_date = '2023-02-05' WHERE id = 1;

COMMIT;
