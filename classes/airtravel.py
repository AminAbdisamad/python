class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No Airline code in '{}' ".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid Airline code '{}' ".format(number))
        if not (number[:2].isdigit() and int(number[:2]) <= 9999):
            raise ValueError("Invalid route number '{}' ".format(number))
        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]




