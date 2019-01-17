from employee import Employee


class Developer(Employee):
    _raiseUp = 1.10  # This comes from Employee variable

    def __init__(self, first, last, pay, company, pl):
        super().__init__(first, last, pay, company)  # One way to do it
        #Employee.__init__(self, first, last, pay, company)
        self._pl = pl


dev1 = Developer("Amin", "Abdi", 5000, 'IBM', 'Python')
if __name__ == "__main__":
    print(dev1._pay)
    # print(dev1.info())
    dev1.yearlyRaise()
    print(dev1._pay)
    # print(dev1.info())
    print(dev1._email)
    print(dev1._pl)
