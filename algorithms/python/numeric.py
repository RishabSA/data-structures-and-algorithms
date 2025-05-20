def isPrime(num):
    if num <= 1:
        return False

    limit = int(num**0.5) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


# Convert unsigned Base 10 Number to Binary
def toBinary(num):
    if num <= 0:
        return [0]

    binaryList = []
    while num > 0:
        binaryList.append(num % 2)
        num //= 2

    binaryList.reverse()
    return binaryList


def getFactorial(num):
    if num < 2:
        return 1

    factorial = 1
    for i in range(2, num + 1):
        factorial *= i

    return factorial


def getGCD(m, n):
    if n == 0:
        return m

    return getGCD(n, m % n)


if __name__ == "__main__":
    num = int(input("Enter a number to check if it is prime: "))
    numIsPrime = isPrime(num)

    if numIsPrime:
        print(f"{num} is prime!")
    else:
        print(f"{num} is not prime.")

    decimalNum = int(input("Enter an unsigned number to get its binary counterpart: "))
    binaryNum = toBinary(decimalNum)
    print(f"Binary Representation: {binaryNum}")

    num = int(input("Enter a number to get its factorial: "))
    factorial = getFactorial(num)
    print(f"The factorial of {num} is {factorial}.")

    num1 = int(input("Enter number 1 to get its GCD: "))
    num2 = int(input("Enter number 2 to get its GCD: "))
    gcd = getGCD(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd}.")
