import sqlite3
import os

def initialize_database():
    db_path = "student.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Check if the STUDENT table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENT'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create STUDENT table
        cursor.execute("""
            CREATE TABLE STUDENT (
                NAME TEXT,
                CLASS TEXT,
                SECTION TEXT,
                MARKS INTEGER
            );
        """)

        # Insert sample records
        students = [
            ('Krish', 'Data Science', 'A', 90),
            ('Sudhanshu', 'Data Science', 'B', 100),
            ('Darius', 'Data Science', 'A', 86),
            ('Vikash', 'DEVOPS', 'A', 50),
            ('Dipesh', 'DEVOPS', 'A', 35)
        ]
        cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)
        connection.commit()

        print("STUDENT table created and data inserted.")
    else:
        print("STUDENT table already exists. Skipping creation and insertion.")

    connection.close()

# Optional: Run this function directly if this script is executed
if __name__ == "__main__":
    initialize_database()
