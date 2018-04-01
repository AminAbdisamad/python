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


aminux = Person('Amin', 'aminux@gmail.com')
# aminux.set_name('Mohamed Amin')
# aminux.set_email("Aminux@gmail.com")

print(aminux.get_name())
print(aminux.get_email())


