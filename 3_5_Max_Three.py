"""
Practical : 3.5
Aim:  Write a program to find a maximum of given three numbers 
      (Use ternary operator).
      As Python does not provide any ternary operator, we will use following 
      formula: max = x if x>y else y
Date:15/09/2022
Enrollment No: 216450307001
Name: Mehul Manani
""" 
num_1 = float(input("Enter First Number: \n"))
num_2 = float(input("Enter Second Number: \n"))
num_3 = float(input("Enter Third Number: \n"))

max = (num_1 if (num_1 > num_2 and num_1 > num_3) else (num_2 if (num_2 > num_1 and num_2 > num_3) else num_3))
    
print(f"The Maximum number from given three numbers {num_1}, {num_2} and {num_3} is : {max}")
