import re

textToSearch = ''' 
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

aminux.com

321-555-4321
123.555.1234

Mr. Hassan
Mr Ali
Ms Davis
Mrs. Robinson
Mr. T '''

text = 'You\'ll know you\'re strong when the only option you have is to be strong'
# compiles regular expression and returns object
pattern = re.compile(r'^')
matchs = pattern.finditer(textToSearch)
for match in matchs:
    print(match.group(0))


# print(r'\ttab')
