#include <iostream>
#include <vector> // Have to use vector for dynamic "arrays" with non-static lengths

template <typename T> class Heap {
public:
    Heap(bool min) {
        // Get parent index: (index − 1) / 2
        // Get left child index: 2 * index + 1
        // Get right child index: 2 * index + 2

        isMin = min;
        length = 0;
    };

    int getLength() { return length; }

    std::vector<T> getHeap() { return heap; }
    
    void PrintHeap() {
        std::cout << "Heap: ";
        for (int x : heap) {
            std::cout << x << " ";
        }
        std::cout << "\n";
    }

    // O(log(n))
    void Add(T value) {
        // Adding the value at the end is O(1)
        heap.push_back(value);
        length++;

        // Resorting the heap is O(log(n))
        isMin ? MinHeapify() : MaxHeapify();
    }

    void MinHeapify() {
        int i = length - 1;
        while ((i > 0) && (heap[i] < heap[(i - 1) / 2])) {
            std::swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    };

    void MaxHeapify() {
        int i = length - 1;
        while ((i > 0) && (heap[i] > heap[(i - 1) / 2])) {
            std::swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    };

    int FindIndex(T value) {
        int index = 0;
        for (int x : heap) {
            if (x == value) return index;
            index++;
        }
        return -1;
    }

    bool Remove(T value) {
        int index = FindIndex(value);
        if (index < 0) return false;

        // Move last element into slot and pop it
        heap[index] = heap.back();
        heap.pop_back();
        length = heap.size();

        // Restore heap property by sifting down
        while (true) {
            int left  = 2 * index + 1;
            int right = 2 * index + 2;
            int swapIdx = index;

            // pick the smaller (for min-heap) or larger (for max-heap) child
            if (left  < length &&
                ((isMin && heap[swapIdx] > heap[left]) ||
                (!isMin && heap[swapIdx] < heap[left])))
                swapIdx = left;
            if (right < length &&
                ((isMin && heap[swapIdx] > heap[right]) ||
                (!isMin && heap[swapIdx] < heap[right])))
                swapIdx = right;

            if (swapIdx == index) break;
            std::swap(heap[index], heap[swapIdx]);
            index = swapIdx;
        }
        return true;
    }

private:
    std::vector<T> heap;
    int length;
    bool isMin;
};

int main() {
    bool isMin = true;
    Heap<int> heap(isMin);

    heap.Add(3);
    heap.Add(9);
    heap.Add(12);
    heap.Add(7);
    heap.Add(1);

    std::cout << "The heap has " << heap.getLength() << " elements." << "\n";
    heap.PrintHeap();

    if (heap.Remove(9)) {
        std::cout << "Successfully removed 9." << "\n";
    } else {
        std::cout << "Failed to remove 9." << "\n";
    }

    if (heap.Remove(4)) {
        std::cout << "Successfully removed 4." << "\n";
    } else {
        std::cout << "Failed to remove 4." << "\n";
    }

    std::cout << "The heap has " << heap.getLength() << " elements." << "\n";
    heap.PrintHeap();

    return 0;
}