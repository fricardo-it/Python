#Q1

import random

#1.a
class Vehicle:
    #1.b
    def __init__(self, pilot_name, max_speed, color):
        self.pilot_name = pilot_name
        self.max_speed = max_speed
        self.color = color
        self.is_broken = False
        self.distance = 0
    #1.c
    def move(self):
        if not self.is_broken:
            speed = random.randint(0, self.max_speed)
            self.distance += speed / 20
    #1.d
    def crash(self):
        if random.randint(1, 100) == 55:
            self.is_broken = True

#1.e
class Race:
    #1.e
    def __init__(self, vehicles):
        self.vehicles = vehicles
    #1.e
    def start(self):
        race_finished = False
        
        while not race_finished:
            for vehicle in self.vehicles:
                vehicle.move()
                vehicle.crash()
            #1.f
            for vehicle in self.vehicles:
                if vehicle.distance >= 100:
                    race_finished = True
                    break
            #1.g
            all_broken = True
            for vehicle in self.vehicles:
                if not vehicle.is_broken:
                    all_broken = False
                    break
            #1.h
            if all_broken:
                race_finished = True
            #1.i
            for vehicle in self.vehicles:
                if vehicle.distance >= 100:
                    race_finished = True
                    break

#1.j

# 5 instances of Vehicle
vehicle1 = Vehicle("Francisco", 10, "Red")
vehicle2 = Vehicle("Daniel", 12, "Blue")
vehicle3 = Vehicle("Renan", 8, "Green")
vehicle4 = Vehicle("Larissa", 15, "Yellow")
vehicle5 = Vehicle("Barbara", 9, "Purple")

# 1 instance of Race
race = Race([vehicle1, vehicle2, vehicle3, vehicle4, vehicle5])

# pilot victories
wins_count = {vehicle.pilot_name: 0 for vehicle in race.vehicles}

# 3 races
for i in range(3):
    race.start()

    winner = max(race.vehicles, key=lambda x: x.distance)
    wins_count[winner.pilot_name] += 1

    print(f"Race {i+1} Winner: {winner.pilot_name}")
    
    # reset for new race   
    for vehicle in race.vehicles:
        vehicle.distance = 0
        vehicle.is_broken = False

biggest_winner = max(wins_count, key=wins_count.get)
    
print("\nBiggest Winner:", biggest_winner, "with", wins_count[biggest_winner], "victories.")

