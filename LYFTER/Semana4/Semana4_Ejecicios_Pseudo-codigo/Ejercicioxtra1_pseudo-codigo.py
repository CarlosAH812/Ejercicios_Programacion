
first = float(input("Enter the first number: "))

second = float(input("Enter the second number: "))

if first > second:
    temp = first
    first = second
    second = temp

print("The numbers in ascending order are:")
print(first)
print(second)