my_list = [3, 6, 0, -2, 4]

all_positive = True

for num in my_list:
    if num <= 0: 
        all_positive = False
        break 

if all_positive:
    print("All numbers are positive")
else:
    print("There is at least one negative number or zero")