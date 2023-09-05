"""
Practical : 3.4
Aim: Write a program to get change values in Quarter, Dime, 
     Nickels and Pennies, and calculate the value of change in 
     Dollars. Consider Quarter = 0.25 $, Dime = 0.10 $, 
     Nickels = 0.05 $ and Penny = 0.01 $
Date:15/09/2022
Enrollment No: 216450307001
Name: Mehul Manani
""" 

quarter = float(input("How many Quarters do you want to convert in Dollar?: \n"))
dime = float(input("How many Dimes do you want to convert in Dollar?: \n"))
nickel = float(input("How many Nickels do you want to convert in Dollar?: \n"))
penny = float(input("How many Pennies do you want to convert in Dollar?: \n"))


q_dollar = quarter * 0.25
d_dollar = dime * 0.10
n_dollar = nickel * 0.05
p_dollar = penny * 0.01

print(f"For {quarter} Quarters, You will get {q_dollar} Dollars as a change.")
print(f"For {dime} Dimes, You will get {d_dollar} Dollars as a change.")
print(f"For {nickel} Nickels, You will get {n_dollar} Dollars as a change.")
print(f"For {penny} Pennies, You will get {p_dollar} Dollars as a change.")