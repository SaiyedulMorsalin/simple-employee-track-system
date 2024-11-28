Employee Information Tracking System
====================================

Overview
--------

This is a **Python CLI application** designed to manage and track employee information. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations for employee data, ensuring a user-friendly experience and proper alignment of output.

Features
--------

1.  **Add a New Employee**
    
    *   Adds a new employee to the system with a unique ID.
        
    *   Validates that Employee ID is not duplicated.
        
2.  **Update Employee Information**
    
    *   Updates existing employee details such as Name, Designation, or Salary.
        
    *   Leaves fields unchanged if no new value is provided.
        
3.  **Delete an Employee**
    
    *   Deletes an employee by their Employee ID.
        
4.  **View All Employees**
    
    *   Displays all employee records in a properly formatted table.
        
5.  **Search Employee**
    
    *   Searches for employees by name or designation.
        
6.  **Save and Load Data**
    
    *   Saves all employee data to a .txt file to persist between program runs.
        
7.  **Exit Program**
    
    *   Allows the user to terminate the program gracefully.
        

Usage
-----

### **Running the Program**
**  Prerequisites
  *   Python 3.6 or higher installed.
      
  *   Basic understanding of the CLI.
1. Clone the repo
 ```sh
 git clone https://github.com/SaiyedulMorsalin/simple-employee-track-system.git
 ```
2. Run This Program
 ```sh
  python main.py
 ```

    

### **Example Output**
---- Employee List ----
  
| ID  | Name |  Designation  | Salary |
| ------------- | ------------- |  ------------- | ------------- |
| 1  | Rahim | Junior Developer  | 20000  |
| 2  | Karim  | Python Developer | 25000 |
| 3  | Hasim  | Django Developer | 25000 |
| 4  | Saiyedul  | Python Developer | 25000 |




Files
-----

1.  **main.py**
    
    *   Entry point of the application.
        
    *   Manages the CLI interface and user inputs.
        
2.  **employee\_manager.py**
    
    *   Contains the EmployeeManager class for core functionality like adding, updating, deleting, and searching employees.
        
3.  **employee.txt**
    
    *   Stores employee data persistently between program runs.
        

How to Add or Edit an Employee
------------------------------

### Add Employee

1.  Select option 1 from the menu.
    
2.  Enter a **unique ID**, **Name**, **Designation**, and **Salary**.
    
3.  The system validates the ID for uniqueness before adding.
    

### Update Employee

1.  Select option 2 from the menu.
    
2.  Enter the Employee ID to update.
    
3.  Provide new values for fields or leave blank to keep them unchanged.
    


    

Author
------

Developed by Saiyedul Morsalin as part of an assignment for creating a Python CLI application to manage employee information.
