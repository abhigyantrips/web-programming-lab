# Statistics from N Numbers
import statistics

# Read the number of inputs
n = int(input("Enter the number of values: "))
numbers = []

# Read n numbers from the console
for _ in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Calculate mean, variance, and standard deviation
mean = statistics.mean(numbers)
variance = statistics.variance(numbers)
std_dev = statistics.stdev(numbers)

# Print the results
print(f"The mean of the numbers is: {mean:.2f}")
print(f"The variance of the numbers is: {variance:.2f}")
print(f"The standard deviation of the numbers is: {std_dev:.2f}")
