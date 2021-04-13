#1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.
#E.g. :
#a = 1,
#b = 2.01,
#c = 'string'

#a,b,c = 5, 3.4, 'Python'
#print (a, b, c)


#2. Create a variable of type complex and swap it with another variable of type integer.

#a = (4-2j)
#b = 2
#a=b
#print (a)

#3. Swap two numbers using a third variable and do the same task without using any third variable.

#a = 5
#b = 10
#c = b
#b = a
#a = c
#print (a)
#print (b)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

#Version 2
#a = raw_input("State your name:")
#print "So your name is?", a 

#Version 3
#a = input("State your name:")
#print("So your name is?", a)

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.

#print("Kindly enter two numbers in between 1-30 when prompted")

#a = int(input("Enter your first number:"))
#print("Your first number is", a)

#b = int(input("Enter your second number:"))
#print("Your second number is", b)

#c = a+b
#c+=30
#Result = c
#print("Your final output is:", Result)

#6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc

a = (input("Enter an integer:"))
print("The data type of the input value is:" type(a))


# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.

#Upper CamelCase
CamelCase = 1

#LowerCamelCase
camelCase = 2

#SnakeCase
camel_case = 3

#UpperCase
CAMELCASE = 4
#(Refer: https://capitalizemytitle.com/camel-case/)


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
#Yes the value will be changed since Python is a dynamic language and it is able to recognize various data types and compile it in runtime.