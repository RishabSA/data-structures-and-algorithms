from collections import Counter

if __name__ == "__main__":
    name = "racecar"
    name_counter = Counter(name)  # Dictionary of (character, frequency)
    print(name_counter)

    for char, freq in name_counter.items():
        print(f"{char} appeared {freq} times")
    print("\n")

    print(list(name_counter.elements()))
    print(len(name), len(list(name_counter.elements())))
