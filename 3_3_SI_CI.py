"""
Practical : 3.3
Aim: Write a program to calculate Simple and Compound Interest
    Simple Interest = (P*R*T)/100
    Compound Interest = P * ((1 + (R/(100*n)))**(n*T))
Date:15/09/2022
Enrollment No: 216450307001
Name: Mehul Manani
"""

from tkinter import Y


P = float(input("Enter the Principal Amount: \n"))
R = float(input("Enter the Rate of Interest: \n"))
T = float(input("Enter the Time Period: \n"))
n = float(input("How many times interest is applied during the year? \n"))

SI = (P * R * T) / 100

CI = P * ((1 + (R/(100*n)))**(n*T))
print(f"The Simple Interest of Rs. {P} at Rate {R} for {T} Years is : {SI} ")


print(f"The Compound Interest of Rs. {P} at Rate {R} for {T} Years is : {CI} ")