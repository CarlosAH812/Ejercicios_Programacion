
largest = float(input("Enter number 1: "))

for i in range(2, 101):
    num = float(input(f"Enter number {i}: "))
    if num > largest:
        largest = num

print(f"The largest number entered is: {largest}")