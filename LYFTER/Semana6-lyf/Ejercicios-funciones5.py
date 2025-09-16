def count_upper_lower(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():       
            upper_count += 1
        elif char.islower():     
            lower_count += 1

    return upper_count, lower_count   

# Example usage
text_example = "I love Nación Sushi"
upper, lower = count_upper_lower(text_example)
print(f"There are {upper} uppercase letters and {lower} lowercase letters")


#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#   A. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”