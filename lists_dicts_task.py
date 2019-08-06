
print("Welcome to the special recruitment program, please answer the following questions: ")
#These are the skills that the user will choose from.
skills=[
"python",
"c++",
"javascript",
"juggling",
"running",
"eating",
]

#This dictionary will then hold all of the applicants information.
cv={}

#Ask the user for his name
Name= input("name: ")
cv['name']= Name

#Ask the user for his age
age= input("age: ")
cv['age']= age

#Ask the user for his years of experience
years_experience= input("how many years of experience do you have?: ")
cv['experience']= years_experience

#Add a key skills to the cv dictionary and give it an empty list as a value.
cv['skills']=[] 

#Print the skills from the skills list and number them from 1
skill_list=1
for skill_have in skills:
	print("{}- {}".format(skill_list, skill_have))
	skill_list+= 1

#Ask the user to choose a skill from the list
skill_chosen= int(input("choose a skill from above: "))
user_skill= skills[skill_chosen -1 ] 
cv['skills'].append(user_skill)


#Ask the user for another skill and append it to the skills list in the cv dictionary
another_skill=int(input("choose another skill from above: "))
another_user_skill= skills[another_skill -1] 
cv['skills'].append(another_user_skill)

def exceptence (age, user_name, skill_knows1, skill_knows2, skill_year):
	if ("25"<age<"50") and(skill_year>"3"):
		if ("python" in skill_knows1) or ("python" in skill_knows2):
			print("you have been accepted, {}".format(user_name))
	else:
		print("Sorry, you have been rejected")

exceptence(age, Name, user_skill,another_user_skill, years_experience )





