# ================================================= Dictionaries in Python ============================================

# 1. Dictionaries: Intro -- done
# 2. Need of Dictionary -- done
# 3. Creating Dictionary -- done
# 4. Dictionary : Data Types -- done
# 5. Dictionary Properties: Ordered, Changeable, Unique -- done
# 6. Length of Dictionary -- done
# 7. Access Items in Dictionary: Multiple ways -- done
# Bonus: Comparison Operator -- done
# 8. Modify Items in Dictionary -- done
# 9. Adding Items in Dictionary -- done
# 10. Benefit of using the update() command -- done
# 11. Remove Items from Dictionary: Multiple ways -- done
# 12. Clearing a Dictionary -- done
# 13. Creating a copy of Dictionary: copy() and dict() -- done
# 14. Nested Dictionary -- done
# 15. Loop through Dictionary -- done



# ========================================== Mastering Dictionaries: Learn What Matters ===============================


# Word - aajafajfa, fafhsjfdsjh
# Key - Value

orders = ["Dosa", "Paneer", "Rajma", "Chola", "Burger", "Pizza", "Vada Pao", "Samosa",
          "Chinese", "Momos",
          "Chicken Biryani", "Chicken Tandoori"]

order_dict = {"Aman": ["Dosa", "tea"], "Bharat": "Rajma", "Chandan": "Paneer",
              "TableNo": 14, "DeliveryStatus": False}
# print(order_dict['Aman'])
# print(order_dict['Bharat'])
# print(order_dict['TableNo'])
# print(order_dict['DeliveryStatus'])
#
#
# print("Delivered Order for Table ", order_dict['TableNo'])
# order_dict['DeliveryStatus'] = True
# print(order_dict['DeliveryStatus'])
#
#
# print("Length of dictionary:", len(order_dict))


# table_bharat = order_dict.get("Bharat")
# print(order_dict.keys())
#
#
# print(order_dict.values())
#
#


# if "Aman" in order_dict:
#     print("Take the contri from him also")
# else:
#     print("Don't take the contri from him")



# Modify Dictionaries

# order_dict['Aman'] = "kabab"
# order_dict.update({"Aman": "Kabab"})
# print(order_dict)
#

# order_dict['Rahul'] = "Tea"
order_dict.update({"Rahul": "tea"})


order_dict.pop("Rahul")

del order_dict['TableNo']
# order_dict.clear()

table_2 = order_dict.copy()
table_2['Bharat'] = "Mushroom"
# table_2['Nisha'] = ['Dosa', 'tea']



# print("Table 1: ", order_dict)
# print("Table 2: ", table_2)


















student = {'Name': {"FirstName": "Arpit", "LastName": "Khare"}, "Age": 60, "Mob": 987654310}
# print(student)

# print(student['Name']['LastName'])




#
# for o in order_dict:
#     print(o)
#
#
# for order in order_dict:
#     print(order_dict[order])


# for x in order_dict.values():
#     print(x)
#
#
#

for value in student.values():
    for val in value:
        print(val)
    print(value)





