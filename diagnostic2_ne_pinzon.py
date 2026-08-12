while player_input != "launch":
    player_input = input("enter the type of cargo you want to load (sattelite, rover, supplies) or type 'launch' to launch the rocket: ")
    total_fuel = total_weight * 3
    weight_sattelite = 1000
    weight_rover = 2500
    weight_supplies = 500
if player_input == "sattelite":
    total_weight += weight_sattelite
elif player_input == "rover":
    total_weight += weight_rover
elif player_input == "supplies":
     total_weight += weight_supplies
else:
    print("we can't have that on here, friend.")

def calculate_fuel(cargo_weight):
    total_weight = cargo_weight + 50000
    return total_fuel

total_fuel = total_weight * 3
weight_sattelite = 1000
weight_rover = 2500
weight_supplies = 500