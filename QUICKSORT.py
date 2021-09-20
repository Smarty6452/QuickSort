import random
# This function takes first element as pivot
# partition logicfor  first element as pivot
def partition1(array, start, end):  
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
    array[start], array[high] = array[high], array[start]
    return high


# This function takes mid element as pivot
def partition2(array, start, end):
    array[start], array[int((start + end) / 2)] = array[int((start + end) / 2)], array[start]
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# This function takes random element as pivot
def partition3(arr,low,high):
    p = random.randint(low,high)
    arr[high],arr[p] = arr[p],arr[high]

    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot at last position
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# This function takes last element as pivot
def partition4(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot at last position
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Quick sort function for last element as pivot
def quick_sort4(arr, low, high):
    if low < high:
        pi = partition4(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort4(arr, low, pi - 1)
        quick_sort4(arr, pi + 1, high)

# Quick sort function for random element as pivot
def quick_sort3(input_array,l,r):
    if l>=r: 
        return
    
    p = partition3(input_array,l,r)
    quick_sort3(input_array,l,p-1)
    quick_sort3(input_array,p+1,r)

# Quick sort function for middle element as pivot
def quick_sort2(array, start, end):
    if start >= end:
        return
    p = partition2(array, start, end)
    quick_sort2(array, start, p - 1)
    quick_sort2(array, p + 1, end)

# Quick sort function for first element as pivot
def quick_sort1(array, start, end):
    if start >= end:
        return
    p = partition1(array, start, end)
    quick_sort1(array, start, p - 1)
    quick_sort1(array, p + 1, end)

# Main
array = []
n = int(input("Enter no elements "))

for i in range(0, n):
    ele = int(input("Enter the "+str(i+1)+" no: "))
    array.append(ele)

chi = 'y'
while chi == 'y':
    print("==================================================================")
    choice = int(input("Enter Options for Quicksort\n1: Pivot at starting\n2: Pivot at Middle\n3: Pivot at Random position\n4: Pivot at last\n"))

    if choice == 1:
        quick_sort1(array, 0, len(array) - 1)
        print("Sorted array is ")
        print(array)
        print(array)
    elif choice == 2:
        quick_sort2(array, 0, len(array) - 1)
        print("Sorted array is ")
        print(array)
    elif choice == 3:
        quick_sort3(array, 0, n - 1)
        print("Sorted array is ")
        print(array)
    elif choice == 4:
        quick_sort4(array, 0, len(array) - 1)
        print("Sorted array is ")
        print(array)
    else:
        print("Error")
    chi = input("Do you want to continue?(y/n)")