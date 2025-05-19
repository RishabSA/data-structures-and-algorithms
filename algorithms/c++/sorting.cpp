#include <iostream>
#include <vector>
#include <random>

// O(N^2)
template<typename T>
std::vector<T> bubbleSort(std::vector<T> list) {
    // Moves the larger elements to the back of the list
    for (int i = 0; i < list.size(); i++) {
        for (int j = 0; j < list.size(); j++) {
            if (list[i] < list[j]) {
                std::swap(list[i], list[j]);
            }
        }
    }

    return list;
}

// O(N log(N))
template<typename T>
std::vector<T> mergeSort(std::vector<T> list) {
    // Split a list into two similar sized lists (left and right), sort each list, and then merge the sorted lists together

    // Return if the list is already sorted
    if (list.size() <= 1) {
        return list;
    }

    // Split the list into two halves
    int middle = list.size() / 2;
    std::vector<T> left(list.begin(), list.begin() + middle);
    std::vector<T> right(list.begin() + middle, list.end());

    // Recursively call the mergeSort to get sorted list
    left = mergeSort(left);
    right = mergeSort(right);

    // Merge the left and right lists
    std::vector<T> merged;
    int i = 0, j = 0;

    // Merge elements in sorted order
    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            merged.push_back(left[i++]);
        } else {
            merged.push_back(right[j++]);
        }
    }

    // Append remaining elements
    while (i < left.size()) merged.push_back(left[i++]);
    while (j < right.size()) merged.push_back(right[j++]);

    return merged;
}

// O(N log(N))
template<typename T>
std::vector<T> quickSort(std::vector<T> list) {
    // Pick an item, called pivot, and move all smaller items before it and all greater items after it. 
    // This is the main quick sort operation, called partition, which is recursively repeated on lesser and greater sub lists until their size is one or zero

    // Return if the list is already sorted
    if (list.size() <= 1) {
        return list;
    }

    // Choose the middle element as the pivot
    T pivot = list[list.size() / 2];

    // Partition into less, equal and greater
    std::vector<T> equal;
    std::vector<T> less;
    std::vector<T> greater;

    for (int i = 0; i < list.size(); i++) {
        if (list[i] == pivot) {
            equal.push_back(list[i]);
        } else if (list[i] < pivot) {
            less.push_back(list[i]);
        } else {
            greater.push_back(list[i]);
        }
    }

    // Recursively sort the partitions
    less = quickSort(less);
    greater = quickSort(greater);

    // Concatenate the partitions
    std::vector<T> result;
    result.insert(result.end(), less.begin(), less.end());
    result.insert(result.end(), equal.begin(), equal.end());
    result.insert(result.end(), greater.begin(), greater.end());

    return result;
}

// O(N^2)
template<typename T>
std::vector<T> insertionSort(std::vector<T> list) {
    int unsorted = 1;

    while (unsorted < list.size()) {
        T hold = list[unsorted];
        int i = unsorted - 1;
        while (i >= 0 && hold < list[i]) {
            list[i + 1] = list[i];
            i--;
        }
        list[i + 1] = hold;
        unsorted++;
    }

    return list;
}

int main() {
    // Define the range
    int min = -200;
    int max = 200;
    int size = 25;
    std::vector<int> nums;

    // Seed the random number generator
    std::random_device rd;
    std::mt19937 gen(rd());

    // Define the distribution
    std::uniform_int_distribution<> distrib(min, max);

    std::cout << "Inserted Nums: ";
    for (int i = 0; i < size; i++) {
        nums.insert(nums.begin() + i, distrib(gen));
        std::cout << nums[i] << " ";
    }
    std::cout << "\n\n";

    std::vector<int> bubbleSortedNums = bubbleSort(nums);

    std::cout << "Bubble Sorted Nums: ";
    for (int num : bubbleSortedNums) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    std::vector<int> mergeSortedNums = mergeSort(nums);

    std::cout << "Merge Sorted Nums: ";
    for (int num : mergeSortedNums) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    std::vector<int> quickSortedNums = quickSort(nums);

    std::cout << "Quick Sorted Nums: ";
    for (int num : quickSortedNums) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    std::vector<int> insertionSortedNums = insertionSort(nums);

    std::cout << "Insertion Sorted Nums: ";
    for (int num : insertionSortedNums) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    return 0;
}