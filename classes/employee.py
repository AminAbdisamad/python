import datetime


# Creating class
class Employee:
    # Class variable
    _raiseUp = 1.05
    _numOfEmpl = 0

    # iniate class
    def __init__(self, first, last, pay, company):
        self._first = first
        self._last = last
        self._pay = pay
        self._company = company
        self._numOfEmpl += 1
    # Property Decorator :- getter

    @property
    def email(self):
        return self._first + '.'+self._last+'@'+self._company+'.com'

    @property
    def fullName(self):
        return '{} {}'.format(self._first, self._last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(" ")
        self._first = first
        self._last = last

    @fullName.deleter
    def fullName(self):
        print("User Deleted")
        self._first = ""
        self._last = ""

    # 1. Regular Methods :- automatically takes instance method - self
    def yearlyRaise(self):
        self._pay = int(self._pay * self._raiseUp)

    def info(self):
        return "My Full Name is {0}, I work at {1} with monthly income of ${2}, You can contact me through {3}".format(self.fullName, self._company, self._pay, self.email)

    # 2. Class Method :- automaticaly takes instance calss - cls
    @classmethod
    def setRaiseAmt(cls, amount):
        cls._raiseUp = amount

    @classmethod
    def stringArranger(cls, empString):
        first, last, pay, company = empString.split('-')
        return cls(first, last, pay, company)

    # 3. Static Methods :- don't pass anything automaticaly, a method is static if you don't access instance of the class anywhere in the method
    @staticmethod
    def isWorkday(day):
        # Monday = 0, Saturday = 5, Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Magic Methods
    def __str__(self):
        return "{} - {} - {} - {}".format(self.fullName, self._company, self._pay, self.email)

    def __repr__(self):
        return "Employee('{}', '{}', {},'{}')".format(self._first, self._last, self._pay, self._company)


Employee.setRaiseAmt = 2.0
emp1_str = "Ali-Hassan-7000-AsalSolutions"
emp2_str = "Abdi-Farah-8000-Loopysec"
emp3_str = "Farah-Amin-6000-Google"
emp2 = Employee.stringArranger(emp2_str)
myDate = datetime.date(2019, 1, 13)
emp2.fullName = "Geedi Muran"
if __name__ == "__main__":
    # print(emp1.info())
    # print(emp1.isWorkday(myDate))
    # print(emp1.__repr__())
    print(emp2.fullName)
    print(emp2._first)
    print(emp2._last)
    print(emp2.email)
    del emp2.fullName
    print(emp2.fullName)
