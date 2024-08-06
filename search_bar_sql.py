import mysql.connector

# Connect to MySQL server (adjust the user and password as needed)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ganesh@123"
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS college")

# Use the new database
cursor.execute("USE college")

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(255) NOT NULL UNIQUE
)
''')

# Insert sample data
sample_roll_numbers = ['101', '102', '103', '201', '202', '203', '301', '302', '303']
for roll_number in sample_roll_numbers:
    cursor.execute('INSERT IGNORE INTO students (roll_number) VALUES (%s)', (roll_number,))

conn.commit()
conn.close()