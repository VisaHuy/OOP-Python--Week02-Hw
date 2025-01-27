#Create a list
myList = []
for x in range(21):
    if x % 2 == 0:
        myList.append(x)
print(myList)
#Create a square list using List Comprehension
newList = [x ** 2 for x in myList] #x ** 2 mean x X x
print(newList)