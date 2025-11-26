
class Head:
    def __init__(self):
        self.eyes = 2
        self.nose = 1

class Hand:
    def __init__(self):
        self.fingers = 5

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Foot:
    def __init__(self):
        self.toes = 5

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, name, torso):
        self.name = name
        self.torso = torso

right_hand = Hand()
left_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_foot = Foot()
left_foot = Foot()

right_leg = Leg(right_foot)
left_leg = Leg(left_foot)

head = Head()

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

person = Human("Carlos", torso)

print("Human created successfully!")
print(f"Name: {person.name}")
print(f"Eyes: {person.torso.head.eyes}")
print(f"Fingers on right hand: {person.torso.right_arm.hand.fingers}")
print(f"Toes on left foot: {person.torso.left_leg.foot.toes}")