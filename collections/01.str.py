'''
Str : is a homogeneous immutable sequence of unicode codepoints characters 
 '''
color = "-".join(["Blue", "red", "green"])
print(color)
colorised = color.split("-")
print(colorised)

hi = ''.join(["Hi", "five", "man"])
print(hi)

# Partition - returns tupple
"unforgetable".partition("forget")
fromCity, seperator, toCity = "London:Tokiyo".partition(":")
print(fromCity, toCity)

# we sometimes use _ for un use or dummy value
departure, _, arival = "Mogadishu-Istanbul".partition("-")
print(departure)

items = ["Apple", "Banana", "Google"]
message = "We have {items[0]},{items[1]} and {items[2]} in our Items list".format(
    items=items)
print(message)
