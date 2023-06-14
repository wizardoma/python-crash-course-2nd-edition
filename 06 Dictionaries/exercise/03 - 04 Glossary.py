# A Python dictionary can be used to model an actual dictionary. However, to
# avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the
# previous chapters. Use these words as the keys in your glossary,and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You
# might print the word followed by a colon and then its meaning, or
# print the word on one line and then print its meaning indented on
# a second line. Use the newline character (\n) to insert a blank line
# between each word-meaning pair in your output

glossary = {
    "java": "Java is an oop language",
    "python": "Python is a functional language",
    "Javascript": "Javascript is the language of the web",
    "C#": "This is a popular programming language owned by Microsoft"
}

print(f"Information about Java \n {glossary['java']}\n")
print(f"Information about Python \n {glossary['python']}\n")
print(f"Information about Javascript \n {glossary['Javascript']}\n")
print(f"Information about C# \n {glossary['C#']}\n")


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from
# Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through
# the dictionary’s keys and values. When you’re sure that your loop works, add five more Python
# terms to your glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary["python"] = "Python is a very versatile language and you can use it for virtually anything in tech"

for language, meaning in glossary.items():
    print(f"Information about {language.capitalize()}\n{meaning}")