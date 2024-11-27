from employee_manager import EmployeeManager


def main():
    manager = EmployeeManager()

    while True:
        print("\n--- Employee Information Tracking System ---")
        print("1. Add New Employee")
        print("2. Update Existing Employee Information")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Search Employee")
        print("6. Exit this program...")
        option = input("Enter your choice: ").strip()

        if option == "1":
            while True:
                emp_id = input("Enter Employee ID: ").strip()
                if not emp_id:
                    print("Employee ID cannot be empty. Please try again.")
                    continue

                employees = manager.view_employees()
                if employees and any(emp.emp_id == emp_id for emp in employees):
                    print("This Employee ID already exists. Please enter a unique ID.")
                else:
                    break

            name = input("Enter Employee Name: ").strip()
            if not name:
                print("Employee name cannot be empty.")
                continue

            designation = input("Enter Designation: ").strip()
            if not designation:
                print("Designation cannot be empty.")
                continue

            salary = input("Enter Employee Salary: ").strip()
            if not salary.isdigit():
                print("Salary must be a valid number.")
                continue

            manager.add_employee(emp_id, name, designation, salary)
            print("\n Employee added successfully! ")

        elif option == "2":
            emp_id = input("Enter Employee ID to Update: ").strip()
            name = input("Enter new Name (Leave blank to keep unchanged): ").strip()
            designation = input("Enter new Designation (Leave blank to keep unchanged): ").strip()
            salary = input("Enter new Salary (Leave blank to keep unchanged): ").strip()

            if manager.update_employee(emp_id, name or None, designation or None, salary or None):
                print("\n Employee updated successfully!")
            else:
                print(" \n Employee not found!")

        elif option == "3":
            emp_id = input("Enter Employee ID to Delete: ").strip()
            employees = manager.view_employees()
            if any(emp.emp_id == emp_id for emp in employees):
                manager.delete_employee(emp_id)
                print(" \n Employee deleted successfully!")
            else:
                print("\n Employee ID not found. No deletion performed.")

        elif option == "4":
            employees = manager.view_employees()
            if employees:
                print("\n---- Employee List ----")
                print(f"{'ID':<5} {'Name':<20} {'Designation':<25} {'Salary':<10}")
                print("-" * 65)
                for emp in employees:
                    print(f"{emp.emp_id:<5} {emp.name:<20} {emp.designation:<25} {emp.salary:<10}")
            else:
                print("\n No employees found!")


        elif option == "5":
            query = input("Enter name or designation to search: ").strip()
            results = manager.search_employee(query)
            if results:
                print("\n--- Search Results ---")
                for emp in results:
                    print(f"ID: {emp.emp_id}, Name: {emp.name}, Designation: {emp.designation}, Salary: {emp.salary}")
            else:
                print("\n No matching employees found!")

        elif option == "6":
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm_exit in ["yes", "y"]:
                print("Exiting program...")
                break
            else:
                print("Returning to the main menu.")

        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
