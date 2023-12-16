-- Transaction for Recording a Visit 
-- To ensure that the visit and its corresponding diagnosis are either both recorded or neither is, maintaining data consistency.
COMMIT;

BEGIN TRANSACTION;

INSERT INTO Visits (patient_id, date, reason) VALUES (1, '2023-04-01', 'Follow-up Visit');
INSERT INTO Diagnoses (visit_id, diagnosis) VALUES ((SELECT id FROM Visits WHERE patient_id = 1 AND date = '2023-04-01'), 'Improved Health');

COMMIT;

-- Transaction for Updating Treatment
-- To guarantee that the addition of a treatment and the update to a diagnosis are processed together, ensuring the database reflects the accurate current state of a patient's medical record.
BEGIN TRANSACTION;

INSERT INTO Treatments (diagnosis_id, treatment, start_date, end_date) VALUES ((SELECT id FROM Diagnoses WHERE diagnosis = 'Influenza'), 'Antiviral Medication', '2023-03-06', '2023-03-13');
UPDATE Diagnoses SET diagnosis = 'Influenza - Under Treatment' WHERE diagnosis = 'Influenza';

COMMIT;
