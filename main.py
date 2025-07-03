def fibonacci_sequence(n: int) -> list[int]:
    """Generate and return a list of n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        sequence.append(b)
    return sequence


def fibonacci() -> None:
    """Interactive fibonacci function that prints the sequence."""
    n = int(input("How many Fibonacci numbers do you want to see? "))
    sequence = fibonacci_sequence(n)
    print("Fibonacci sequence:")
    print(" ".join(map(str, sequence)))


if __name__ == "__main__":
    print("Hello World!")
    
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("\nError: Please enter a valid number.\n")

    print(f"\nYou entered: {num}")

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    if num % 4 == 0:
        print(f"{num} is divisible by 4")

    if num == 201:
        fibonacci()
