import random


# O(N^2)
def bubbleSort(list):
    # Moves the larger elements to the back of the list
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]

    return list


# O(N log(N))
def mergeSort(list):
    # Split a list into two similar sized lists (left and right), sort each list, and then merge the sorted lists together

    # Return if the list is already sorted
    if len(list) <= 1:
        return list

    # Split the list into two halves
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    # Recursively call the mergeSort to get sorted list
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge the left and right lists
    merged = []
    i, j = 0, 0

    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# O(N log(N))
def quickSort(list):
    # Pick an item, called pivot, and move all smaller items before it and all greater items after it.
    # This is the main quick sort operation, called partition, which is recursively repeated on lesser and greater sub lists until their size is one or zero

    # Return if the list is already sorted
    if len(list) <= 1:
        return list

    # Choose the middle element as the pivot
    pivot = list[len(list) // 2]

    # Partition into less, equal and greater
    equal = []
    less = []
    greater = []

    for i in range(len(list)):
        if list[i] == pivot:
            equal.append(list[i])
        elif list[i] < pivot:
            less.append(list[i])
        else:
            greater.append(list[i])

    # Recursively sort the partitions
    less = quickSort(less)
    greater = quickSort(greater)

    # Concatenate the partitions
    result = less + equal + greater
    return result


if __name__ == "__main__":
    minimum, maximum, size = -200, 200, 25
    random.seed()
    nums = [random.randint(minimum, maximum) for num in range(size)]

    print(f"Inserted Nums: {nums}")
    print("\n")

    bubbleSortedNums = bubbleSort(nums)
    print(f"Bubble Sorted Nums: {bubbleSortedNums}")
    print("\n")

    mergeSortedNums = mergeSort(nums)
    print(f"Merge Sorted Nums: {mergeSortedNums}")
    print("\n")

    quickSortedNums = quickSort(nums)
    print(f"Quick Sorted Nums: {quickSortedNums}")
    print("\n")

    if bubbleSortedNums == mergeSortedNums and mergeSortedNums == quickSortedNums:
        print("All sorting algorithms are correct!")
    else:
        print("One or more of the sorting algorithms are not correct.")
