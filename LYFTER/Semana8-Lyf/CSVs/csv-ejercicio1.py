import csv

file_name = "videogames.csv"

n = int(input("How many videogames do you want to enter? "))

with open(file_name, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    header = ["Name", "Genre", "Developer", "ESRB_Rating"]
    writer.writerow(header)
    
    for i in range(n):
        print(f"\nVideogame {i+1}:")
        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        esrb = input("ESRB Rating: ")
        
        writer.writerow([name, genre, developer, esrb])

print(f"\n {n} videogames have been saved in the file '{file_name}'.\n")

with open(file_name, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

print(" File content in table format:\n")

for row in rows:
    for i, value in enumerate(row):
        print(value.ljust(widths[i] + 2), end="")  
    print()