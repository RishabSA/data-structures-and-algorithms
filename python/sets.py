if __name__ == "__main__":
    a = {2, 1, 3}
    b = {6, 9, 2, 6}  # Duplicates are ignored

    print(f"Set A: {a}")
    print(f"Set B: {b}")

    print(f"Length of Set A: {len(a)}")
    print(f"Length of Set B: {len(b)}")

    print("\n")

    a.add(4)
    b.add(4)

    print(f"Set A (after adding): {a}")
    print(f"Set B (after adding): {b}")

    print("\n")

    print(f"First element in Set A: {list(a)[0]}")
    print(f"First element in Set B: {list(b)[0]}")

    print(f"Third element in Set A: {list(a)[2]}")
    print(f"Third element in Set B: {list(b)[2]}")

    print("\n")

    a.discard(6)
    b.discard(6)

    print(f"Set A (after deleting): {a}")
    print(f"Set B (after deleting): {b}")

    # Set Union
    union_set = a | b  # or a.union(b)

    # Set Intersection
    intersection_set = a & b  # or a.intersection(b)

    print("Union:", union_set)
    print("Intersection:", intersection_set)
