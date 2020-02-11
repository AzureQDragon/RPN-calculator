#Daniel Moon
#RPN Calculator
#2/12/20
#Postfix notation calculator
# Input: Numbers and operation specified
# Output: Result of the numbers and operations given

#Import tkinter
from tkinter import *

#Linked List node class
class LinkedListNode:
    
    # Creates one-way pointing linked list node
    def __init__(self, myData, myNext):
        #Construct a new Linked List Node
        self.data = myData
        self.next = myNext
        return

# Stack Class
class Stack:
        
    def __init__(self):
        # Construct a new LinkedList. The first node and last node are the same. Size is 0 
        self.firstNode = None
        self.lastNode = self.firstNode
        self.size = 0
        return

    # Add data to the front of the stack 
    def push(self, data):
        node = LinkedListNode(data, self.firstNode)
        self.firstNode = node
        self.size += 1
        return

    # Remove a node from the front of the list
    def pop(self):

        # Returns error if the list is empty
        if self.size == 0:
            print ("Linked List is empty")

        # Otherwise if the list has items
        else:
            currentNode = self.firstNode
            frontData = currentNode.data

            # This is the case where we have only one node in the list
            if currentNode.next == None:
                self.firstNode = None
                self.lastNode = self.firstNode
                self.size = self.size - 1

            # Otherwise remove from the front
            else:
                currentNode = currentNode.next
                self.firstNode = currentNode
                self.size = self.size - 1

        # Return First item that is removed
        return frontData

# --------------------------------- Start Calculator Code ------------------------------------

# Enters a value into memory
def enter():
    string = ""

    # Handles case in which operations are chained with items in memory
    if(buffervalues.size > 0):
        for i in range(buffervalues.size):
            string += buffervalues.pop() # Appends values to create one number
        values.push(string)
        text.set("")

# Store value of a resulting operation 
def storeValue():
    valuecopy = values
    value = valuecopy.pop()
    store.push(value)

# Recall value found within the storage
def recallValue():
    value = store.pop()
    pushValue(value)
    enter()
    text.set(value)

# Pushes values to the buffer stack
def pushValue(value):
    
    #Checks to see if the buffer
    if(buffervalues.size == 0):
        resetBuffer()
    if(not value == ""):
        buffervalues.push(value)
        text.set(text.get() + value)

# Performs calculations with the specified operand
def calculate(operand):

    enter() # First enter the value that is placed before the operand

    # Checks to see if a valid operation can be made
    if(values.size >= 2):

        # Calculates sum
        if(operand == "+"):

            # Stores each of the 2 values into a variable
            first = eval(values.pop())
            second = eval(values.pop())
            sumVal = str(first+second) # Performs operation

            # Push values to stack
            pushValue(sumVal)
            enter()
            text.set(sumVal)

        # Calculates difference
        if(operand == "-"):
            first = eval(values.pop())
            second = eval(values.pop())
            difVal = str(second-first)
            buffervalues.push(difVal)
            enter()
            text.set(difVal)
        
        # Calculates product
        if(operand == "×"):
            first = eval(values.pop())
            second = eval(values.pop())
            proVal = str(first*second)
            buffervalues.push(proVal)
            enter()
            text.set(proVal)
        
        # Calculates quotient
        if(operand == "÷"):
            first = eval(values.pop())
            second = eval(values.pop())

            # Checks to see if division by zero occurs
            if(first != 0):
                quoVal = str(second/first)
                buffervalues.push(quoVal)
                enter()
                text.set(quoVal)
            
            # In the case of division by zero
            else:
                invalidOp()
    else:
        invalidOp()

# Called whenever there is an invalid operation
def invalidOp():
    resetMemory()
    text.set("Invalid operation")

# Clears the buffer stack
def resetBuffer():
    text.set("")
    for i in range(buffervalues.size):
        buffervalues.pop()
    return

# Resets the memory of the buffer, values, and store stacks
def resetMemory():
    text.set("")
    resetBuffer()
    for i in range(values.size):
        values.pop()
    if(store.size >= 1):
        store.pop()
    return

# Storage stacks
buffervalues = Stack() # Temporarily stores values as they are copied to values
values = Stack()       # Stores the actual values of the operations
store = Stack()        # Stores the value of item in the storage

# --------------------------------- End Calculator Code ----------------------------------------

# --------------------------------- Start Tkinter Code -----------------------------------------

# Initialize window and frame
window = Tk()
frame1 = window.frame()

# Variable to store text on screen
text = StringVar()

# Utility buttons
EnterButton = Button(window, text="Enter", command = enter) # Connects to the enter function
ClearEntry = Button(window, text="CLX", command = resetBuffer) # Resets the buffer stack
Clear = Button(window, text="CLR", command = resetMemory) # Resets the entirety of the values and buffer stack
Store = Button(window, text="STO", command = storeValue) # Store function
Recall = Button(window, text="RCL", command = recallValue) # Recall function
CalcScreen = Entry(window, textvariable = text, state=DISABLED)

# Number buttons send a specific number through lambda to the pushValue function
num0 = Button(window, text = "0", command = lambda:pushValue("0"))
num1 = Button(window, text = "1", command = lambda:pushValue("1"))
num2 = Button(window, text = "2", command = lambda:pushValue("2"))
num3 = Button(window, text = "3", command = lambda:pushValue("3"))
num4 = Button(window, text = "4", command = lambda:pushValue("4"))
num5 = Button(window, text = "5", command = lambda:pushValue("5"))
num6 = Button(window, text = "6", command = lambda:pushValue("6"))
num7 = Button(window, text = "7", command = lambda:pushValue("7"))
num8 = Button(window, text = "8", command = lambda:pushValue("8"))
num9 = Button(window, text = "9", command = lambda:pushValue("9"))

# Operation buttons are linked to the calculate function through lambda
add = Button(window, text = "+", command = lambda: calculate("+"))
sub = Button(window, text = "-", command = lambda: calculate("-"))
mult = Button(window, text = "×", command = lambda: calculate("×"))
div = Button(window, text = "÷", command = lambda: calculate("÷"))

# Grid screen 
CalcScreen.grid(row = 0, column = 1,columnspan=3)

# Grid operation buttons
add.grid(row = 1, column = 0, padx=5, pady=5)
sub.grid(row = 2, column = 0, padx=5, pady=5)
mult.grid(row = 3, column = 0, padx=5, pady=5)
div.grid(row = 4, column = 0, padx=5, pady=5)

# Grid utility buttons
EnterButton.grid(row = 5, column = 1, padx=5, pady=5)
Clear.grid(row=1, column = 2, padx=5, pady=5)
ClearEntry.grid(row=1, column = 3, padx=5, pady=5)
Store.grid(row =5, column =2, padx=5, pady=5)
Recall.grid(row=5, column = 3, padx=5, pady=5)

# Grid the numbers on the calculator
num0.grid(row = 1, column = 1, padx=5, pady=5)
num1.grid(row = 2, column = 2, padx=5, pady=5)
num2.grid(row = 2, column = 3, padx=5, pady=5)
num3.grid(row = 2, column = 1, padx=5, pady=5)
num4.grid(row = 3, column = 2, padx=5, pady=5)
num5.grid(row = 3, column = 3, padx=5, pady=5)
num6.grid(row = 3, column = 1, padx=5, pady=5)
num7.grid(row = 4, column = 2, padx=5, pady=5)
num8.grid(row = 4, column = 3, padx=5, pady=5)
num9.grid(row = 4, column = 1, padx=5, pady=5)

window.mainloop() # Mainloop call
# --------------------------------- End Tkinter Code -----------------------------------------
