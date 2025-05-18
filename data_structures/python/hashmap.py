if __name__ == "__main__":
    # In python, hashmaps are dictionaries
    people = {"John": 32, "Adele": 45, "Bo": 29}

    print(f"John is {people["John"]} years old")
    print(f"Adele is {people["Adele"]} years old")

    people["Jenny"] = 22
    people["Liam"] = 24
    people["Kasper"] = 20
    people["Anja"] = 30

    del people["John"]

    print("\n")

    for person, age in people.items():
        print(f"{person} is {age} years old.")
