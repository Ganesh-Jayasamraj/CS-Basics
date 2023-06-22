# Files I/O

# input

# str = input("Enter anything :")
# print (str)

# open function
# fo = open("new_file.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)
# print ("Softspace flag : ", fo.softspace)
# fo.close()          # Close Function

fo = open("new_file.txt", "w")
fo.write("Something that will be writen on text")       # Write Function
fo.close()

fo = open("new_file.txt", "r+")
print(fo.read())                                        # Read Function
fo.close()

# Renaming and deleting Files
import os
os.rename("new_file.txt", "Ultra_new_file.txt")
os.remove("Ultra_new_file.txt")

# Making New directory
os.mkdir("newdir")

# Removing Directorty
os.rmdir("newdir")