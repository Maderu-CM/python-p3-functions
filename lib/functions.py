#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name="Naureen"):
    print(f"Hello, {name}!")

greet()          

        
def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

greet_with_default()         
greet_with_default("Sunny") 


def add(num1, num2):
    return num1 + num2
sum_result = add (1,2)
print (sum_result)
 

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

result = halve(100)
print(result)  # Output: 50.0

result = halve(99.0)
print(result)  # Output: 49.5

result = halve("two")
print(result)  # Output: None
