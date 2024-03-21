def minOperations(n):
    # If n is less than or equal to 1, no operations are needed
    if n <= 1:
        return 0

    # Initialize the total number of operations
    operations = 0
    # Start with the smallest prime factor
    divisor = 2

    # Loop until n becomes 1
    while n > 1:
        # Check if the current divisor divides n
        while n % divisor == 0:
            # If yes, add the divisor to the total operations
            operations += divisor
            # Update n by dividing it by the divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1

    # Return the total number of operations
    return operations
