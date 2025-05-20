# O(N)
def seqSearch(list, val):
    # Loop through the list and check every item
    for i in range(len(list)):
        if list[i] == val:
            return i

    return -1


# O(log(N))
def binarySearch(list, val):
    mid = 0
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == val:
            return mid
        elif list[mid] < val:
            low = mid + 1
        elif list[mid] > val:
            high = mid - 1

    return -1


if __name__ == "__main__":
    nums = [0, 1, 3, 5, 6, 7, 9, 10, 34, 50]

    seqSearchIdx = seqSearch(nums, 10)
    print(f"Sequential Search found 10 at index: {seqSearchIdx}")

    binarySearchIdx = binarySearch(nums, 10)
    print(f"Binary Search found 10 at index: {binarySearchIdx}")
