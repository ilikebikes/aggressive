import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('aggressive_driving_reports.db')
cursor = conn.cursor()

# Create a table for the reports
cursor.execute('''
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    location TEXT,
    vehicle_description TEXT,
    driver_behavior TEXT,
    reporter_contact TEXT
)
''')

conn.commit()
conn.close()

def add_report(date, time, location, vehicle_description, driver_behavior, reporter_contact):
    conn = sqlite3.connect('aggressive_driving_reports.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO reports (date, time, location, vehicle_description, driver_behavior, reporter_contact)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (date, time, location, vehicle_description, driver_behavior, reporter_contact))
    conn.commit()
    conn.close()
    print("Report added successfully!")

def display_reports():
    conn = sqlite3.connect('aggressive_driving_reports.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports')
    reports = cursor.fetchall()
    conn.close()
    for report in reports:
        print(f"ID: {report[0]}")
        print(f"Date: {report[1]}")
        print(f"Time: {report[2]}")
        print(f"Location: {report[3]}")
        print(f"Vehicle Description: {report[4]}")
        print(f"Driver Behavior: {report[5]}")
        print(f"Reporter Contact: {report[6]}")
        print("-" * 40)

def main():
    while True:
        print("Aggressive Driving Report System")
        print("1. Report an Incident")
        print("2. View Reports")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM): ")
            location = input("Enter the location: ")
            vehicle_description = input("Enter the vehicle description: ")
            driver_behavior = input("Describe the aggressive behavior: ")
            reporter_contact = input("Enter your contact information: ")
            add_report(date, time, location, vehicle_description, driver_behavior, reporter_contact)
        
        elif choice == '2':
            display_reports()
        
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
