# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:19:52 2024

@author: Sharvani Yadav
"""

fruits = ["apple", "banana", "orange"]

# Looping through a list
print("Looping through a list:")
for iterator in fruits:
    print(iterator)

# Looping through a string
print("\nLooping through a string:")
for char in "Hello":
    print(char)

# Looping through a range of numbers
print("\nLooping through a range of numbers:")
for num in range(1, 5):
    print(num)

# Looping through a dictionary
print("\nLooping through a dictionary:")
student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)