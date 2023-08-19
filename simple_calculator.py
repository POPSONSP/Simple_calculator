"""
PROJECT:
Write a simple programme requesting for firstname, lastname,location,  two values to be added, the sum of the two values 
the print the names, loation and the total
"""
fname = input("Enter fname: ")
lname= input("Enter lname: ")
location= input("Enter location: ")
val1 =(input("Enter your first valaue: "))
val2 = (input('Enter your second value: '))
total = int(val1) + int(val2)
print(f" My name is {lname} {fname}, i am presently located in {location} my total score is {total}")