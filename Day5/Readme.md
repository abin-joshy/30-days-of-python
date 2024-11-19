
## Task:Understand and use the string and String Functions in python

## Description
In Python, strings are sequences of characters.Python provides a wide range of built-in string methods to manipulate and perform operations on strings

String creation
# Create a string
s_single = 'Hello, World!'  # Single quotes
s_double = "Hello, World!" #Double quotes
s_triple = '''Hello,World!'''  # Triple quotes (for multi-line strings)

## Common String Functions:

## 1) String Length-len()
Returns the length of the string (number of characters, including spaces).

Syntax:

length = len(string)

## 2) String Case Conversion:
a) lower() – Converts all characters to lowercase.

#syntax
​​lower = string.lower()

b) upper() – Converts all characters to uppercase.

#syntax
upper = string.upper()

c) title() – Converts the first character of each word to uppercase.

#syntax
title = string.title()

d) swapcase() – Swaps uppercase characters to lowercase and vice versa.

#syntax
swap = string.swapcase()

e) capitalize() – Capitalizes the first character of the string.

#syntax
capital = string.capitalize()

## 3.String Trimming:
strip()
Removes leading and trailing whitespace.

#syntax
strip = string.strip() 

## 4.String Replacement:
1.replace()
replaces one word with another, the first word in the bracket is the word you want to replace and the second word is the new word.

#syntax
string.replace(old, new)

Eg:
s = "green apple"
sn = text.replace("green","orange")
print(result)  
Output:orange apple

6.String Splitting and Joining:
~ split() – Splits a string into a list of substrings.

#syntax
split = string.split()

 Eg:
s = "Hello, World!"
print(s.split(","))  
Output: ['Hello', ' World!'] 
(by using split function in a string the output will be in list format)

~ join() – Joins a list of strings into a single string, separated by a specified delimiter.

#syntax
x = ['a','b']
join = "  ".join(x) #' " " ' act as a seperator

#Eg:
s = ['Hello', 'World']
print(" ".join(words)) 
# Output: Hello World
