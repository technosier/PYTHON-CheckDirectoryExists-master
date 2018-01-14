#Coded by | lucifer
#https://github.com/technosier
#Import the OS module
import os
CheckDir = raw_input("Enter the name of the directory to check : ")
print
if os.path.exists(CheckDir):#Checks if the dir exists
	print "The directory exists"
else:
	print "No directory found for "+CheckDir #Output if no directory
	print
	os.makedirs(CheckDir)#Creates a new dir for the given name
	print "Directory created for "+CheckDir
