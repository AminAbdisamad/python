'''A program that provides which year you will be 100 years old '''

name = input("What is you Name?: ")
age = int(input("How old are you?: "))


def hundredYears(age):
    currentYear = 2018
    hundredYearsLater = (currentYear - age) + 100
    return "{0}, Do you know that You will be 100 Years in the year {1}".format(name, hundredYearsLater)


print(hundredYears(age))
