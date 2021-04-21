# Crypto-Team-7
Repository for the research project

### Downloading and Running
In order to properly use this program, you can download the 3 files into the same directory and run driver.py, or you can clone the entire repository, maneuver to the main directory, and then run driver.py from there.
Make sure to run it with python3!

### Execution
This program acts like a simulation of how cryptocurrency can be doled out to useful individuals who make good additions to a project. When the program is run, the user can enter integer sets (each number of the set separated by a space, and if they choose to put in multiple sets at once, each set separated by a comma), and the driver will hand them to one of the workers. When the worker finishes sorting, it will return the task as complete. The driver will check if the task was completed correctly, the worker will recieve points to add to its own "wallet", weighted based on how large or "difficult" their task was. Otherwise, the task goes up again for another attempt at solving it. By typing 'status', the user can look at the stats of each worker so far since the program ran, and if they type 'exit', the program will terminate.

### driver.py
Coded by Connor Stine, it is the main engine for the program. It takes input from the user and interprets it to send as an integer array to one of the workers. It checks the worker's work, and pays them in points if successful, or puts the task up again if it was a failure.

### goodWorkers.py //TODO
Coded by 

### badWorker.py
Coded by Dalton Miller, it handles the faulty logic of the less useful workers. Their solutions are not always correct, leading to a lack of payment for their efforts.
