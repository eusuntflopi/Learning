# Checking if a value is in a list
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings) # True
print("pepperoni" in requested_toppings) # False

# Checking whether a value is NOT in a List
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    