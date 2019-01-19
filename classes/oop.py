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

aminux.get_name()
aminux.get_email()

aminux.tostring()


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

Abdihalim.customer_info()


''' How Multiple classes interact each other '''
#Robots class
class Robots:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce(self):
        print("I'm {} my color is {} and my weight is {}".format(self.name,self.color,self.weight))

GA = Robots("GA","Blue",45)
Siri = Robots("Siri","green",56)
# GA.introduce()
# Siri.introduce()

#Company class

class Company:
    def __init__(self,name,type,isOpensource):
        self.name = name
        self.type = type
        self.isOpensource = isOpensource
        # self.robotOwned = robotOwned
    

# init company

Apple = Company("Apple","Computer Manufacturer",False)
Google = Company("Google","Internet",True)

Apple.robotOwned = Siri
Apple.robotOwned.introduce()


def test(c,e,d):
    return c > e+d 
    # if c > e + d:
    #     return True
    # else:
    #     return False

test(5,4,0)





