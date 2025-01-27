#Create a funtion for merging the list
def mergeList(myList1, myList2):
    if len(myList1) <= 0:
        print(myList2)
    elif len(myList2) <= 0:
        print(myList1)
    else:
        for x in myList2:
            if x not in myList1:
                myList1.append(x)
        print(myList1)
#Create two list
myList1 = [1, 2, 3]
myList2 = [2, 3, 4, 5]
mergeList(myList1, myList2)