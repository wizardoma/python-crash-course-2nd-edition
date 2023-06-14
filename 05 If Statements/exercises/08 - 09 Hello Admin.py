# Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a
# website. Loop through the list, and print a greeting to each user:
# If the username is 'admin', print a special greeting, such as Hello
# admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you
# for logging in again.

usernames = ["alex","lex","james","wilson","admin"]

for username in usernames:
    if ("admin" == username):
        print("Hello admin, would you like to see status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")


# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the
# correct message is printed.

usernames = []

if (not usernames):
    print("We need to find some users")