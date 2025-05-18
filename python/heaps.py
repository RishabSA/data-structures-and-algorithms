class Heap:
    def __init__(self):
        # Get parent index: (index − 1) / 2
        # Get left child index: 2 * index + 1
        # Get right child index: 2 * index + 2

        self.length = 0
        self.heap = []

    def PrintHeap(self):
        print(f"Heap: {self.heap}")

    # O(log(N))
    def Add(self, val):
        # Adding to heap is O(1)
        self.heap.append(val)
        self.length += 1

        # Resorting the heap is O(log(N))
        self.MinHeapify()

    # O(log(N))
    def MinHeapify(self):
        i = self.length - 1  # Start with last inserted element
        # Starting at the lowest children in the heap, check if they are less than parents
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            # Swap with parent which moves it upwards
            self.heap[i], self.heap[(i - 1) // 2] = (
                self.heap[(i - 1) // 2],
                self.heap[i],
            )
            i = (i - 1) // 2

    # O(log(N))
    def MaxHeapify(self):
        i = self.length - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = (
                self.heap[(i - 1) // 2],
                self.heap[i],
            )
            i = (i - 1) // 2

    # O(N)
    def FindIndex(self, value):
        for i in range(self.length):
            if self.heap[i] == value:
                return i

        return -1

    def Remove(self, value):
        index = self.FindIndex(value)
        if index < 0:
            return False

        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self.length -= 1

        i = index
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            if left >= self.length:  # No children
                break

            # Get the smaller child
            smallest = left
            if right < self.length and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[i] <= self.heap[smallest]:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return True

    def Contains(self, value):
        start = 0
        nodes = 1

        while start < self.length:
            start = nodes - 1
            end = nodes + start
            count = 0

            while start < self.length and start < end:
                if value == self.heap[start]:
                    return True
                elif value > self.heap[(start - 1) // 2] and value < self.heap[start]:
                    count += 1

                start += 1

            if count == nodes:
                return False

            nodes *= 2

        return False


if __name__ == "__main__":
    heap = Heap()
    heap.Add(3)
    heap.Add(9)
    heap.Add(-3)
    heap.Add(7)
    heap.Add(1)
    heap.Add(-4)
    heap.PrintHeap()

    print(f"The heap has {heap.length} elements.")
    print("\n")

    if heap.Remove(9):
        print("Successfully removed 9.")
    else:
        print("Failed to remove 9.")

    if heap.Remove(4):
        print("Successfully removed 4.")
    else:
        print("Failed to remove 4.")

    print(f"The heap has {heap.length} elements.")
    heap.PrintHeap()
    print("\n")

    if heap.Contains(3):
        print("The heap contains 3.")
    else:
        print("The heap does not contain 3.")

    if heap.Contains(9):
        print("The heap contains 9.")
    else:
        print("The heap does not contain 9.")
