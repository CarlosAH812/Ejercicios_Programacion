from datetime import datetime

class User:
    
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        
        return age


def validate_adult(function):
    
    def wrapper(*args, **kwargs):
        user = None
        
        for arg in args:
            if isinstance(arg, User):
                user = arg
                break 
        
        if user is None:
            for value in kwargs.values():
                if isinstance(value, User):
                    user = value
                    break
        
        if user is None:
            raise ValueError("Function requires a User parameter")
        
        if user.age < 18:
            raise PermissionError(f"User '{user.name}' is underage. Age: {user.age}, required: 18+")
        
        result = function(*args, **kwargs)
        
        return result
    
    return wrapper