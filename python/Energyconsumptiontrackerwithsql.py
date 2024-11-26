import mysql.connector
import csv
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database = "csproject"
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consumption (
                id INT AUTO_INCREMENT PRIMARY KEY,
                appliance_name VARCHAR(30),
                energy_used FLOAT,
                cost_per_hour FLOAT,
                Total_cost FLOAT
            )
        """)
        conn.commit()
        return conn
    except Exception as e:
        print(e)
        return None

def add_consumption_to_db(conn, appliance, energy):
    cost_per_hour = float(input("Enter Cost per Hour: "))
    cost = energy * cost_per_hour
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO consumption (appliance_name, energy_used,cost_per_hour,Total_cost) VALUES ('{appliance}', {energy}, {cost_per_hour},  {cost})")
        conn.commit()
        print("Data added to the database successfully!\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

def view_data_from_db(conn):
    global cost_per_hour
    global cost
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consumption")
        for i in cursor:
            print(i)
        print()

    except Exception as e:
        print(e)

def total_consumption_from_db(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(energy_used) FROM consumption")
        total = cursor.fetchone()[0] or 0
        print(f"\nTotal energy consumption: {total} kWh\n")
    except Exception as e:
        print(e)
def delete_consumption_data(conn):
    try:
        view_data_from_db(conn)
        record_id = int(input("Enter the ID of the record to delete: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM consumption WHERE id = %s", (record_id,))
        conn.commit()
        print("Record deleted successfully!\n")
    except Exception as e:
        print(e)
def update_consumption_data(conn):
    try:
        view_data_from_db(conn)
        record_id = int(input("Enter the ID of the record to update: "))
        column = input("Which field do you want to update? (appliance_name, energy_used, cost_per_hour): ")
        new_value = input("Enter the new value: ")
        cursor = conn.cursor()
        x = f"UPDATE consumption SET {column} = %s WHERE id = %s"
        cursor.execute(x, (new_value, record_id))
        conn.commit()
        print("Record updated successfully!\n")
    except Exception as e:
        print(e)
def search_consumption_data(conn):
    try:
        search_term = input("Enter the appliance name to search: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consumption WHERE appliance_name LIKE %s", (f"%{search_term}%",))
        results = cursor.fetchall()

        if results:
            for record in results:
                print(record)
            print()
        else:
            print("No matching records found.\n")
    except Exception as e:
        print(e)
def export_data_to_csv(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consumption")
        results = cursor.fetchall()

        with open("consumption_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Appliance Name", "Energy Used (kWh)", "Cost per Hour", "Total Cost"])
            writer.writerows(results)

        print("Data exported to 'consumption_data.csv' successfully!\n")
    except Exception as e:
        print(e)

def main():
    conn = connect_to_database()
    if not conn:
        print("Failed to connect to the database. Exiting program.")
        return

    while True:
        print("Energy Consumption Tracker")
        print("1. Add Consumption Data")
        print("2. View Consumption Data")
        print("3. Calculate Total Consumption")
        print("4. Delete Consumption Data")
        print("5. Update Consumption Data")
        print("6. Search Records by Appliance Name")
        print("7. Export Data to CSV")
        print("8. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            appliance = input("Enter appliance name: ")
            try:
                energy = float(input("Enter energy used (kWh): "))
                add_consumption_to_db(conn, appliance, energy)
            except Exception as e:
                print(e)
        elif choice == "2":
            view_data_from_db(conn)
        elif choice == "3":
            total_consumption_from_db(conn)
        elif choice == "4":
            delete_consumption_data(conn)
        elif choice == "5":
            update_consumption_data(conn)
        elif choice == "6":
            search_consumption_data(conn)
        elif choice == "7":
            export_data_to_csv(conn)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
