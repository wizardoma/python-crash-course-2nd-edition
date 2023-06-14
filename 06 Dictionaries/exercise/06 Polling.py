# Use the code in favorite_languages.py (page 97).
# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some
# that are not.
# Loop through the list of people who should take the poll. If they
# have already taken the poll, print a message thanking them for
# responding. If they have not yet taken the poll, print a message
# inviting them to take the poll.

polls = {
    "alex": 3,
    "james": 5,
    "wilson": 6
}

names = ["james", "ibekas", "victor"]

for nam in names:
    if (nam in polls.keys()):
        print(f"Your name {nam} is already among those who polled")
    else: 
        print(f"{nam} please take a poll")