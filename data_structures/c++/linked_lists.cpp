#include <iostream>
#include <memory>
#include <optional>

template <typename T> struct Node {
  T num;
  Node<T> *next = nullptr;
};

template <typename T> class LinkedList {
public:
  LinkedList() = default;
  ~LinkedList() {
    delete head;
    delete tail;
  };

  // For bool functions, return true if successful

  bool Push(T num) {
    // O(1)

    if (head == nullptr) {
      head = new Node<T>();
      head->num = num;

      // Track the tail
      tail = head;
      length++;

      return true;
    }

    Node<T> *newNode = new Node<T>();
    newNode->num = num;

    tail->next = newNode;
    tail = newNode;
    length++;

    return true;
  };

  void Display() {
    // O(N)
    if (head == nullptr) {
      return;
    }

    Node<T>* current = head;
    while (current != nullptr) {
      std::cout << current->num << " ";
      current = current->next;
    }
    std::cout << std::endl;
  };

  // Given a value return the 0-based index of where it is
  // in the list.
  int Search(T num) {
    // O(N)

    if (head == nullptr) {
      return -1;
    }

    int currentIdx = 0;

    Node<T> *current = head;

    while (current != nullptr) {
      if (current->num == num) {
        return currentIdx;
      }

      current = current->next;
      currentIdx++;
    }

    return -1;
  };

  T *RemoveAtIndex(int index) {
    if (head == nullptr) {
      return nullptr;
    }

    int currentIdx = 0;

    Node<T> *current = head;
    Node<T> *previous = nullptr;

    while (current->next != nullptr) {
      if (currentIdx == index) {
        T *currentVal = &current->num;
        previous->next = current->next;

        length--;

        return currentVal;
      }

      previous = current;
      current = current->next;
      currentIdx++;
    }

    if (currentIdx == index) {
      T *currentVal = &current->num;
      previous->next = current->next;

      length--;

      return currentVal;
    }

    return nullptr;
  }

  T *Pop() { return RemoveAtIndex(length - 1); }

  int getLength() { return length; }

private:
  Node<T> *head = nullptr;
  Node<T> *tail = nullptr;
  int length = 0;
};

int main() {
  // Create a ll
  LinkedList<int> ll;

  // Insert a few things (6, 10, -15, 0)
  ll.Push(6);
  ll.Push(10);
  ll.Push(-15);
  ll.Push(0);

  std::cout << "Length: " << ll.getLength() << std::endl;

  ll.Display();

  // Search a few things
  std::cout << "Index of -15: " << ll.Search(-15) << std::endl;
  std::cout << "Index of 15: " << ll.Search(15) << std::endl;

  // Pop Last
  auto *popValue = ll.Pop();
  if (popValue == nullptr) {
    std::cout << "Something broke..." << std::endl;
    return 0;
  }

  std::cout << "Popped Value: " << *popValue << std::endl;
  ll.Display();
  std::cout << "Length: " << ll.getLength() << std::endl;

  // Remove at index 1
  auto *value = ll.RemoveAtIndex(1);
  if (value == nullptr) {
    std::cout << "Something broke..." << std::endl;
    return 0;
  }

  std::cout << "Removed Value: " << *value << std::endl;
  ll.Display();
  std::cout << "Length: " << ll.getLength() << std::endl;

  std::cout << "End of program..." << std::endl;

  return 0;
}