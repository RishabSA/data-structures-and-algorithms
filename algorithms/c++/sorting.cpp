#include <iostream>
#include <vector>
#include <random>

// O(N^2)
std::vector<int> bubbleSort(std::vector<int> list) {
    // Moves the larger elements to the back of the list
    for (int i = 0; i < list.size() - 1; i++) {
        for (int j = 0; j < list.size() - 1; j++) {
            if (list[i] < list[j]) {
                std::swap(list[i], list[j]);
            }
        }
    }

    return list;
}

// O(N log(N))
std::vector<int> mergeSort(std::vector<int> list) {
    // Split a list into two similar sized lists (left and right), sort each list, and then merge the sorted lists together

    // Return if the list is already sorted
    if (list.size() <= 1) {
        return list;
    }

    // Split the list into two halves
    int middle = list.size() / 2;
    std::vector<int> left(list.begin(), list.begin() + middle);
    std::vector<int> right(list.begin() + middle, list.end());

    // Recursively call the mergeSort to get sorted list
    left = mergeSort(left);
    right = mergeSort(right);

    // Merge the left and right lists
    std::vector<int> merged;
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

    return 0;
}