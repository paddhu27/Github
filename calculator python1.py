from ast import Yield
def addition(x,y):
	result=x+y
	print(x,"+",y,"=",result)
def subtraction(x,y):
	result=x-y
	print(x,"-",y,"=",result)
def multiplication(x,y):
	result=x*y
	print(x,"*",y,"=",result)
def division(x,y):
	result=x/y
	print(x,"/",y,"=",result)
def power(x,y):
	result=x**y
	print(x,"^",y,"=",result)
number1=float(input("enter first number:"))
number2=float(input("enter second number:"))
print("choose the operation that you want to perform")
print("+ for addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Divison")
print("^ for exponent")
choice=input()
if (choice == '+'):
	addition(number1,number2)
elif (choice == '-'):
	subtraction(number1,number2)
elif (choice == '*'):
	multiplication(number1,number2)
elif (choice == '/'):
	division(number1,number2)
elif (choice == '^'):
	power(number1,number2)
else:
	print("invalid entry")
