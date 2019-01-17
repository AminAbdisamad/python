'''
Sets: Unordered collection of unique, immutable objects
'''

s = {112, 23, 34, 454, 56, 57, 676, 7878}
print(type(s))

d = {}
print(type(d))
# Empty set makes it dictionary so for empty use set
ss = set()
ss.add(12)
ss.add(12)
# Adding multiple items to sort
ss.update([123, 3434, 454, 56, 56, 55])
# Memebership and containment for set
10 in ss  # false
10 not in ss  # returns true

# [.Remove ]Removing item from set - if item is not found it returns an error
ss.remove(12)
ss.discard(123)  # remove Items from set if not found do nothing
# to find type use type
print(type(ss))
print(ss)  # it holds unique value so it will hold only 12

# Removing duplicates from a list
l = [12, 1, 23, 34, 45, 45, 45, 565, 767, 677]
l.sort()
removedDL = set(l)

# Usefull scenario for set

peopleWithBlueEyes = {'Hassan', 'Amin', 'Abdihalim', 'Farah', 'Fardowso'}
peopleWithBlackHair = {'Hassan', 'Ahmed', 'Geedi', 'Farah', 'Fardowso'}
peopleWhoLikeSugar = {'Amin', 'Abdihalim'}
peopleWhoLikesalty = {'Amin', 'Hassan', 'Farah', 'Abdihalim'}
O_Blood = {'Amin', 'Hassan', 'Farah', 'Abdihalim'}
B_Blood = {'Ahmed', 'Omar', 'Geedi', 'Goosab'}

# Lets find people with blue eyes or  black hair - union
blueEyesOrBlackHair = peopleWithBlueEyes.union(
    peopleWithBlackHair)  # returns Hassan, Farah
print(blueEyesOrBlackHair)

# Lets find people with blue eyes and  black hair - intersect
blueEyesAndBlackHair = peopleWithBlueEyes.intersection(
    peopleWithBlackHair)  # returns Hassan, Farah
print(blueEyesAndBlackHair)

# Lets find people with blue eyes and  don't have black hair - difference
blueEyesAndNotBlackHair = peopleWithBlueEyes.difference(
    peopleWithBlackHair)  # returns Hassan, Farah
print(blueEyesAndNotBlackHair)

# Lets find people with blue eyes and  don't have black hair or vise verse - symmetric_difference
blackHairNotBlueEyes = peopleWithBlueEyes.symmetric_difference(
    peopleWithBlackHair)  # returns Hassan, Farah
print(blackHairNotBlueEyes)

# people with blue eyes like sugar # issubset
marunbaa = peopleWhoLikeSugar.issubset(peopleWithBlueEyes)
print(marunbaa)
# people who like sugar have blue eyes # issuperset
marunbaa_mise = peopleWithBlueEyes.issuperset(peopleWhoLikeSugar)
print(marunbaa_mise)

# to test two sets have no members in common use use isdisjoint
O_Blood.isdisjoint(B_Blood)  # true
