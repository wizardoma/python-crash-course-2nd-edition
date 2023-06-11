# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical
# order.

# Print your list in its original order. Don’t worry about printing the
# list neatly, just print it as a raw Python list.

# Use sorted() to print your list in alphabetical order without
# modifying the actual list.

# Show that your list is still in its original order by printing it.

# Use sorted() to print your list in reverse alphabetical order without
# changing the order of the original list.

# Show that your list is still in its original order by printing it again.

# Use reverse() to change the order of your list. Print the list to show
# that its order has changed.

# Use reverse() to change the order of your list again. Print the list to
# show it’s back to its original order.

# Use sort() to change your list so it’s stored in alphabetical order.

# Print the list to show that its order has been changed.Use sort() to change your list so it’s stored in reverse alphabetical
# order. Print the list to show that its order has changed.

places = ["UK", "Canada","Italy","France","Australia"]

print(places)

new_places = sorted(places)

print(f"Sorted places {new_places}")

print(f"original list {places}")

print(f"reversed sorted {sorted(places,reverse=True)}")

places.reverse()

print(f"reversed list {places}")

places.reverse()
print(f"reversed list again {places}")

places.sort()

print(f"sorted list {places}")

places.sort(reverse=True)

print(f"sorted reveresed list {places}")


