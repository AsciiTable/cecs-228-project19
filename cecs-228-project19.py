#CECS 228 Project Code
#Contributors: Linda Trinh, Hanson Nguyen, Bryan Vu, Jessica Wei

#Gets the two numbers in the range of the array to be compared
def part(idArr, low, high):
    i = (low - 1)
    piv = idArr[high]

    for z in range(low, high):
        #if a number from the higher index is less than or equal to the pivot point
        if idArr[z] <= piv:
            i = i + 1
            #then swap the number with the number one index greater than the index last swapped
            idArr[i],idArr[z] = idArr[z],idArr[i]
            
    #swap the next index with the highest index within the range
    idArr[i + 1],idArr[high] = idArr[high],idArr[i + 1]
    #returns the next index to be evaluated
    return(i+1)

#Performs the overall sort with recursion 
def quickSort(idArr, low, high):
    #if the lower index is greater than the higher index
    if low < high:
        #Start comparing and/or sorting the indicies within the range
        p1 = part(idArr, low, high)
        #Sorts the array between the low index to the next position to be evaluated
        quickSort(idArr, low, p1 - 1)
        #Sorts the array between the next position to be evaluated to the high index
        quickSort(idArr, p1 + 1, high)


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



