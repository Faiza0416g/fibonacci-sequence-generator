print("🔢 Fibonacci Sequence Generator")

n = int(input("Enter the number of terms: "))

first = 0
second = 1

count = 0

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(first)
else:
    print("Fibonacci sequence:")

    while count < n:
        print(first)
        next_number = first + second
        first = second
        second = next_number
        count += 1
