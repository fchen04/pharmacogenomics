# `database-files` Folder

## Pharmacogenetics Database Sample Data

This folder contains the SQL files for creating and populating the Pharmacogenetics database system. It includes all the necessary tables, sample data, and insert statements required for your project.

### Files Overview

1. **00_pharmacogenetics.sql**
   - Contains the database schema definition with all table structures necessary for the Pharmacogenetics app, including doctors, patients, medications, genetic profiles, prescriptions, and related tables.

2. **01_pharmacogenetic-data.sql**
   - Contains the SQL insert statements for system data like doctors, patients, medications, and genetic profiles.

3. **02_insert_to_pharmacogenetic.sql**
   - Contains sample insert statements to populate various tables, including data related to prescriptions, drug interactions, alerts, treatment progress, and medication recommendations.

### Data Volumes

This sample data follows the requirements outlined below:

- **Strong entities** (Doctor, Patient, Medication, GeneticProfile, etc.): ~30-40 rows each.
- **Weak entities** (Prescription, DrugInteraction, Alert, TreatmentProgress, etc.): ~50-75 rows each.
- **Bridge tables** (e.g., Prescription-Medication relationships): ~125 rows.

### Usage

The files should be executed in order to set up and populate the database correctly. They are prefixed with numbers to ensure proper execution order. When you create a new database container, these files will be automatically executed.

#### Steps to Use:
1. Place the SQL files in the `database-files` directory of your project repository.
2. Create a new Docker container to load the data by running:
   ```bash
   docker compose up db -d
