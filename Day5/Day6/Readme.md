## Learn to use Conditional statements 

## 1)Conditional Statements:
a) if statement
Description:
The if statement is used for making decision in Python.
It executes a block of code if the condition evaluates to True.

#Syntax:

if condition:
    # code to execute if the condition is true

b) if-else Statement
Description:
The if-else statement provides an alternative block of code to execute if the condition is False.

#Syntax:

if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

c) if-elif-else Statement:
The if-elif-else statement is used to check multiple conditions. It executes the first block where the condition evaluates to True. If none of the conditions are True, the else block executes.

#Syntax:

if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if no conditions are true

# Task 1 : Age Group Classifier
## Write a program that takes an age as input and classifies the person into an age group of:

◐"Child" if the age is between 0 and 12.
◐"Teenager" if the age is between 13 and 19.
◐"Adult" if the age is between 20 and 64.
◐"Senior" if the age is 65 or older.

Expecter output
Enter your age : 23
You are an adult
