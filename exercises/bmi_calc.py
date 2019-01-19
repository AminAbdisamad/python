# A program that calculates BMI

name = input("What is Your Name: ")
hieght = float(input("Write Your height in Meters: "))
weight = float(input("Write Your weight in KG: "))


def bmi_calc(name, hieght, weight):
    bmi = weight / (hieght**2)
    if bmi < 20:
        return "{0}, your BMI is {1:.3f} you're underweight".format(name, bmi)
    elif bmi > 25:
        return "{0}, your BMI is {1:.3f} you're Overweight".format(name, bmi)
    else:
        return "{0}, your BMI is {1:.3f} you're in shape".format(name, bmi)


userinfo = bmi_calc(name, hieght, weight)
print(userinfo)
