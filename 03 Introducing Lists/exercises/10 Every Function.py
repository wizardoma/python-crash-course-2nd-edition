# Think of something you could store in a list. For example, you could
# make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a
# program that creates a list containing these items and then uses each function introduced in this
# chapter at least once.

list = ["Java","Python","Go"]
list.sort()
print(f"sorted list {list}")

list.sort(reverse=True)
print(f"sorted list {list}")


print(f"sorted list {sorted(list)}")

print(f"sorted reversed list {sorted(list,reverse=True)}")

list.append("Elixir")
print(f"add to end of list {list}")

list.insert(0,"C++")
print(f"add to start of list {list}")

