# ============================================ Functions in Python ===================================================

# 1. Functions: Intro -- done
# 2. Need of Functions  --done
# 3. Creating a Function -- done
# 4. Calling a Function -- done
# 5. Arguments to Function -- done
# 6. Parameters vs Arguments -- done
# 7. Number of Arguments -- done
# 8. Arbitrary Arguments *args -- done
# 9. Keyword Arguments -- done
# 10. Arbitrary Keyword Arguments -- done
# 11. Default Parameter Value -- done
# 12. Passing a List as an Argument -- done
# 13. Return Values and Pass Statements -- done
# 14. Lambda Functions: Why and when to use? -- done
# 15. Lambda Functions: How to use? -- done


# ===============================================================================================================


# ========================================== Mastering Python: Playing with Functions =================================


# num = int(input("Enter the number"))

#
# def check_even(val):  # val is parameter
#     if val % 2 == 0:
#         print(f"The number {val} is even")
#     else:
#         print(f"The number {val} is odd")
#

# Function: Write once, call multiple times
# check_even()


# x = 53
# check_even(x)  # x is argument
# check_even(67)
# check_even(46)


#
# def greeting_bot(name, location="Canada"):
#     print(f"Hello World from {name}, I am talking from {location}")
#
#
# greeting_bot(location="India", name="Bot-101")
# greeting_bot("Bot-102", "USA")
# greeting_bot("Bot-103", "Russia")
# greeting_bot("Bot-104", "China")
# greeting_bot("Bot-105", "Australia")
# greeting_bot("Bot-007")
# #
# def find_youngest_child(**children):
#     print(f"The youngest child is {children['youngest']}")
#     print(children)
#     print(type(children))
#     # print(children)
#     # print(type(children))
#
#
# find_youngest_child(youngest="Raman", eldest="Rohan", middle="Ruhani")
#
#

# Arbitrary Arguments -=> * with parameter
# Arbitrary Keyword Arguments => ** with parameter


#
# def ages_class_10(ages):
#     print("The ages are: ", ages)
#
#
# class_list = [15, 16, 15, 14, 17]
# ages_class_10(class_list)



#
#
#
# def perimeter_circle(radius):
#     p = 2 * 3.14 * radius
#     return p
#
#
# res = perimeter_circle(5) + 20
# print("Final result value is: ", res)








# Lambda Functions
x = lambda a: a+10

print(x(45))



































































