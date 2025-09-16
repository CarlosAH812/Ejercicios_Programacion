entrada = input("Enter a list of numbers separated by spaces or commas: ")

# Reemplazar comas por espacios, luego separar por espacios y convertir a enteros
my_list = [int(x) for x in entrada.replace(",", " ").split()]

# Mostrar la lista que se creó
print("The list of numbers is:", my_list)

# Pedir el número a buscar
number_to_find = int(input("Enter the number you want to search for: "))

# Contar cuántas veces aparece
count = my_list.count(number_to_find)

# Mostrar el resultado
print(f"The number {number_to_find} appears {count} times")