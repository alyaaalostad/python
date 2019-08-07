
list_item=[]
price_total=[]
total=0

#checks the users input and leave the loop if the input was "done".
#Save the user's inputs in a dictionary and append it to the list of items.
while True:
	users_input={}
	item= input("item (enter 'done' when finished): ")
	if 'done' in item:
		break
	price= float(input("price: "))
	quantity= int(input("quantity: "))
	users_input['item']=item
	users_input['price']=price
	users_input['quantity']=quantity
	list_item.append(users_input)


print("-----------------")
print("receipt")
print("-----------------")




#Using a for loop, go through the list and print the receipt.

for receipt in list_item:

	#print(price_total)

	price_total=receipt['price'] * receipt['quantity']
	print("{} {} {} KD".format(receipt['quantity'], receipt['item'], price_total))
	total= price_total + total 

print("-----------------")
print("total: {}KD".format(total))