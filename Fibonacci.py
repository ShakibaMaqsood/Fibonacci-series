def fibonacci_generator(n):
    # Initialize variables to store the first two numbers in the sequence

    num1, num2 = 0, 1
    count = 0

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, "terms:")
        print(num1)
    else:
        print("Fibonacci sequence up to", n, "terms:")
        while count < n:
            print(num1, end=" ")
            nth_num = num1 + num2

            # Update values for the next iteration

            num1 = num2
            num2 = nth_num
            count += 1

# Example usage: Generate Fibonacci sequence up to 10 terms
fibonacci_generator(10)