
import csv
import os

CSV_FILENAME = "students_data.csv"

def export_to_csv(students):
   
    if not students:
        print("\nNo students to export. Please add students first.")
        return
    
    try:
        with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'section', 'spanish', 'english', 'social', 'science']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        
        print(f"\n Successfully exported {len(students)} student(s) to '{CSV_FILENAME}'")
        print(f"File location: {os.path.abspath(CSV_FILENAME)}")
    
    except Exception as e:
        print(f"\n Error exporting data: {e}")

def import_from_csv(students):
    
    if not os.path.exists(CSV_FILENAME):
        print(f"\n File '{CSV_FILENAME}' not found.")
        print("Please export data first or make sure the file exists in the same directory.")
        return students 
    
    try:
        imported_count = 0
        
        with open(CSV_FILENAME, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            if students:
                print(f"\nCurrently there are {len(students)} student(s) in memory.")
                choice = input("Do you want to (R)eplace all or (A)ppend to existing data? (R/A): ").upper().strip()
                
                if choice == 'R':
                    
                    students = []
                    print("Existing data cleared.")
                elif choice == 'A':
                    print("New data will be added to existing students.")
                else:
                    print("Invalid choice. Operation cancelled.")
                    return students  
            
            for row in reader:
                try:
                    student = {
                        'name': row['name'],
                        'section': row['section'],
                        'spanish': int(row['spanish']),
                        'english': int(row['english']),
                        'social': int(row['social']),
                        'science': int(row['science'])
                    }
                    
                    grades = [student['spanish'], student['english'], student['social'], student['science']]
                    if all(0 <= grade <= 100 for grade in grades):
                        students.append(student)
                        imported_count += 1
                    else:
                        print(f"Warning: Skipped student '{student['name']}' - invalid grades")
                
                except ValueError:
                    print(f"Warning: Skipped row with invalid grade format")
                except KeyError as e:
                    print(f"Warning: Skipped row - missing column: {e}")
        
        if imported_count > 0:
            print(f"\n Successfully imported {imported_count} student(s)")
            print(f"Total students now: {len(students)}")
        else:
            print("\n No valid students were imported")
        
        return students
    
    except Exception as e:
        print(f"\n Error importing data: {e}")
        return students

def show_file_info():
    
    if os.path.exists(CSV_FILENAME):
        file_size = os.path.getsize(CSV_FILENAME)
        print(f"\n File info:")
        print(f"Name: {CSV_FILENAME}")
        print(f"Size: {file_size} bytes")
        print(f"Location: {os.path.abspath(CSV_FILENAME)}")
        
        try:
            with open(CSV_FILENAME, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                print(f"Lines in file: {len(lines)}")
                if lines:
                    print(f"Header: {lines[0].strip()}")
        except:
            print("Could not read file content")
    else:
        print(f"\n File '{CSV_FILENAME}' does not exist")