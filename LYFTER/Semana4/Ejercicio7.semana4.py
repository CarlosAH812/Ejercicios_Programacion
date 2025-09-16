
number = int(input("Enter a number (1 to 10): "))

print(f"Multiplication table for {number}:")
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")