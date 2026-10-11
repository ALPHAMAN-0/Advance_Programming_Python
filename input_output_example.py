"""Beginner-friendly console input and output example."""

name = input("Enter your name: ")
age_text = input("Enter your age: ")

try:
    age = int(age_text)
    next_year_age = age + 1
    print(f"Hello, {name}! Next year you will be {next_year_age} years old.")
except ValueError:
    print("Please enter a valid whole number for age.")
