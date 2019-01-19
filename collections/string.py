greeting = "HelloWorld"

# Capitalize
print(greeting.capitalize())

# SwapCase
print(greeting.swapcase())
# len

print(len(greeting))
# Replace
print(greeting.replace('World', 'Aminux'))

# Count

sub = 'w'
print(greeting.count(sub))

# Starts with
print(greeting.startswith('Hello'))

# Ends with
print(greeting.endswith('ld'))

# split - returns list
print(greeting.split())

# Find - finds the position of the elements if not it returns -1 same as indexOf in JS
print(greeting.find('W'))

# Index - same as find except it throws error when not found
print(greeting.index('W'))

# is all alphanumeric
print(greeting.isalnum())
# is all alphabetic
print(greeting.isalpha())
# is degits
print(greeting.isdigit())


