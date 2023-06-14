# Using one of the programs you wrote in this chapter, add several lines to the end
# of the program that do the following:

# Print the message The first three items in the list are:. Then use a
# slice to print the first three items from that program’s list.

# Print the message Three items from the middle of the list are:. Use a
# slice to print three items from the middle of the list.

# Print the message The last three items in the list are:. Use a slice to
# print the last three items in the list

odd_numbers = [v for v in range(1,11,2)]

print(f"The first three items in the list are {odd_numbers[:3]}")

print(f"The three items in the middle of the list are {odd_numbers[int(len(odd_numbers)/2):int(len(odd_numbers)/2) + 3]}")

print(f"The last three items in the list are {odd_numbers[-3:]}")
