# You don’t have to limit the number of tests you create to ten.
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have
# at least one True and one False result for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

name = "Alexander Onyebuchi Ibekason"

list = ["shoe","bag","mose"]

if name == "Alexander Onyebuchi Ibekason":
    print("name is alex's")

if (name == "JAmes"):
    print("name is not james")

if (len(name) == 28):
    print("name is 28 characters")

if (len(name) != 20):
    print("name is not 20 characters")

if (name.lower() == "alexander ibekason onyebuchi"):
    print("name is also lower for alex's name")

if (len(name) > 20):
    print("name length is greater than 20")   

if (len(name) < 30):
    print("name length is less than 30")

if (len(name) > 20 or len(name) == 28):
    print("name is greater than 28 characters or equal to 28")

if (len(name) < 30 or len(name) == 28):
    print("name length is less than 30 or is equal to 28")

if (len(name) > 20 and len(name) < 30):
    print("name is between 20 to 30 characters long")

if "shoe" in list:
    print("cup is not in the list")

if "phone" not in list:
    print("Phone is not in list")