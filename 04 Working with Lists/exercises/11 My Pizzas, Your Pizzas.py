# Start with your program from Exercise 4-1 (page 56).
#  Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# Add a new pizza to the original list.

# Add a different pizza to the list friend_pizzas.

# Prove that you have two separate lists. Print the message My
# favorite pizzas are:, and then use a for loop to print the first list.

# Print the message My friend’s favorite pizzas are:, and then use a for
# loop to print the second list. Make sure each new pizza is stored in
# the appropriate list

pizzas = ["peporoni", "chicken", "tomato"]

friends_list = pizzas[:]

pizzas.append("mushroom")
friends_list.append("bbq")

print("my fav pizzas are ")
for p in pizzas:
    print(f"{p}")


print("my friends fav pizzas are ")
for p in friends_list:
    print(f"{p}")

