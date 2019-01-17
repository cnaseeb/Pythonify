#!/usr/bin/python

DataScientist = Employee("Zara", "1994", "75000", "25", "London", "0044568956326")
SoftwareEngineer = Employee("David", "1993", "60000", "26", "Berlin", "0049562356326")

DataScientist.retrieveEmployeeData()

SoftwareEngineer.retrieveEmployeeData()

#using built in class attributes
print(Employee.__doc__)

#calling financeEmployee class and creating it's instance
SoftwareEngineer_Finance = FinanceEmployee("Ankur","1990", "60000", "28", "Milano", "0039262356326", "True")
SoftwareEngineer_Finance.retrieveEmployeeData()
