# Start with the program you wrote for Exercise 6-1 (page 99). Make two new
# dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know
# about each person.

alex = {
    'first_name': "Alexander",
    'last_name': "Ibekason",
    'age': 26,
    'city': "Abuja"
}

james = {
    'first_name': "James",
    'last_name': "Ibekason",
    'age': 24,
    'city': "Aba"
}

wilson = {
    'first_name': "Wilson",
    'last_name': "Ibekason",
    'age': 19,
    'city': "Aba"
}

people = [alex,james,wilson]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}")

