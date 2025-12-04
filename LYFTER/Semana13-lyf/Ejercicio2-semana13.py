def validate_numbers(function):
    
    def wrapper(*args, **kwargs):
        
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"All parameters must be numbers. '{arg}' is {type(arg).__name__}")
        
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"All parameters must be numbers. '{key}={value}' is {type(value).__name__}")
        
        result = function(*args, **kwargs)
        
        return result
    
    return wrapper