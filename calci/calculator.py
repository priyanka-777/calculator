#basic calculator using python
#for adding
def add(x,y):
	return x+y
#for subtracting
def subtract(x,y):
	return x-y
#for multiplying
def multiply(x,y):
	return x*y
#for division
def divide(x,y):
	return x/y
while True:
	num1=float(input("enter first number:"))
	num2=float(input("enter second number:"))
	print("enter the operation to be performed:")
	print("1.ADD")
	print("2.SUBSTRACT")
	print("3.MULTIPLY")
	print("4.DIVIDE")
	operation=int(input())
	if (operation == 1):
		print (num1 , "+" , num2,"=" ,add(num1,num2))
	elif (operation == 2):
		print (num1 , "-" , num2,"=" ,subtract(num1,num2))
	elif (operation == 3):
		print (num1 , "*" , num2,"=" ,multiply(num1,num2))
	elif (operation == 4):
		print (num1 , "/" , num2,"=" ,divide(num1,num2))
	else:
		print("invalid entry")
	next_calculation=input("enter 0 to stop the process:")
	if (next_calculation == 0):
		break
