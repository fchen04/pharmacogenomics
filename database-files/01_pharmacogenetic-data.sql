use PharmacogeneticAppDB

-- ------------------------------------------------------------
-- Table Creation Script for PharmacogeneticAppDB
-- ------------------------------------------------------------

-- Disable foreign key checks and unique checks to allow for table creation
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- ------------------------------------------------------------
-- Clinical Domain Tables
-- ------------------------------------------------------------

-- Table: DOCTOR
-- This table stores information about doctors involved in the treatment
CREATE TABLE IF NOT EXISTS DOCTOR (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255)
);

-- Table: PATIENT
-- This table stores patient details
CREATE TABLE IF NOT EXISTS PATIENT (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Age INT,
    ContactInfo VARCHAR(255)
);

-- Table: DATA_SOURCE
-- This table stores the source of the genetic data
CREATE TABLE IF NOT EXISTS DATA_SOURCE (
    SourceID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Type VARCHAR(100)
);

-- Table: GENETIC_PROFILE
-- This table stores the genetic data for each patient
CREATE TABLE IF NOT EXISTS GENETIC_PROFILE (
    ProfileID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    TestDate DATE,
    GeneticMarkers TEXT,
    SourceID INT,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID),
    FOREIGN KEY (SourceID) REFERENCES DATA_SOURCE(SourceID)
);

-- Table: MEDICATION
-- This table stores details about medications
CREATE TABLE IF NOT EXISTS MEDICATION (
    MedicationID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Indications TEXT,
    DosageGuidelines TEXT
);

-- Table: PRESCRIPTION
-- This table stores prescriptions given to patients
CREATE TABLE IF NOT EXISTS PRESCRIPTION (
    PrescriptionID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    MedicationID INT NOT NULL,
    Date DATE,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES DOCTOR(DoctorID),
    FOREIGN KEY (MedicationID) REFERENCES MEDICATION(MedicationID)
);

-- Table: DRUG_INTERACTION
-- This table stores drug interaction data for medications
CREATE TABLE IF NOT EXISTS DRUG_INTERACTION (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY,
    Medication1ID INT NOT NULL,
    Medication2ID INT NOT NULL,
    InteractionDetails TEXT,
    FOREIGN KEY (Medication1ID) REFERENCES MEDICATION(MedicationID),
    FOREIGN KEY (Medication2ID) REFERENCES MEDICATION(MedicationID)
);

-- Table: ALERT
-- This table stores alerts related to patients
CREATE TABLE IF NOT EXISTS ALERT (
    AlertID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    AlertType VARCHAR(100),
    Message TEXT,
    Date DATE,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID)
);

-- Table: TREATMENT_PROGRESS
-- This table stores progress of the treatment for each patient
CREATE TABLE IF NOT EXISTS TREATMENT_PROGRESS (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    Date DATE,
    SymptomScore VARCHAR(50),
    LabResults TEXT,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID)
);

-- Table: MEDICATION_RECOMMENDATION
-- This table stores medication recommendations based on genetic information
CREATE TABLE IF NOT EXISTS MEDICATION_RECOMMENDATION (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    MedicationID INT NOT NULL,
    Date DATE,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID),
    FOREIGN KEY (MedicationID) REFERENCES MEDICATION(MedicationID)
);

-- ------------------------------------------------------------
-- System Administration Domain Tables
-- ------------------------------------------------------------

-- Table: ROLE
-- This table stores roles in the system
CREATE TABLE IF NOT EXISTS ROLE (
    RoleID INT AUTO_INCREMENT PRIMARY KEY,
    RoleName VARCHAR(100) NOT NULL
);

-- Table: SYSTEM_USER
-- This table stores system user details
CREATE TABLE IF NOT EXISTS SYSTEM_USER (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL UNIQUE,
    HashedPassword VARCHAR(255) NOT NULL,
    RoleID INT,
    FOREIGN KEY (RoleID) REFERENCES ROLE(RoleID)
);

-- Table: SYSTEM_LOG
-- This table stores logs of system events
CREATE TABLE IF NOT EXISTS SYSTEM_LOG (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    Timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    EventType VARCHAR(50),
    Message TEXT,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES SYSTEM_USER(UserID)
);

-- Table: EXTERNAL_SYSTEM
-- This table stores external system details for integration
CREATE TABLE IF NOT EXISTS EXTERNAL_SYSTEM (
    ExternalSystemID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    API_Endpoint VARCHAR(255)
);

-- Table: ENCRYPTION_SETTINGS
-- This table stores encryption settings for securing data
CREATE TABLE IF NOT EXISTS ENCRYPTION_SETTINGS (
    SettingID INT AUTO_INCREMENT PRIMARY KEY,
    Parameter VARCHAR(255) NOT NULL,
    Value VARCHAR(255) NOT NULL,
    LastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Table: CLEANUP_TASK
-- This table stores cleanup tasks for data maintenance
CREATE TABLE IF NOT EXISTS CLEANUP_TASK (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,
    Description TEXT,
    ScheduledDate DATE,
    Status VARCHAR(50)
);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
