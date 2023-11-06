# Health and Fitness Tracking App

## Overview
This project is a Health and Fitness Tracking App that emphasizes the importance of sleep in overall well-being. The app integrates various health metrics, including physical activity, nutrition, sleep, and mental well-being to provide users with a comprehensive view of their health.

## Repository Structure
- `create_tables.py`: Defines the SQL schema for the app, including tables, columns, primary keys, and foreign keys.
- `insert_data.py`: Populates the database with sample data using the Python Faker library.
- `query_data.py`: Contains diverse SQL query scenarios to extract meaningful insights from the stored data.

## Setup and Execution

### Prerequisites
- Python 3.x
- SQLite
- SQLAlchemy
- Python Faker library

### Steps to Run the Project

1. **Set Up a Virtual Environment**:
   ```
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. **Install Required Packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Scripts**:
   - To create the database tables:
     ```
     python create_tables.py
     ```
   - To populate the database with sample data:
     ```
     python insert_data.py
     ```
   - To execute the SQL query scenarios:
     ```
     python query_data.py
     ```

5. **Deactivate the Virtual Environment**:
   ```
   deactivate
   ```

## Key Features
- **Data Normalization**: The database design follows normalization principles, ensuring data consistency and reducing redundancy.
- **Dynamic Data Population**: Uses the Python Faker library to generate diverse and realistic sample data.
- **Comprehensive Query Scenarios**: Offers insights into nutrition-sleep correlation, dynamic recommendations based on sleep score, the impact of nutrition on workouts, and more.
