#CECS 228 Project Code
#Contributors: Linda Trinh, Hanson Nguyen, Bryan Vu, Jessica Wei

#Gets the two numbers in the range of the array to be compared
def part(idArray, low, high):
    index = (low - 1)
    pivot = idArray[high]

    for z in range(low, high):
        #if a number from the higher index is less than or equal to the pivot point
        if idArray[z] <= pivot:
            index = index + 1
            #then swap the number with the number one index greater than the index last swapped
            idArray[index],idArray[z] = idArray[z],idArray[index]
            
    #swap the next index with the highest index within the range
    idArray[index + 1],idArray[high] = idArray[high],idArray[index + 1]
    #returns the next index to be evaluated
    return(index+1)

#Performs the overall sort with recursion 
def quickSort(idArray, low, high):
    #if the lower index is greater than the higher index
    if low < high:
        #Start comparing and/or sorting the indicies within the range
        partition = part(idArray, low, high)
        #Sorts the array between the low index to the next position to be evaluated
        quickSort(idArray, low, partition - 1)
        #Sorts the array between the next position to be evaluated to the high index
        quickSort(idArray, partition + 1, high)


import random

studentDict = {321: "Linda Trinh", 123: "Hanson Nguyen", 231: "Bryan Vu", 213: "Jessica Wei"}
idArray = []

print("TEST 1 - 4 STUDENTS")
unsortedList = "Unsorted Students\n"

for x in studentDict:
    idArray.append(x)
    unsortedList = unsortedList + " " + str(x) + ": " + studentDict[x] + "\n"

print(unsortedList)

length = len(idArray)
quickSort(idArray, 0, (length - 1))

sortedList = "Sorted Students by ID:\n";
for x in idArray:
    sortedList = sortedList + " " + str(x) + ": "+ studentDict[x] + "\n"

print(sortedList)
################################################################################################
studentDict.clear();
idArray.clear();

print("TEST 2 - 10 STUDENTS")
unsortedList = "Unsorted Students\n"

count = 0
while count < 10:
    rID = random.randint(100,999)
    check = 0
    while check < len(idArray):
        if idArray[check] == rID:
            rID = random.randint(100,999)
            check = 0
        else:
            check = check + 1
    idArray.append(rID)
    studentDict[rID] = "Student " + str(count + 1)
    count = count + 1

for x in studentDict:
    unsortedList = unsortedList + " " + str(x) + ": " + studentDict[x] + "\n"

print(unsortedList)

length = len(idArray)
quickSort(idArray, 0, (length - 1))

sortedList = "Sorted Students by ID:\n";
for x in idArray:
    sortedList = sortedList + " " + str(x) + ": "+ studentDict[x] + "\n"

print(sortedList)
################################################################################################
studentDict.clear();
idArray.clear();

print("TEST 3 - 20 STUDENTS")
unsortedList = "Unsorted Students\n"

count = 0
while count < 20:
    rID = random.randint(100,999)
    check = 0
    while check < len(idArray):
        if idArray[check] == rID:
            rID = random.randint(100,999)
            check = 0
        else:
            check = check + 1
    idArray.append(rID)
    studentDict[rID] = "Student " + str(count + 1)
    count = count + 1

for x in studentDict:
    unsortedList = unsortedList + " " + str(x) + ": " + studentDict[x] + "\n"

print(unsortedList)

length = len(idArray)
quickSort(idArray, 0, (length - 1))

sortedList = "Sorted Students by ID:\n";
for x in idArray:
    sortedList = sortedList + " " + str(x) + ": "+ studentDict[x] + "\n"

print(sortedList)



