class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1
    def displayCount(self):
        print("TOtal Employee :",Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name,",salary:",self.salary)
emp1=Employee("Yuvaraj",55000)
print("Total Employee",Employee.empCount)
emp2=Employee("Raju",54000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee {0}".format(Employee.empCount))
emp3=Employee("Praveen",55500)
#print("Total Employee %d" %Employee.empCount)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
print("Total Employee {0}".format(Employee.empCount))
        
