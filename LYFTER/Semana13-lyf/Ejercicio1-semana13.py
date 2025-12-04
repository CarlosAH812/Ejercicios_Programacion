def show_info(function):
    
    def wrapper(*args, **kwargs):
        
        print(f"Calling '{function.__name__}'")
        
        print(f"  Positional parameters: {args}")
        
        print(f"  Keyword parameters: {kwargs}")
    
        result = function(*args, **kwargs)
        
        print(f"  Return: {result}")
        print("-" * 40)
        
        return result
    
    return wrapper