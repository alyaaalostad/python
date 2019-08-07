from datetime import datetime

class Employee:
	def __init__(self,name, age,salary, employement_date):
		self.name=name
		self.age=age
		self.salary=salary
		self.employement_date=employement_date


	def get_working_years(self, today, employement_date):
		date = datetime.now()
		today=date.year
		employement_year= today - employement_date

	def __str__(self):
	        return "name: %s age: %d salary: %d employement_date: %d" % (self.name, self.age, self.salary, self.employement_date)

class Manager(Employee):
	def __init__(self, name, age, salary, employement_date,bonus_percentage):
		Employee.__init__(self, name, age, salary, employement_date)
		self.bonus_percentage=bonus_percentage

	def get_working_years(self, today, employement_date): 
		super().get_working_years(today, employement_date)

	def get_bonus(self,bonus_percentage, salary):
		bonus_percentage * salary

	def __str__(self):
	        return "name: %s age: %d salary: %d employement_date: %d bonus_percentage: %d" % (self.name, self.age, self.salary, self.employement_date, self.bonus_percentage)


def print_menu():
	print("")
	print(" Welcome to HR Pro 2019")
	print("Choose an action to do: ")
	action=[
	"show employees",
	"show managers",
	"add an employee",
	"add a manager",
	"exit",
	]

	action_list=1
	for user_action in action:
		print("  {}. {}".format(action_list, user_action))
		action_list+=1

	choice= int(input("What would you like to do?"))
	print()

	return choice

employees=[]
managers=[]

choice= print_menu()

while choice != 5:
	if(choice==1):
		for e in employees:
			print(e)

	elif (choice==2):
		for m in managers:
			print(m)

	elif (choice==3):
		name = input("Name: ")
		age = int(input("Age: "))
		salary = int(input("Salary: "))
		employement_date = int(input("Employment date: "))

		employee = Employee(name,age,salary,employement_date)
		employees.append(employee)
		print("Employee added succesfully")

	elif (choice==4):
		name = input("Name: ")
		age = int(input("Age: "))
		salary = int(input("Salary: "))
		employement_date = int(input("Employment date: "))
		bonus_percentage=int(input("bonus percentage: "))

		manager = Manager(name,age,salary,employement_date,bonus_percentage)
		managers.append(manager)
		print("Manager added succesfully")

	else:
		print("you have entered an invalid number")

	choice = print_menu()






