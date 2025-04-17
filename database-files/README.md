# `database-files` Folder

This folder contains the SQL files necessary for initializing and populating the `PharmacogeneticAppDB` database.

### Structure of the Files

1. **SQL Schema Files**: These files contain the schema definitions for the database, including table creation, relationships, and foreign keys. These files are responsible for creating the structure that supports storing the application data.
   
2. **Sample Data Files**: These files are used to populate the database with mock data for testing and development purposes. They contain `INSERT` statements to add realistic but non-sensitive data into the tables. 

### How to Re-Bootstrap the Database

To reset or re-bootstrap the database (e.g., after making changes to the schema or adding new mock data), follow these steps:

1. **Stop Running Containers**: If your containers are running, stop them first by executing:
   ```bash
   docker compose down
