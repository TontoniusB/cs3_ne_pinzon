

| Thinking skill | What to write |
| :---- | :---- |
| Decomposition | Only One Lane Only Two Plant Objects The Plants must have different damage values each Each Plants attack Once per turn If the plant is dead (hp \<= 0\) it will not move. If all plants are dead, break immediately and print that the zombies have won. Only One Zombie Object If the zombie’s hp \<= 0, Stop turn If the hp is not less than or equal to 0, Keep moving 1 space forward if the distance is not 0 If the distance is 0, it attacks the first living plant If the zombie had killed the first plant, it will go on to kill the other after the turn it killed it. If the zombie dies, Plants win. Break it and print. We have to show each action happening |
| Pattern recognition | The plant attacks \-\> The zombie takes damage The zombie moves 1 space forward until it reaches a plant, which it will then attack If the first plant dies, the second plant will start attacking the zombie while it is being attacked by the zombie If either all the plants or the zombie dies, the game ends |
| Abstraction | The First Plant (Guyabasher) has 60 HP The First Plant Deals 10 damage per spike shot The Second Plant (Calamanshooter) has 20 HP The Second Plant Deals 20 Damage Per Seedshot The Zombie (Cone Head) has 130 HP The Zombie Deals 15 Damage per bite The Zombie Has to travel 8 tiles before being able to attack the plants |
| Algorithm design | Check if zombie’s distance from plant is \= 0 Attack if Distance \= 0 Check if plant1 is alive Attack if alive, ignore if dead Check if plant2 is alive Attack if alive, ignore if dead First eligible plant attacks Zombie gets damaged Zombie walks 1 space closer to the plants (Steps 1-9 repeat) |

