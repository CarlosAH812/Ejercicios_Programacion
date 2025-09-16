
women = 0
men = 0
counter = 1

while counter <= 6:
    sex = int(input(f"Enter the sex of person {counter} (1 = woman, 2 = man): "))

    if sex == 1:
        women += 1
    else:
        men += 1

    counter += 1

percent_women = (women * 100) / 6
percent_men = (men * 100) / 6

print(f"Percentage of women: {percent_women:.2f}%")
print(f"Percentage of men: {percent_men:.2f}%")