"""
Dictionary is a unordered collection of data that stores 
data in the format of key:value pair. It is like hash tables 
in any other language with the time complexity of O(1).
"""
fruit_quantity = {"Apple":10, "Banana":12, "Mango":5}

#Add new element 
fruit_quantity["Lychee"] = 50
fruit_quantity["Grapes"] = 100
print("Dictionary after adding element:")
for fruits in fruit_quantity:
    print(fruits, fruit_quantity[fruits])

#Updating Value
fruit_quantity["Grapes"] = 50
print("Quantity of grapes after updating value:", fruit_quantity["Grapes"])

#Delete element from the dictionary
del fruit_quantity["Mango"]
print("Dictionary after deleting element:")
for fruit, quantity in fruit_quantity.items():
    print(fruit, quantity)