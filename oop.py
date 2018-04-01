# Classes and Objects


class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def tostring(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)


aminux = Person('Amin', 'aminux@gmail.com')
# aminux.set_name('Mohamed Amin')
# aminux.set_email("Aminux@gmail.com")

print(aminux.get_name())
print(aminux.get_email())

print(aminux.tostring())


# Create new Customer class to extend person
class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def customer_info(self):
        return '{} has a balance of {} and can be contacted {}'.format(self.__name, self.__balance, self.__email)


Abdihalim = Customer('Abdihalim', 'abdihalim@gmail.com', 100)

print(Abdihalim.customer_info())






