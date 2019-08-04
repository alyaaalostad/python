

#Asking the user
first_number= input("Enter the first number:  ")
second_number= input("Enter the second number:  ")
operation= input("Choose the operation (+,-,/,*): ")

#checking whether the numbers are numbers
firstNumber=first_number.isdigit()
secondNumber=second_number.isdigit()


#If the numbers provided were valid
if (firstNumber and secondNumber):
	if operation == "*":
		answer= int(first_number) * int(second_number)
		print(answer)
		
	elif operation == "/":
		answer= int(first_number) / int(second_number)
		print(answer)

	elif operation == "+":
		answer= int(first_number) + int(second_number)
		print(answer)

	elif operation == "-":
		answer= int(first_number) - int(second_number)
		print(answer)

	else:
		print("the operation is invalid")

else:
	print("the numbers were invalid")



	