# ======================================= Tuples in Python ===================================

# 1. Tuples: Intro -- done
# 2. Creating Tuples -- done
# 3. Need of Tuples -- done
# 4. Length of Tuples -- done
# 5. Tuple Items: Data Types -- done
# 6. Access Specific Items -- done
# 7. Negative Indexing -- done
# 8. Access Range of Items -- done
# 9. Membership operator on Tuples -- done
# 10. Modify Tuple Values -- done
# 11. Tuple Properties: Ordered, Unchangeable, Allow Duplicates -- done
# 12. Append Items to Tuples -- done
# 13. Remove Items from Tuples -- done
# 14. Delete the Tuple -- done
# 15. Unpacking Tuples -- done
# 16. Unpacking Tuples with Asterisk * -- done
# 17. Join Tuples -- done


# ========================================== Playing with Tuples: Learn what matters ===============================

#
# my_tup = ("Apple", "Mango", "Banana", 123, True, False, False)
# print(my_tup)
# print(type(my_tup))
# print(my_tup)
# print(my_tup)
# print(len(my_tup))
# print(my_tup[1])

# couple = ("Rohan", "Rakul")
# guy = "Bastard"
# # Black magic person
# couple[0]= guy

# print(couple)
# print(my_tup[starting_index:ending_index+1])
# print(my_tup[1:3+1])
#
# if "banana" in my_tup:
#     print("Fruit is present")
# else:
#     print("Get some fruits bro.")
# temp = list(my_tup)
# # print(temp)
# temp[1] = "Kiwi"
# temp.append("Watermelon")
# # print(temp)
# # print(my_tup)
# my_tup = tuple(temp)
# print(my_tup)
#
#
# x = (1, 2, 3)
# a, b, c = x
# print(a)
# print(b)
# print(c)
#
#


# fruit1, fruit2, fruit3, *temp = my_tup
#
# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(temp)




my_tup = ("Apple", "Mango", "Banana", 123, True, False, False)
second_tup = ("India", "Australia")

res_tup = my_tup + second_tup
print(res_tup)