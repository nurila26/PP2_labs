#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:
thisset1 = {"apple", "banana", "cherry", "apple"}

print(thisset1)

#True and 1 is considered the same value:
thisset2 = {"apple", "banana", "cherry", True, 1, 2}

print(thisset2)

#False and 0 is considered the same value:
thisset3 = {"apple", "banana", "cherry", False, True, 0}

print(thisset3)

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Using the set() constructor to make a set:
thisset4 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset4)
