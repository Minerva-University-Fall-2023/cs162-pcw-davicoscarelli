-- Insert Patients
INSERT INTO Patients (name, dob, gender) VALUES ('Emily Johnson', '1985-07-12', 'Female');
INSERT INTO Patients (name, dob, gender) VALUES ('Michael Brown', '1990-09-23', 'Male');

-- Insert Visits
INSERT INTO Visits (patient_id, date, reason) VALUES (1, '2023-03-01', 'Routine Checkup');
INSERT INTO Visits (patient_id, date, reason) VALUES (2, '2023-03-05', 'Flu Symptoms');

-- Insert Diagnoses
INSERT INTO Diagnoses (visit_id, diagnosis) VALUES (1, 'Good Health');
INSERT INTO Diagnoses (visit_id, diagnosis) VALUES (2, 'Influenza');
