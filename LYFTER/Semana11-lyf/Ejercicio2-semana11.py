
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers 
        self.passengers = []  
        print(f" Bus created with capacity for {max_passengers} passengers")
    
    def board(self, person): 
        if len(self.passengers) >= self.max_passengers:
            print(f" Bus full. {person.name} cannot board")
            print(f"Capacity: {len(self.passengers)}/{self.max_passengers}")
            return False  
        
        self.passengers.append(person)  
        print(f" {person.name} boarded the bus")
        print(f"Current passengers: {len(self.passengers)}/{self.max_passengers}\n")
        return True  
    
    def alight(self, person):
        if person in self.passengers:
            self.passengers.remove(person)  
            print(f" {person.name} got off the bus")
            print(f"Remaining passengers: {len(self.passengers)}/{self.max_passengers}")
            return True  
        else:
            print(f" {person.name} is not on the bus")
            return False 
    
    def show_passengers(self):
        print(f"\n Passengers on the bus ({len(self.passengers)}/{self.max_passengers}):")
        if self.passengers:  
            for i, person in enumerate(self.passengers, 1):
                print(f"{i}. {person}")
        else:
            print("(Empty bus)")
    
    def is_full(self):
        return len(self.passengers) >= self.max_passengers
    
    def available_seats(self):
        return self.max_passengers - len(self.passengers)


print("=" * 50)
print("BUS SYSTEM TEST")
print("=" * 50)

bus = Bus(max_passengers=3)

ana = Person("Ana", 25)
carlos = Person("Carlos", 30)
maria = Person("Maria", 28)
juan = Person("Juan", 35)

print("\n--- Trying to board passengers ---")
bus.board(ana) 

bus.board(carlos)  

bus.board(maria)  

bus.board(juan)     

bus.show_passengers()

print("\n--- Passengers getting off ---")

bus.alight(carlos)  

bus.show_passengers()

print("\n--- Trying to board again ---")

bus.board(juan)     

bus.show_passengers()

print("\n--- Trying to remove someone who is not on the bus ---")

bus.alight(carlos)  

print(f"\n Available seats: {bus.available_seats()}")
print(f" Is bus full?: {bus.is_full()}")
