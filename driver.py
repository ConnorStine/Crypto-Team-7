# driver.py coded by Connor Stine
# imports
import time
import random

looping = True
# Initial header
print("INITIALIZED DRIVER.PY\nYou have 3 options:\n    'exit' - by typing this keyword, you will terminate the program."
			,"\n    'status' - by typing this keyword, you will list the status of all the workers."
			,"\n    Or type an integer set separated by spaces. You may also send multiple sets"
			,"\n    at once by separating sets with commas, i.e.:"
			,"\n        1 2 3 4, 5 6, 7 8 9, 3 8 0, 23 3 8 39 923")
# Loop until exit
while looping:
	userIn = input("Please enter your chosen input: ")
	if userIn == "exit":
		print("Exit signal received, goodbye!")
		time.sleep(1)
		looping = False
	elif userIn == "status":
		print("TODO")
	else:
		if userIn == "": 	# Clarity spacing if people want it
			continue
		try:
			sets = userIn.split(',')	# Split input up by commas just in case
			for item in sets:
				set = item.split()
				for number in set:
					number = int(number)	# Make sure all items are numbers in the List
				print(random.randint(1,5))	# Choose a random worker
				# TODO
				
		except ValueError:
			print("Sorry, a set could not be properly interpreted, please try again!")
