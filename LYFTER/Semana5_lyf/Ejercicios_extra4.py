my_list = [10, 20, 30, 40, 50]

average = sum(my_list) / len(my_list)

above_average = [num for num in my_list if num > average]

print(f"Average: {average}")
print(f"New list: {above_average}")