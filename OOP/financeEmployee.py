#!/usr/bin/python
""" This class implements inheritance, overriding etc concepts"""


class FinanceEmployee (Employee):
    'FinanceEmployee inhrits from Employee class'
    def __init__(self):
        print("FinanceEmployee class constructor")
        
#restricting access based on the class to which thsi employee belongs

    def __init__(self, name, dob, salary, age, address, phone, accessFin):
        self.name = name
        self.dob = dob
        self.salary = salary
        self.age = age
        self.address = address
        self.phone = phone
        self.accessFin = accessFin
        
    def count(self):
        print("Total Employees in Finance Dept are: ", FinanaceEmployee.empCount)
              
    def retrieveEmployeeData(self):
        print("Name: ", self.name, "date of birth: ", self.dob, 
             "Income: ", self.salary, "Age: ", self.age,
             "Address: ", self.address, "Contact: ", self.phone, "accessFin: ", self.accessFin)
