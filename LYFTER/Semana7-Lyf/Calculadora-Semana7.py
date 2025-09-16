def read_number(prompt):
    
    text = input(prompt).strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None

def display_menu(current):

    print("\n=== Calculator ===")
    print(f"Current number: {current}")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Clear result (set to 0)")

def get_user_option():
    
    return input("Choose an option (Ctrl+C to quit): ").strip()

def validate_option(option):
    
    return option.isdigit() and int(option) in range(1, 6)

def clear_result():
    
    print("🧹 Result cleared. Current number = 0")
    return 0.0

def perform_addition(current, number):
    
    result = current + number
    print(f"✅ Addition done. New current = {result}")
    return result

def perform_subtraction(current, number):
    
    result = current - number
    print(f"✅ Subtraction done. New current = {result}")
    return result

def perform_multiplication(current, number):
    
    result = current * number
    print(f"✅ Multiplication done. New current = {result}")
    return result

def perform_division(current, number):
    
    if number == 0:
        print("❌ Error: cannot divide by zero.")
        return None
    result = current / number
    print(f"✅ Division done. New current = {result}")
    return result

def show_invalid_option_error():
    
    print("❌ Invalid option. Please choose 1, 2, 3, 4 or 5.")

def show_invalid_number_error():
    
    print("❌ Invalid number. Try again (examples: 5, 3.14, -7.5).")

def process_operation(current, option):
    
    if option == 5:
        return clear_result()
    
    number = read_number("Enter the number for the operation: ")
    if number is None:
        show_invalid_number_error()
        return current
    
    if option == 1:
        return perform_addition(current, number)
    elif option == 2:
        return perform_subtraction(current, number)
    elif option == 3:
        return perform_multiplication(current, number)
    elif option == 4:
        result = perform_division(current, number)
        return result if result is not None else current

def main():
    
    current = 0.0
    
    try:
        while True:
            display_menu(current)
            option = get_user_option()
            
            if not validate_option(option):
                show_invalid_option_error()
                continue
            
            option = int(option)
            current = process_operation(current, option)
            
    except KeyboardInterrupt:
        print("\n👋 Exiting calculator. Goodbye!")

if __name__ == "__main__":
    main()