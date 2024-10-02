# Intro
# Indentation
# Comments
# Variables
# Data Types
# String
# Multiline strings
# String as Arrays
# Finding a sub string inside a string
# String Concatenation

# I just wrote this print command, for demo purpose
# print("Hello World, this is my first program")
name = "Arpit"
age = 36
price = 399.99
student_ages = (23, 24, 25, 30, 29, 24)
# print(type(student_ages))

my_student = {
    "Name": "Arpit",
    "Age": 45,
    "Mob": 9876543210,
    "City": "Mumbai"
}
# print(my_student['Age'])
# print(type(my_student))

x = True
# print(type(x))

# String
# txt = 'Hey there, this is a dummy message.' \
#       'Hello this is my second line ' \
#       ''

# """"""
# new_txt = """Hey there, this is a dummy message.
# This is the second line.
# This is the third line.
# Keep on writing like this.
# Dont do it now
# AAge padhao"""
# # print(new_txt)

# print(name)
"Arpit"
# print(name[3])








#
# new_txt = """Hey there, this is a dummy message.
# This is the second line.
# This is the third line.
# Keep on writing like this.
# Dont do it now
# AAge padhao"""
#
# if "Message" in new_txt:
#     print("Sub string was present")
# else:
#     print("Sub string was not present")


# String Slicing
# wlcm_msg = "hey there, welcome to my channel"
# s = 11
# e = 17
# print(wlcm_msg[s:e+1])
#
# first_name = "Amitabh"
# last_name = "Arora"
#
# full_name = first_name + " " + last_name # concatenate
# print(full_name)

#
# my_list = ['Apple', "Mango", "Papaya", "Papaya",
#            23, 24.54, True]
# print(my_list)
#
# # Appending new items
# my_list.insert(3, 456)
# print(my_list)
#
# # Appending complete list
# my_list.extend([12, 13, 14])
# print(my_list)
#

my_list1 = [1, 2, 3]
my_list2 = [5, 6, 7]
final_list = my_list1 + my_list2
# print(final_list)

# Tuples
# Creating Tuples
# Data Types in Tuples
# Unchangeable
#
# my_frnds = ("Doraemon", "Nobita", "Giyan", "Suneo", 420)
# # my_frnds[1] = "Dekesugi"
# print(my_frnds)

# Sets
# Unordered, Unchangeable, Unique
# Set Items Data Types
# Access Set Items
# Add Set Items: add()
# Remove Set Items: remove()

my_set = {123, 124, 125, 125, 127, 128, 120}
# print(my_set)
# print(type(my_set))
# #
#
# for item in my_set:
#     print(item)
#
# my_set.add("Hello World")
# print(my_set)
#
# my_set.remove(125)
# print(my_set)


# Dictionary
# Dictionary Items: Ordered, Changeable and No Duplicates
# Data Types

#
# word -> key
# meaning -> value

student = {
    "Name": "Nobita",
    "Age": 14,
    "School": "Dora School"
}
# school_name = student['School']
# print(school_name)
# print(student)
# student['Age'] = student['Age'] + 1
# print(student)




# while loop

# print("Hello World")
#
# counter = 0
# while counter < 15:
#     print("Hey there, I am learning Python")
#     counter = counter + 1
#
#
# my_list = ["Nobita", "Doremon", "Shuzuka", "Giyan", "Suneo"]
#
# for character in my_list:
#     print(f"I am watching {character}")

# Functions
def rajma_bnao():
    print("Market Jao")
    print("Rajma Khareed ke lao")
    print("Ek raat pehle rajma ko paani mein bhigao")
    print("Sabzi ko agle din fridge se bahar nikaalo")
    print("Sabzi ko dhul ke lao")
    print("Sabzi ko kaato")
    print("Bartan gas pe chadhao")
    print("Tel bartan mein daalo aur garam hone do")
    print("Thoda sa door hoke khade rho, varna cheeta padega")
    print("Pyaaz ko garam tel mein daalo")
    print("Haldi daalo pyaz mein")
    print("Hari mirchi ko garam pyaaz mein daalo")
    print("Tamatar ko bartan mein daalo, aur upar se saare masale bhi daal do")
    print("Tamatar ko bhoono, paste bnne do")
    print("Rajma ko masale ke paste mein daalo")
    print("Thodi der usko bhunne do")
    print("Thodi der baad aalu daaldo")
    print("Bhun jane do")
    print("Paani daalo, jyada mat daalna, varna maza nahi aayega")
    print("Cooker mein seeti lga do")
    print("Aur bed pe jake insta reels dekho")
    print("Lekin, sath mein cooker ki seeti bhulna mat")
    print("Varna, raajma jal jayega")
    print("Pakne tak wait kro, swaaad leke enjoy kro")


print("=================Date: 21 Sep====================")
rajma_bnao()
print("=================Date: 23 Sep====================")
rajma_bnao()
print("=================Date: 25 Sep==================")
rajma_bnao()




























