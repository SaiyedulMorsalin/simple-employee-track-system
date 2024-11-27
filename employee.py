class Employee:
    def __init__(self,emp_id,name,designation,salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary
        
    
    def __repr__(self):
        return f"{self.emp_id}, {self.name}, {self.designation}, {self.salary}"