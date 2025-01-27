#Write the reverse function for the list
def reverseList(inputList):
    if len(inputList) > 0:
        print("After Reverse: ", inputList[::-1]) #Print the reverse value in the list
    else:
        print("List is Empty!!")
#Create a list
myList = [1, 2, 3, 4, 5]
print("Before Reverse:", myList)
reverseList(myList)