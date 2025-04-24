motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

    # change the first element (replace)
#motorcycles[0] = "ducati"
#print(motorcycles)

    # append element to a list (at the end of the list)
#motorcycles.append("ducati")
#print(motorcycles) 

    # starting with empty list, then add elements
#motorcycles_2 = []

#motorcycles_2.append("honda")
#motorcycles_2.append("yamaha")
#motorcycles_2.append("ducati")

#print(motorcycles_2)

    # inserting elements into a list
#motorcycles.insert(0, "ducati")
#print(motorcycles)

    # removing an item using del statement
#del motorcycles[0]
#print(motorcycles)

    # removing an item using the pop() method (last item)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

    # removing items from any position
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

    # removing an item by value
# motorcycles.remove("suzuki")
# print(motorcycles)

too_expensive = "honda"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
