class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next  # Next Node


class LinkedList:
    def __init__(self):
        self.head = Node(value=None, next=None)

    def append(self, value):
        """
        Get the head and do a while loop over it
        while the value of the head is not None, go to the next
        once it exits out of the while loop, get the current node and set value equal to the value
        then set the next to be a new Node with value=None, next=None

        O(N)
        """
        current = self.head

        while current.value != None:
            current = current.next

        current.value = value
        current.next = Node(value=None, next=None)

    def insert(self, index, value):
        """
        O(N)
        """
        current = self.head
        currentIndex = 0

        while current.value != None:
            if currentIndex == index:
                currentValue = current.value
                current.value = value
                current.next = Node(value=currentValue, next=current.next)

            current = current.next
            currentIndex += 1

    def pop(self):
        current = self.head

        if current.next.value != None:
            # More than one item
            while current.next.next.value != None:
                current = current.next

            current.next = Node(value=None, next=None)
        else:
            # One item
            self.head = Node(value=None, next=None)

    def remove(self, index):
        """
        O(N)
        """
        current = self.head
        currentIndex = 0

        while current.value != None:
            if currentIndex == index:
                nextValue = current.next.value
                nextNext = current.next.next
                current.value = nextValue
                current.next = nextNext

            current = current.next
            currentIndex += 1

    def valueAt(self, index):
        """
        O(N)
        """
        current = self.head
        currentIndex = 0

        while current.value != None:
            if currentIndex == index:
                return current.value
            current = current.next
            currentIndex += 1

        return None

    def indexOf(self, value):
        """
        O(N)
        """
        index = 0
        current = self.head
        while current.value != None:
            if current.value == value:
                return index
            index += 1
            current = current.next

        return -1

    def getLength(self):
        current = self.head
        length = 0

        while current.value != None:
            length += 1
            current = current.next

        return length

    def toList(self):
        arr = []
        current = self.head

        while current.value != None:
            arr.append(current.value)
            current = current.next

        return arr


list = LinkedList()
list.append(10)
list.append(20)
list.append(30)

list.insert(0, 5)
list.insert(2, 15)

print(list.indexOf(10))
print(list.indexOf(20))
print(list.indexOf(30))
print(list.indexOf(5))
print(list.indexOf(40))

print(list.valueAt(0))
print(list.valueAt(1))
print(list.valueAt(2))
print(list.valueAt(3))

print(list.toList())

# list.pop()
# print(list.toList())
# list.pop()
# print(list.toList())
# list.pop()
# print(list.toList())
# list.pop()
# print(list.toList())
# list.pop()
# print(list.toList())

list.remove(1)
print(list.toList())
list.remove(2)
print(list.toList())

print(list.getLength())
