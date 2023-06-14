# Make several dictionaries, where each dictionary represents a different pet. In each
# dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list
# called pets. Next, loop through your list and as you do, print everything you know about each
# pet.

bingo = {
    "name": "Bingo",
    "animal": "dog",
    "owner": "alex"
}

meow = {
    "name": "Meow",

    "animal": "cat",
    "owner": "alex"
}

lucky = {
    "name": "Lucky",

    "animal": "pigeon",
    "owner": "james"
}

promise = {
    "name": "Promise",

    "animal": "dog",
    "owner": "chinedu"
}

pets = [bingo,meow,lucky,promise]

for pet in pets:
    print(f"{pet['name']} is a {pet['animal']} and is owned by {pet['owner']}")


