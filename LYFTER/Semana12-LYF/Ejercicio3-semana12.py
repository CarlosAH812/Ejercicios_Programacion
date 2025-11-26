class CanFly:
   
    def __init__(self, max_altitude):
        self.max_altitude = max_altitude
    
    def fly(self):
        return f"Flying up to {self.max_altitude} meters!"


class CanSwim:
 
    def __init__(self, max_depth):
        self.max_depth = max_depth
    
    def swim(self):
        return f"Swimming down to {self.max_depth} meters!"


class CanRun:

    def __init__(self, max_speed):
        self.max_speed = max_speed
    
    def run(self):
        return f"Running at {self.max_speed} km/h!"

class Bird(CanFly):
 
    def __init__(self, name, max_altitude):
        self.name = name
        CanFly.__init__(self, max_altitude)


class Fish(CanSwim):

    def __init__(self, name, max_depth):
        self.name = name
        CanSwim.__init__(self, max_depth)

class Duck(CanFly, CanSwim, CanRun):

    def __init__(self, name, max_altitude, max_depth, max_speed):
        self.name = name
        CanFly.__init__(self, max_altitude)
        CanSwim.__init__(self, max_depth)
        CanRun.__init__(self, max_speed)
    
    def quack(self):
        return "Quack quack!"

print("=" * 60)
print("Animals with single inheritance")
print("=" * 60)

parrot = Bird("Loro", 100)
print(f"\n{parrot.name}:")
print(f"  - {parrot.fly()}")

salmon = Fish("Salmón", 50)
print(f"\n{salmon.name}:")
print(f"  - {salmon.swim()}")

print("\n" + "=" * 60)
print("Animal with multiple inheritance")
print("=" * 60)

donald = Duck(
    name="Donald",
    max_altitude=50,
    max_depth=10,
    max_speed=15
)

print(f"\n{donald.name}:")
print(f"  - {donald.fly()}")     
print(f"  - {donald.swim()}")    
print(f"  - {donald.run()}")     
print(f"  - {donald.quack()}")   
