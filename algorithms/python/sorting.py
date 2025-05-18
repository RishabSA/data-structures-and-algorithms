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
