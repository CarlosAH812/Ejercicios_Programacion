students = []

def validate_grade(subject_name):

    while True:
        try:
            grade = int(input(f"Enter {subject_name} grade (0-100): "))
            
            if 0 <= grade <= 100:
                return grade  
            else:
                print("Grade must be between 0 and 100. Please try again.")
        
        except ValueError:
            print("Please enter only numbers.")

def add_student():

    print("\n=== Add New Student ===")
    
    name = input("Enter full name: ").strip()
    
    while not name:
        print("Name cannot be empty.")
        name = input("Enter full name: ").strip()
    
    section = input("Enter section (e.g., 11B): ").strip()
    while not section:
        print("Section cannot be empty.")
        section = input("Enter section (e.g., 11B): ").strip()
 
    print(f"\nEnter grades for {name}:")
    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English") 
    social_grade = validate_grade("Social Studies")
    science_grade = validate_grade("Science")
    
    student = {
        "name": name,
        "section": section,
        "spanish": spanish_grade,
        "english": english_grade,
        "social": social_grade,
        "science": science_grade
    }
    
    students.append(student)

    print(f"\n Student {name} has been added successfully!")

def show_all_students():
   
    if not students:
        print("\nNo students have been added yet.")
        return
    
    print(f"\n=== All Students ({len(students)}) ===")
    
    for i, student in enumerate(students, 1):
        print(f"\n{i}. {student['name']}")
        print(f"   Section: {student['section']}")
        print(f"   Spanish: {student['spanish']}")
        print(f"   English: {student['english']}")
        print(f"   Social Studies: {student['social']}")
        print(f"   Science: {student['science']}")
        
        average = (student['spanish'] + student['english'] + 
                  student['social'] + student['science']) / 4
        print(f"   Average: {average:.2f}") 

def calculate_student_average(student):
    
    return (student['spanish'] + student['english'] + 
            student['social'] + student['science']) / 4

def show_top_3():
    
    if not students:
        print("\nNo students have been added yet.")
        return
    
    if len(students) < 3:
        print(f"\nShowing top {len(students)} student(s):")
    else:
        print("\n=== TOP 3 Students ===")
    
    top_students = sorted(students, key=calculate_student_average, reverse=True)
    
    for i, student in enumerate(top_students[:3], 1):
        average = calculate_student_average(student)
        print(f"\n{i}. {student['name']} - Section: {student['section']}")
        print(f"   Average: {average:.2f}")
        print(f"   Grades: Spanish({student['spanish']}) English({student['english']}) "
              f"Social({student['social']}) Science({student['science']})")

def calculate_general_average():
   
    if not students:
        print("\nNo students have been added yet.")
        return
    
    print("\n=== General Average ===")
    
    total_average = 0
    for student in students:
        student_avg = calculate_student_average(student)
        total_average += student_avg
    
    general_average = total_average / len(students)
    
    print(f"Total students: {len(students)}")
    print(f"General average: {general_average:.2f}")
    
    print(f"\nDetailed breakdown:")
    for i, student in enumerate(students, 1):
        avg = calculate_student_average(student)
        print(f"{i}. {student['name']}: {avg:.2f}")

def add_multiple_students():
   
    while True:
        try:
            num_students = int(input("\nHow many students do you want to add? "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nYou will add {num_students} student(s)")
    
    for i in range(num_students):
        print(f"\n--- Student {i + 1} of {num_students} ---")
        add_student()
    
    print(f"\n All {num_students} students have been added successfully!")