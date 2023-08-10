"""
Practical : 2
Aim: Write a program to read your name, contact number, email, and 
birthdate and print those details on the screen. 
Date:15/09/2022
Enrollment No: 216450307001
Name: Mehul Manani

"""



my_name = input("Enter Your Name:\n")
contact_number = input("Enter Your Number:\n")
my_email = input("Enter Your Email Address:\n")
my_birthdate = input("Enter Your Birth Date:\n")

print("\tHello Friends")
print("*******************************")
# print("My name is: ", my_name)
# print("My Contact Number is :", contact_number)

# print("My name is: " + my_name)
# print("My Contact Number is :" + contact_number)

# print("My name is: {}" .format(my_name))
# print("My Contact Number is : {}" .format(contact_number))

print(f"My Name is: {my_name}")
print(f"My Contact Number is : {contact_number}")
print(f"My Email Address is: {my_email}")
print(f"I Was Born on Date : {my_birthdate}")