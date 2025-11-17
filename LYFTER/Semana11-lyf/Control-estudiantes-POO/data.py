
import csv
import os
from student import Student

def export_to_csv(students, csv_filename="students_data.csv"):
    if not students:
        print("\nNo students to export. Please add students first.")
        return
    
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'section', 'spanish', 'english', 'social', 'science']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in students:
                writer.writerow(student.to_dict())
        
        print(f"\n Successfully exported {len(students)} student(s) to '{csv_filename}'")
        print(f"File location: {os.path.abspath(csv_filename)}")
    
    except Exception as e:
        print(f"\n Error exporting data: {e}")

def import_from_csv(students, csv_filename="students_data.csv"):
    if not os.path.exists(csv_filename):
        print(f"\n File '{csv_filename}' not found.")
        print("Please export data first or make sure the file exists in the same directory.")
        return students
    
    try:
        imported_count = 0
        
        with open(csv_filename, 'r', encoding='utf-8') as file:
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
                    row['spanish'] = int(row['spanish'])
                    row['english'] = int(row['english'])
                    row['social'] = int(row['social'])
                    row['science'] = int(row['science'])
                    
                    grades = [row['spanish'], row['english'], row['social'], row['science']]
                    if all(0 <= grade <= 100 for grade in grades):
                        student = Student.from_dict(row)
                        students.append(student)
                        imported_count += 1
                    else:
                        print(f"Warning: Skipped student '{row['name']}' - invalid grades")
                
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
        print(f"\n✗ Error importing data: {e}")
        return students

def show_file_info(csv_filename="students_data.csv"):
    
    if os.path.exists(csv_filename):
        file_size = os.path.getsize(csv_filename)
        print(f"\n File info:")
        print(f"Name: {csv_filename}")
        print(f"Size: {file_size} bytes")
        print(f"Location: {os.path.abspath(csv_filename)}")
        
        try:
            with open(csv_filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                print(f"Lines in file: {len(lines)}")
                if lines:
                    print(f"Header: {lines[0].strip()}")
        except:
            print("Could not read file content")
    else:
        print(f"\n File '{csv_filename}' does not exist")