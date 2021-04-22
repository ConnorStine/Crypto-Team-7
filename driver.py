# driver.py coded by Connor Stine
# imports
import time
import random
import badWorker as BAD
import goodWorker as GOOD

looping = True
# Initial header
print("INITIALIZED DRIVER.PY\nYou have 3 options:\n    'exit' - by typing this keyword, you will terminate the program."
			,"\n    'status' - by typing this keyword, you will list the status of all the workers."
			,"\n    Or type an integer set separated by spaces. You may also send multiple sets"
			,"\n    at once by separating sets with commas, i.e.:"
			,"\n        1 2 3 4, 5 6, 7 8 9, 3 8 0, 23 3 8 39 923")
			
# Create Workers
workers = []
badWorker1 = BAD.badWorker()
badWorker1.setID(1)
workers.append(badWorker1)
badWorker2 = BAD.badWorker()
badWorker2.setID(2)
workers.append(badWorker2)
goodWorker1 = GOOD.goodWorker()
goodWorker1.setID(3)
workers.append(goodWorker1)
goodWorker2 = GOOD.goodWorker()
goodWorker2.setID(4)
workers.append(goodWorker2)
goodWorker3 = GOOD.goodWorker()
goodWorker3.setID(5)
workers.append(goodWorker3)

# Loop until exit
while looping:
	userIn = input("Please enter your chosen input: ")
	if userIn == "exit": # Exit signal received
		print("Exit signal received, goodbye!")
		time.sleep(1)
		looping = False
	elif userIn == "status": # Get the status of every worker
		print("\nCURRENT STATUS OF ALL WORKERS:\n")
		for w in workers:
			print("Worker {}:".format(w.getID()))
			if w.getID() > 2:
				print("< GOOD WORKER >")
			else:
				print("< BAD WORKER >")
			print("    Total Tasks Claimed:    ", w.getTotalTasks())
			print("    Total Successful Tasks: ", w.getCorrectTasks())
			print("    Total Currency Gained:  ", w.getCurrency())
			print("") # skip a line
	else: # This should be a/an int List(s)
		if userIn == "": # Clarity spacing if people want it
			continue
		try:
			sets = userIn.split(',') # Split input up by commas just in case
			for item in sets:
				set = item.split()
				set = list(map(int, set)) # Make sure all items are numbers in the List
				oSet = []
				for number in set: # Copy original set
					oSet.append(number)
				
				# Begin handling all sets
				sorting = True
				while sorting:
					print("\nPutting set", oSet, "up for sorting.")
					time.sleep(random.uniform(0.1, 0.8)) # Random sleep to facilitate visibility and randomness
					rand = random.randint(0,4) # Pick a worker
					print("Task taken by worker", rand + 1)
					workers[rand].addTask(set)
					rSet = workers[rand].chanceSort()
					time.sleep(0.5)	# "task time"
					print("Set sorted by Worker {}: {}".format(rand + 1, rSet))
					# If sorted, continue on, if not, put it up again
					if all(rSet[i] <= rSet[i+1] for i in range(len(rSet)-1)):
						print("Set correctly sorted! Currency paid.\n_\n")
						workers[rand].setCurrency(workers[rand].getCurrency() + len(rSet))
						sorting = False
					else:
						print("Set incorrectly sorted! No currency paid.")
		except ValueError:
			print("Sorry, a set could not be properly interpreted, please try again!")
