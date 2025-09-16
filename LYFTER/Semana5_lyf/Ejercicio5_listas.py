numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

highest = max(numbers)

print(f"The numbers you entered were: {numbers}. The highest was {highest}.")