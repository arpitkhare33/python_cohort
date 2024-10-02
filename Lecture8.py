# ====================================== Sets in Python ==========================================

# 1. Sets: Intro -- done
# 2. Creating Sets -- done
# 3. Need of Sets -- done
# 4. Set Properties: Unordered, Unchangeable, Unique -- done
# 5. Length of a Set -- done
# 6. Set Items: Data Types -- done
# 7. Access Specific Items -- done
# 8. Change Set Items -- done
# 9. Add Single Item in Sets -- done
# 10. Add Multiple Items in Sets -- done
# 11. Removing Existing Item from Sets -- done
# 12. remove() vs discard() -- done
# 13. Emptying a Set -- done
# 14. clear() vs del() -- done
# 15. Join Sets - IMP -- done
# BONUS TOPIC: Union() vs update() -- done

# =================================================================================================


# ===================================== Playing with Sets - Learn What Matters ========================================



# print(my_set)
# my_set.add("Orange")
# temp_set = {"India", "Aussie"}
# my_set.update(temp_set)  # similar to extend in List
# print(my_set)
# my_set.remove("Aussie")
#
#
#
# my_set.discard("Aussie")
# print(my_set)






# my_set = {1, 2, 3, 3, 2, 1, "Welcome"}
# del my_set
# print(my_set)
# print(len(my_set))
#
# # UNION, UPDATE
# A = {1, 2, 3}
# B = {4, 5, 6}
# C = A.union(B)
# # C = A.update(B)
# print(A)
# print(B)
# print(C)
#
# print("Now comes update()")
# C = A.update(B)
# print(A)
# print(B)
# print(C)

# Intersection
A = {1, 2, 3}
B = {4, 5, 6, 3}
# C = A.intersection(B)
# print(A)
# print(B)
# print(C)
#
# C= A.difference(B) # A- B
# print(C)
#
# C= A.union(B)
# print(C)


# Symmetric Difference
print(A)
print(B)
C = A.symmetric_difference(B)
print(C)
