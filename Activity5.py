cart = {'apple': 2, 'banana': 5, 'milk': 1}

item = input("Enter an item to add to the cart: ").lower()

if item in cart:
    cart[item] += 1         
else:
    cart[item] = 1         

print("You have ", end="") 

items_list = list(cart.items())   

for i in range(len(items_list)):
    name, count = items_list[i]
    
    if i == len(items_list) - 1:          
        print(f"and {count} {name}.")
    else:
        print(f"{count} {name}, ", end="")