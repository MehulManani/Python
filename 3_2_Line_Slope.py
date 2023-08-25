"""
Practical : 3.2
Aim: Write a program to compute the slope of a line between two points
     (x1, y1) and (x2, y2).
     The equation to calculate the slope of a line is: 
     Slope = (y2 - y1)/(x2 - x1)
Date:15/09/2022
Enrollment No: 216450307001
Name: Mehul Manani
"""


x1 = float(input("Enter the x coordinate of Point 1: "))
y1 = float(input("Enter the y coordinate of Point 1: "))

x2 = float(input("Enter the x coordinate of Point 2: "))
y2 = float(input("Enter the y coordinate of Point 2: "))

slope = (y2 - y1)/(x2 - x1)

print(f"The slope of the line from Points ({x1},{y1}) and ({x2},{y2}) is : {slope}")
