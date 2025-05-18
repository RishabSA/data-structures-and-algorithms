class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def Push(self, val):
        if self.head == None:
            self.head = Node(val=val)
            self.tail = self.head
        else:
            self.tail.next = Node(val=val)
            self.tail = self.tail.next

        self.length += 1

    # O(N) but O(1) for insertion at head
    def Insert(self, val, idx):
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            old_head = self.head
            self.head = Node(val=val, next=old_head)
            if self.length == 0:
                self.tail = self.head

            self.length += 1
            return True

        current = self.head
        currentIdx = 0

        while current != None:
            if currentIdx == idx - 1:
                new_node = Node(val=val, next=current.next)
                current.next = new_node
                if current.next == None:
                    self.tail = new_node

                self.length += 1
                return True

            currentIdx += 1
            current = current.next

        return False

    # O(N)
    def GetList(self):
        if self.head == None:
            return None

        current = self.head
        convertedList = []

        while current != None:
            convertedList.append(current.val)
            current = current.next

        return convertedList

    def Display(self, reversed=False):
        if self.length == 0:
            return

        if reversed:
            convertedList = self.ReverseTraversal()

            print(f"Reversed Linked List Items: {convertedList}")
        else:
            convertedList = self.GetList()

            print(f"Linked List Items: {convertedList}")

    # O(N)
    def Search(self, val):
        if self.head == None:
            return -1

        current = self.head
        currentIdx = 0

        while current != None:
            if current.val == val:
                return currentIdx

            currentIdx += 1
            current = current.next

        return -1

    # O(N) but O(1) for deletion of head
    def Remove(self, val):
        if self.head == None:
            return -1

        if self.head.val == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

            self.length -= 1
            return 0

        # Start from second item because we already checked the first
        currentIdx = 1
        current = self.head.next
        previous = self.head

        while current != None:
            if current.val == val:
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous

                self.length -= 1
                return currentIdx

            currentIdx += 1
            previous = current
            current = current.next

        return -1

    # O(N) but O(1) for deletion of head
    def RemoveAtIndex(self, idx):
        if self.head == None or idx < 0 or idx >= self.length:
            return None

        if idx == 0:
            removedVal = self.head.val
            self.head = self.head.next
            if self.head is None:
                self.tail = None

            self.length -= 1
            return removedVal

        currentIdx = 0
        current = self.head
        previous = None

        while current != None:
            if currentIdx == idx:
                removed_val = current.val
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous

                self.length -= 1
                return removed_val

            currentIdx += 1
            previous = current
            current = current.next

        return None

    # O(N)
    def Pop(self):
        return self.RemoveAtIndex(self.length - 1)

    # O(N^2)
    def ReverseTraversal(self):
        reversedList = []

        if self.tail == None:
            return []

        current = self.tail
        while current != self.head:
            previous = self.head
            while previous.next != current:
                previous = previous.next

            reversedList.append(current.val)
            current = previous

        reversedList.append(current.val)

        return reversedList


if __name__ == "__main__":
    ll = LinkedList()
    ll.Push(6)
    ll.Push(10)
    ll.Push(-15)
    ll.Push(0)

    ll.Insert(3, 2)
    ll.Insert(9, 0)

    ll.Display()
    ll.Display(reversed=True)
    print(f"Linked List Length: {ll.length}")

    idx1 = ll.Search(10)
    print("Could not find 10" if idx1 == -1 else f"Found 10 at index: {idx1}")

    idx2 = ll.Search(16)
    print("Could not find 16" if idx2 == -1 else f"Found 16 at index: {idx2}")

    idx3 = ll.Search(-15)
    print("Could not find -15" if idx3 == -1 else f"Found -15 at index: {idx3}")

    removedIdx1 = ll.Remove(10)
    print(f"Removed 10 at index: {removedIdx1}")
    ll.Display()

    removedItem0 = ll.RemoveAtIndex(0)
    print(f"Removed first index item: {removedItem0}")
    ll.Display()

    poppedVal = ll.Pop()
    print(f"Popped last item: {poppedVal}")
    ll.Display()
