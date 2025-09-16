my_list = [9, 4, 7, 1, 5]

smallest = my_list[0]

for num in my_list[1:]:
    if num < smallest:
        smallest = num  

# Display the result
print(f"The smallest value is {smallest}")