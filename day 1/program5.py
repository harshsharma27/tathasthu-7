p1 = int(input("Enter runs scored by player-1 on 60 balls: "))
p2 = int(input("Enter runs scored by player-2 on 60 balls: "))
p3 = int(input("Enter runs scored by player-3 on 60 balls: "))
strikerate_1 = p1 * 100/60
strikerate_2 = p2 * 100/60
strikerate_3 = p3 * 100/60
print("Strike rate of player 1 is: ",strikerate_1)
print("Strike rate of player 2 is: ",strikerate_2)
print("Strike rate of player 3 is: ",strikerate_3)
print("Runs scored by player 1 if they played 60 balls more: ",p1*2)
print("Runs scored by player 2 if they played 60 balls more: ",p2*2)
print("Runs scored by player 3 if they played 60 balls more: ",p3*2)
print("Maximum number of sixes hit by player 1 is: ",p1//6)
print("Maximum number of sixes hit by player 2 is: ",p2//6)
print("Maximum number of sixes hit by player 3 is: ",p3//6)