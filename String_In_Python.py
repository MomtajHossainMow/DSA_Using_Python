"""
String is the immutable array of bytes representing Unicode characters. Python does not have 
a character data type, a single character is simply a string with a length of 1.
"""
string_1 = "Learning Python"

#Accessing the first character of the string
print("First character of the string is:", string_1[0])
#Accessing the last character of the string
print("Last character of the string is:", string_1[-1])

#Slicing the string using positive index
print("First eight characters of the string are:", string_1[0:8])
#SLicing the string using negative index
print("Last six characters of the string are:", string_1[-7:])

#Checking presence of substring
print("Python is present in the string:", 'Python' in string_1)

#Replace character in string
string_2 = "Learning Python 2"
#It doesn't change the main string, rather creates a new string replacing the characters
new_string = string_2.replace("2", "3")
print("String after replacing the character:", new_string)

#Splitting the string
word_list = new_string.split()
print("Splitted string:", word_list)

#upper() function
print("Upper case of the string_list[0] is:", word_list[0].upper())
#lower() function
print("Lower case of the string_list[1] is:", word_list[1].lower())

#multiplicating string
new_string = "Blah" * 3
print("New string is:", new_string)