def isPalindrome(word):
    left = 0
    right = len(word) - 1

    while word[left] == word[right] and left < right:
        left += 1
        right -= 1

    return word[left] == word[right]


if __name__ == "__main__":
    word = input("Enter a word to check if it is a palindrome: ")
    wordIsPalindrome = isPalindrome("".join(c.lower() for c in word if c.isalnum()))

    if wordIsPalindrome:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")
