import os
from employee import Employee


class EmployeeManager:
    def __init__(self,file_name = "employees.txt"):
        self.file_name = file_name
        self.employees = self.load_employees()
        
    
    def load_employees(self):
        if not os.path.exists(self.file_name) or os.path.getsize(self.file_name) == 0:
            return []
        with open(self.file_name,'r') as file:
            lines = file.readlines()
        return [self.parse_employee(line.strip()) for line in lines]
    
    def save_employees(self):
        with open(self.file_name,'w') as file:
            file.writelines([str(emp) + "\n" for emp in self.employees])
    @staticmethod
    def parse_employee(data):
        emp_id,name,designation,salary = data.split(",")
        return Employee(emp_id,name,designation,salary)
    
    
    def add_employee(self,emp_id,name,designation,salary):
        
        self.employees.append(Employee(emp_id,name,designation,salary))
        self.save_employees()
        
    
    def update_employee(self,emp_id,name=None,designation=None,salary=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                if name:
                    emp.name = name
                if designation:
                    emp.designation = designation
                if salary:
                    emp.salary = salary
                self.save_employees()
                return True
        return False
    
    def delete_employee(self,emp_id):
        self.employees =[emp for emp in self.employees if emp.emp_id != emp_id]
        self.save_employees()
    
    def search_employee(self,query):
        return [emp for emp in self.employees if query.lower() in emp.name.lower() or query.lower() in emp.designation.lower()]
    
    def view_employees(self):
        return self.employees
                