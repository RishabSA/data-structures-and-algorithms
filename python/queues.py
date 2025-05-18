if __name__ == "__main__":
    queue = []  # Queues use FIFO (First In, First Out)

    # Enqueue
    queue.append(10)
    queue.append(12)
    queue.append(9)
    queue.append(8)
    queue.append(3)

    print(f"Queue: {queue}")

    print(f"The queue has {len(queue)} elements.")
    print("\n")

    # Front and Back Elements
    print(f"The front element is: {queue[0]}")
    print(f"The back element is: {queue[-1]}")
    print("\n")

    # Dequeue
    queue.pop(0)
    queue.pop(0)

    print(f"(After dequeue) Queue: {queue}")
    print(f"The front element is: {queue[0]}")
    print(f"The back element is: {queue[-1]}")
