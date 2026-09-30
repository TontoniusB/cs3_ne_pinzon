class Zombie:
    def __init__(self,name,health,damage,distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance
        print(name,health,damage,distance)

    def move(distance):
        distance = 8
        while distance != 0:
            distance = 8 - 1
            print(f"Zombie moved {distance} steps forward")

    def attack(self, plant):
       
        print(f"{plant} got attacked by {self.name}")


    def take_damage(amount):
        pass
    

class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        print(name,health,damage)

    def attack(self, zombie):
        Zombie.health = Zombie.health - self.damage
        print(f"{zombie} got attacked by {self.name}")


    def take_damage(amount):
        pass

Zombiee = Zombie("Conehead",130,15,8)
Prantsu = Plant("Guyabasher",60,10)
Pranstu2 = Plant("Calamanshooter",20,20)
print("The Zombie Died")