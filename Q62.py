class Ambulance:
    def __init__(self, priority, speed, capacity):
        self.priority = priority
        self.speed = speed
        self.capacity = capacity

p1 = Ambulance(1, 45 ,4)

controlled_velocity = -10(1 - priority) + 2.37(speed/10) + 30(capacity +1.2)

print(controlled_velocity)
