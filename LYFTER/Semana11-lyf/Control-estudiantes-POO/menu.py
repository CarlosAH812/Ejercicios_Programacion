from actions import add_multiple_students, show_all_students, show_top_3, calculate_general_average
from data import export_to_csv, import_from_csv

def show_menu():
    
    print("\n" + "="*50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add students")
    print("2. View all students") 
    print("3. Show top 3 students")
    print("4. Calculate general average")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. Exit")
    print("="*50)

def get_user_choice():
    
    while True:
        try:
            choice = int(input("Select an option (1-7): "))
            
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid option. Please select a number between 1 and 7.")
        
        except ValueError:
            print("Please enter a valid number.")

def process_menu_choice(choice, students):
    
    if choice == 1:
        students = add_multiple_students(students)
    
    elif choice == 2:
        show_all_students(students)
    
    elif choice == 3:
        show_top_3(students)
    
    elif choice == 4:
        calculate_general_average(students)
    
    elif choice == 5:
        export_to_csv(students)
    
    elif choice == 6:
        students = import_from_csv(students)
    
    elif choice == 7:
        print("\n Thank you for using the Student Management System!")
        print("Goodbye!")
        return students, False
    
    return students, True

def main_menu():
    print(" Welcome to the Student Management System!")
    
    students = []
    
    continue_program = True
    
    while continue_program:
        show_menu()
        user_choice = get_user_choice()
        
        students, continue_program = process_menu_choice(user_choice, students)