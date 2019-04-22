#CECS 228 Project Code
#Contributors: Linda Trinh, Hanson Nguyen, Bryan Vu, Jessica Wei

def part(idArr, low, high):
    i = (low - 1)
    piv = idArr[high]

    for z in range(low, high):
        if idArr[z] <= piv:
            i = i + 1
            idArr[i],idArr[z] = idArr[z],idArr[i]

    idArr[i + 1],idArr[high] = idArr[high],idArr[i + 1]
    return(i+1)

def quickSort(idArr, low, high):
    if low < high:
        p1 = part(idArr, low, high)
        quickSort(idArr, low, p1 - 1)
        quickSort(idArr, p1 + 1, high)


studentDict = {321: "Linda Trinh", 123: "Hanson Nguyen", 231: "Bryan Vu", 213: "Jessica Wei"}
print("Unsorted Students by ID: ", studentDict) 
idArray = []
for x in studentDict:
    idArray.append(x)

length = len(idArray)
quickSort(idArray, 0, (length - 1))

last = idArray[length - 1]

sortedList = "Sorted Students by ID:";
for x in idArray:
    sortedList = sortedList + " " + str(x) + ": "+ studentDict[x]
    if x != last:
        sortedList = sortedList + ","

print(sortedList)
