import statistics

numbers = [int(_) for _ in input("Enter numbers separated by space: ").split()]

mean = statistics.mean(numbers)

median = statistics.median(numbers)

try:
    mode = statistics.mode(numbers)
except statistics.StatisticsError:
    mode = "No unique mode found"

range_value = max(numbers) - min(numbers)

variance = statistics.variance(numbers)

std_deviation = statistics.stdev(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", range_value)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
