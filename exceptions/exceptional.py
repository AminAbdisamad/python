import sys

s = input("Enter Your Name:")


def convert(s):
    if not isinstance(s, str):
        raise TypeError("Argument Must be a string")
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion Error: {} ".format(str(e)), file=sys.stderr)
        return e


print(convert(s))
