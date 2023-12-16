CREATE TABLE Patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE,
    gender TEXT
);

CREATE TABLE Visits (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    date DATE,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id)
);

CREATE TABLE Diagnoses (
    id INTEGER PRIMARY KEY,
    visit_id INTEGER,
    diagnosis TEXT,
    FOREIGN KEY (visit_id) REFERENCES Visits(id)
);

CREATE TABLE Treatments (
    id INTEGER PRIMARY KEY,
    diagnosis_id INTEGER,
    treatment TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnoses(id)
);
