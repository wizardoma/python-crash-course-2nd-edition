# Modify your program from Exercise 6-2 (page 99) so each person
# can have more than one favorite number. Then print each person’s name along with their
# favorite numbers.


favorite_numbers = {
    "alex": [3,7,10],
    "james": [4],
    "victor": [6],
    "abba": [7],
    "wilson": [8],

}

for name, numbers in favorite_numbers.items():

    print(f"from our analysis, {name} loves the following numbers")
    for number in numbers:
        print(number)


