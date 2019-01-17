from employee import Employee
from developer import Developer


class Manager(Employee):
    def __init__(self, first, last, pay, company, employees=None):
        super().__init__(first, last, pay, company)
        if employees is None:
            self._employees = []
        else:
            self._employees = employees

    def addEmp(self, emp):
        if emp not in self._employees:
            self._employees.append(emp)

    def remEmp(self, emp):
        if emp in self._employees:
            self._employees.remove(emp)

    def displayEmp(self):
        for emp in self._employees:
            print("<-- ", emp.fullName())


dev_1 = Developer("Amin", "Balad", "15000", "Facebook", "PHP")
dev_2 = Developer("Arab", "Dahir", "80000", "Facebook", "C++")
mn1 = Manager('Hassan', 'Mohamed', '88000', 'Facebook', [dev_1])
mn1.addEmp(dev_2)
mn1.remEmp(dev_1)

if __name__ == "__main__":
    pass
    print(mn1.displayEmp())
    # We can take advantage with built in functions -isinstance and issubclass
    print(isinstance(Manager, Developer))
    print(issubclass(Manager, Employee))
