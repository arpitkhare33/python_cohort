# ============================= Exception Handling and File Handling ==================================================
import os.path

# 1. Exception Handling : Intro -- done
# 2. Need of Exception Handling -- done
# 3. Else block with Exception Handling -- done
# 4. Finally block with Exception Handling -- done
# 5. Raising an Exception -- done
# 6. File Handling: Intro -- done
# 7. Reading a File -- done
# 8. Reading only parts of the File -- done
# 9. Read Single Line from File -- done
# 10. Loop through lines of the File -- done
# 11. Writing something on a File -- done
# 12. Appending something on a File -- done
# 13. Closing a File -- done
# 14. Check if a File Exists -- done
# 15. Deleting a File, Folder -- done


# ====================================================================================================================


# ======================================== Exception Handling & File Handling ==========================================

#
# i = 1
# try:
#     while i < 49:
#         if 49 % i == 0:
#             print("The number dividing 49 is : ", i)
#
#         i = i + 1
# except Exception as ex:
#     print(ex)
# finally:
#     print("The execution terminated.")
#




# age = int(input("Enter your age: "))
#
# if age <=0:
#     raise Exception("Please enter a value greater than 0")




# file = open("demo_file.txt", "r")

# # print(file.readline())
#
# for item in file:
#     print(f"Hey, My name is {item}")



# ================================= Writing on a file ===========================
# 1. Open the file in a desired mode.
# 2. Perform the operation

# fw = open("demo_file2.txt", "a")
# fw.write("\n Hello everyone, everything is vanished.")
#
#
# fw.close()

# if os.path.exists("demo_file.txt"):
#     print("File is present")
#     os.remove("demo_file.txt")
# else:
#     print("File is not present")
#
#
#


os.rmdir("temp")







































