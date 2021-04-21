"""goodWorker(workerID=0, currency=0, totalTasks=0, correctTasks=0, numListList=[])
PURPOSE:
    The goodWorker class is a worker class that has a queue of int lists
    given to it thru the method addTask and sorts a task when the 
    sort method is called. FIFO methodology.
PARAMETERS/VARIABLES:
    - int workerID - idenctification number for the object
    - int currency - the 'wallet' of the object
    - int totalTasks - count of total tasks added to queue
    - int correctTasks - count of tasks correctly performed
    - int numListList - list of int lists to be sorted, a queue of int lists.
RELEVANT METHODS:
    - sort() - sorts the next int list in queue.         
    - addTask(intList) - adds a list of ints to the queue of tasks for this obj
        ex: addTask([4, 2, 1, 3])
    - getX() - returns the corresponding variable, replace 'X' with the desired
        variable ex: getWorkerID() returns the workerID. Methods are always camelCase
        ex: getCurrency(), getTotalTasks()
    - setX(x) - Sets the obj's x variable to the given value, where x is any given
        variable ex: setCurrency(100) sets currency var to 100. Always camelCase
"""
class goodWorker:
    #Constructor
    def __init__(self, workerID=0, currency=0, totalTasks=0, correctTasks=0, numListList=[]):
        self.workerID = workerID
        self.currency = currency
        self.totalTasks = totalTasks
        self.correctTasks = correctTasks
        self.numListList = numListList
    
    #Sort the 0th int list in numListList queue at 100% accuracy
    def chanceSort(self):
        try:
            return self.goodSort(self.numListList.pop(0))
        except IndexError:
            raise IndexError("ID#" + str(self.workerID) + " cannot sort, no tasks!")
    
    #Sort the intList para correctly
    def goodSort(self, intList):
        #print("goodsorting: ", intList)
        self.correctTasks += 1
        intList.sort()
        return intList
    
    #Append an int list to the task list
    def addTask(self, intList):
        for element in intList:
            if not type(element) is int:
                raise TypeError("ERROR: List contains NON-INT: " + str(element))
        self.numListList.append(intList)
        self.totalTasks += 1
        
    #Getter methods
    def getID(self):
        return self.workerID
    def getCurrency(self):
        return self.currency
    def getTotalTasks(self):
        return self.totalTasks
    def getCorrectTasks(self):
        return self.correctTasks
    def getNumListList(self):
        return self.numListList
    #Setter methods
    def setID(self, workerID):
        self.workerID = workerID
    def setCurrency(self, currency):
        self.currency = currency
    def setTotalTasks(self, totalTasks):
        self.totalTasks = totalTasks
    def setCorrectTasks(self, correctTasks):
        self.correctTasks = correctTasks
    def setNumListList(self, numListList):
        self.numListList = numListList
    
