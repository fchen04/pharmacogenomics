USE PharmacogeneticAppDB;

-- ------------------------------------------------------------
-- Sample Data Inserts for System Users
-- ------------------------------------------------------------

INSERT INTO DOCTOR (Name, Specialty) VALUES
('Dr. Emily Zhang', 'Family Medicine'),
('Dr. John Smith', 'Cardiology');

INSERT INTO PATIENT (Name, Age, ContactInfo) VALUES
('Sarah Johnson', 45, 'sarah.johnson@example.com'),
('Michael Brown', 60, 'michael.brown@example.com');

INSERT INTO DATA_SOURCE (Name, Type) VALUES
('GenLab Inc.', 'Genetic Lab'),
('City Hospital', 'Hospital');

INSERT INTO GENETIC_PROFILE (PatientID, TestDate, GeneticMarkers, SourceID) VALUES
(1, '2025-01-15', 'MarkerA, MarkerB', 1),
(2, '2025-02-10', 'MarkerC, MarkerD', 2);

INSERT INTO MEDICATION (Name, Indications, DosageGuidelines) VALUES
('Metformin', 'Type 2 Diabetes', '500 mg twice daily'),
('Lisinopril', 'Hypertension', '10 mg once daily');

INSERT INTO PRESCRIPTION (PatientID, DoctorID, MedicationID, Date) VALUES
(1, 1, 1, '2025-03-01'),
(2, 2, 2, '2025-03-05');

INSERT INTO DRUG_INTERACTION (Medication1ID, Medication2ID, InteractionDetails) VALUES
(1, 2, 'Increased risk of hypotension');

INSERT INTO ALERT (PatientID, AlertType, Message, Date) VALUES
(1, 'Drug Interaction', 'Potential interaction between Metformin and Lisinopril', '2025-03-02'),
(2, 'Progress', 'Patient requires follow-up visit', '2025-03-06');

INSERT INTO TREATMENT_PROGRESS (PatientID, Date, SymptomScore, LabResults) VALUES
(1, '2025-03-10', 'Mild', 'HbA1c: 7.2%'),
(2, '2025-03-12', 'Moderate', 'BP: 140/90');

INSERT INTO MEDICATION_RECOMMENDATION (PatientID, MedicationID, Date) VALUES
(1, 1, '2025-03-15'),
(2, 2, '2025-03-16');

INSERT INTO ROLE (RoleName) VALUES
('Admin'),
('User');

INSERT INTO SYSTEM_USER (Username, HashedPassword, RoleID) VALUES
('admin_user', 'hashed_password_1', 1),
('regular_user', 'hashed_password_2', 2);

INSERT INTO SYSTEM_LOG (EventType, Message, UserID) VALUES
('Login', 'Admin user logged in', 1),
('Error', 'Failed to sync data', 2);

INSERT INTO EXTERNAL_SYSTEM (Name, API_Endpoint) VALUES
('Hospital Database', 'https://api.hospital.com'),
('Pharmacy System', 'https://api.pharmacy.com');

INSERT INTO ENCRYPTION_SETTINGS (Parameter, Value) VALUES
('EncryptionAlgorithm', 'AES-256'),
('KeyRotationInterval', '90 days');

INSERT INTO CLEANUP_TASK (Description, ScheduledDate, Status) VALUES
('Archive inactive patient records', '2025-04-01', 'Scheduled'),
('Remove outdated genetic profiles', '2025-04-05', 'Scheduled');

commit