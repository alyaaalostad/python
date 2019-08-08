from datetime import datetime

class Employee:
	def __init__(self,name, age,salary, employement_date, **kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employement_date=employement_date

		for key, value in kwargs.items():
			setattr(self, key, value)


	def get_working_years(self, today, employement_date):
		employement_date_year= today - employement_date
		print("years of employement:{}".format(employement_date_year))

	def __str__(self):
	        return "name: %s age: %d salary: %d employement_date: %d " % (self.name, self.age, self.salary, self.employement_date)

class Manager(Employee):
	def __init__(self, name, age, salary, employement_date,bonus_percentage):
		Employee.__init__(self, name, age, salary, employement_date)
		self.bonus_percentage=bonus_percentage

	def get_working_years(self, today, employement_date): 
		super().get_working_years(today, employement_date)



	def get_bonus(self,bonus_percentage, salary):
		manager_bonus= bonus_percentage * salary
		print("Manager's bonus: {}".format(manager_bonus))


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
			date = datetime.now()
			today=date.year
			e.get_working_years(today,employement_date)

	
	elif (choice==2):
		for m in managers:
			print(m)
			date = datetime.now()
			today=date.year
			m.get_working_years(today,employement_date)
			m.get_bonus(bonus_percentage, salary)


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






