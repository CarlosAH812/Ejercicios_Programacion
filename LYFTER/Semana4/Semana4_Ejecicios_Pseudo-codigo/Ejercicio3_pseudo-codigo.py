
number = int(input("Enter a number: "))

sum_total = 0
counter = 1

while counter <= number:
    sum_total += counter
    counter += 1

print(f"The sum is: {sum_total}")