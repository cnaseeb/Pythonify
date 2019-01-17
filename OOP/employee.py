#!/usr/bin/python

class Employee:
    empCount = 0
    
    def __init__(self, name, dob, salary, age, address, phone):
        self.name = name
        self.dob = dob
        self.salary = salary
        self.age = age
        self.address = address
        self.phone = phone
        
    def count(self):
        print("Total Employees in our organization are: ", Employee.empCount)
              
    def retrieveEmployeeData(self):
        print("Name: ", self.name, "date of birth: ", self.dob, 
             "Income: ", self.salary, "Age: ", self.age,
             "Address: ", self.address, "Contact: ", self.phone)
