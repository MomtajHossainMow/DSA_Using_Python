#Tuple is immutable and it can contain elements of different type 
#Create tuple
numbers = (1, 2, 3, 4, 5)
print("Elements of the tuple are:", numbers)

#Creating tuple with the use of a list
name_list = ["Shayan", "Shohan", "Dola", "Mona", "Moni"]
name = tuple(name_list)
print("Elements of the tuple 'name' are:", name)

#Accessing the first element of the tuple using index
print("First element of the name tuple is:", name[0])

#Accessing the elements of tuple using for loop
print("Elements of the tuple 'numbers' are:")
for number in numbers:
    print(number)