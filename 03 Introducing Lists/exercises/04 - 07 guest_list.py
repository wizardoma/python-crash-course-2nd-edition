# If you could invite anyone, living or deceased, to dinner, who would you
# invite? Make a list that includes at least three people you’d like to invite to dinner. Then use
# your list to print a message to each person, inviting them to dinner.

missed_ones = ["Grandma", "Lesley", "Darlington"]

print(f"{missed_ones[0]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[1]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[2]}, I have missed you so much. Please come for dinner")


#Exercise 05 Changing Guest List
# ou just heard that one of your guests can’t make the dinner, so
# you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the
# end of your program stating the name of the guest who can’t make
# it.

# Modify your list, replacing the name of the guest who can’t make
# it with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who
# is still in your list.


print(f"Unfortunately, {missed_ones[2]} cannot make it")

missed_ones[2] = "Nephew"

print(f"We have gotten a new option {missed_ones[2]}")

print(f"{missed_ones[0]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[1]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[2]}, I have missed you so much. Please come for dinner")


# Execise 06 More Guesses
# You just found a bigger dinner table, so now more space is available. Think
# of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a
# print() call to the end of your program informing people that you
# found a bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.

# Use insert() to add one new guest to the middle of your list.

# Use append() to add one new guest to the end of your list.

# Print a new set of invitation messages, one for each person in your
# list.

print("Hurray, I found a bigger table")

missed_ones.insert(0,"Layy")
missed_ones.insert(int(len(missed_ones)/2),"LAiehjf")
missed_ones.append("Last person")

print(f"{missed_ones[0]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[1]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[2]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[3]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[4]}, I have missed you so much. Please come for dinner")
print(f"{missed_ones[5]}, I have missed you so much. Please come for dinner")


# Exercise 7: Shrinking Guest List

# You just found out that your new dinner table won’t arrive in time
# for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that
# prints a message saying that you can invite only two people for
# dinner.
# 
# Use pop() to remove guests from your list one at a time until only
# two names remain in your list. Each time you pop a name from
# your list, print a message to that person letting them know you’re
# sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting
# them know they’re still invited.

# Use del to remove the last two names from your list, so you have
# an empty list. Print your list to make sure you actually have an
# empty list at the end of your program.

print("Just realized we can only invite 2 people for this program")

invitee = missed_ones.pop()
print(f"I am sorry we cant invite you to dinner {invitee}")

invitee = missed_ones.pop()
print(f"I am sorry we cant invite you to dinner {invitee}")
invitee = missed_ones.pop()
print(f"I am sorry we cant invite you to dinner {invitee}")
invitee = missed_ones.pop()
print(f"I am sorry we cant invite you to dinner {invitee}")

del missed_ones[0]

del missed_ones[0]

print(f"List is empty now {missed_ones}")