# def calculate_golden_ratio(numbers):
#   golden_ratios = []
#   for i in range(1, len(numbers)):
#     if numbers[i - 1] == 0:
#       continue
#     golden_ratio = numbers[i] + numbers[i - 1]
#     golden_ratios.append(golden_ratio)
#   return golden_ratios

# sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# print(calculate_golden_ratio(sequence))
# Initialize the sequence with the first two numbers
fibonacci = [0, 1]

# Set the limit for the number of elements in the sequence
limit = 10

# Generate the rest of the sequence using a for loop
for i in range(2, limit):
  fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)
