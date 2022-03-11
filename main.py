num = int(input('Enter the upper limit: '))
print([i for i in range(2, num) if all([i % j for j in range(2, i)])])

# The program will print a list of prime numbers below the input value.
