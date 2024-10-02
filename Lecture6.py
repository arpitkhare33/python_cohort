# =============================== Playing with Lists ===========================


# 1. List Intro -- done
# 2. Length Command -- done
# 3. List Items - Data Types -- done
# 4. Access Specific Items -- done
# 5. Negative Indexing -- done
# 6. Extracting range from Lists -- done
# 7. Membership operator on Lists -- done
# 8. Modify Specific List Items -- done
# 9. Modify range of values from Lists -- done
# 10. Append Item in List -- done
# 11. Insert any item in between -- done
# 12. Append complete list at the end of a List -- done
# 13. Remove specific item from List -- done
# 14. Remove item from specific index -- done
# 15. Del vs Clear Methods for Lists -- done




# =================================== Lists: Learn What Matters =========================

# 1. List Intro
list1 = ['Apple', "Mango", "Orange", "Papaya", "Banana", 1, 2, True]
# len_list = len(list1)
# print(len_list)

# print(list1[-5])

# list_name[start_index: end_index+1]
# print(list1[3:9])
#

# Membership operator
# if "banana" in list1:
#     print("Fruit Found")
# else:
#     print("Get some fruit from instamart")
#

# list1[4] = "Kiwi"
# print(list1)

list1[3:5] = ["Kiwi", "Watermelon"]
# print(list1)

# append item
# print("Appending value 'India'")
list1.append("India")
# print(list1)

# print("Inserting 'IPhone' in between Kiwi and Watermelon")
list1.insert(4, "IPhone")
# print(list1)

list1.extend(["Virat", "Rohit", "Dhoni"])
print(list1)
# print(list1[10])

list1.remove("Watermelon")
print(list1)

list1.pop(4)
print(list1)


# del list1
# print(list1)

list1.clear()
print(list1)
list1.append("America")
print(list1)
