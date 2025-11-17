
class Student:
    
    def __init__(self, name, section, spanish, english, social, science):
        
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
    
    def calculate_average(self):
        return (self.spanish + self.english + self.social + self.science) / 4
    
    def to_dict(self):
        return {
            'name': self.name,
            'section': self.section,
            'spanish': self.spanish,
            'english': self.english,
            'social': self.social,
            'science': self.science
        }
    
    @staticmethod
    def from_dict(data_dict):
        return Student(
            name=data_dict['name'],
            section=data_dict['section'],
            spanish=int(data_dict['spanish']),
            english=int(data_dict['english']),
            social=int(data_dict['social']),
            science=int(data_dict['science'])
        )
    
    def __str__(self):
        return f"{self.name} ({self.section}) - Promedio: {self.calculate_average():.2f}"
    
    def __repr__(self):
        return f"Student(name='{self.name}', section='{self.section}', avg={self.calculate_average():.2f})"