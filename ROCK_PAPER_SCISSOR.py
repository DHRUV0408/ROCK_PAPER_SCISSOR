import random 
i = 1
while i:
    print("-----[R]OCK---[P]APER---[S]CISSOR-----")
    print("--CHOOSE--[R]--FOR--ROCK\n--CHOOSE--[P]--FOR--PAPER\n--CHOOSE--[S]--FOR--SCISSOR")
    user = input("\nCHOOSE YOUR WEAPON AND SHOOT : ")
    user_1 = user.capitalize()
    
    choice = random.choice(["R","P","S"])
    if (user_1 == "R" and choice == 'R') or (user_1 == "P" and choice == 'P') or (user_1 == "S" and choice == 'S'):
        print("-----TIE-----")
        print("I SHOOT : ",choice)
    elif (user_1 == "R" and choice == 'S') or (user_1 == "P" and choice == 'R') or (user_1 == "S" and choice == 'P'):
        print("-----YOU--WON-----")
        print("I SHOOT : ",choice)
    elif (user_1 == "R" and choice == 'P') or (user_1 == "P" and choice == 'S') or (user_1 == "S" and choice == 'R'):
        print("-----YOU--LOSS-----")
        print("I SHOOT : ",choice)
    user_2 = int(input("PRESS 1 FOR PLAY AGAIN OTHERWISE 0 : "))
    if user_2 != 1:
        break
    i = i + user_2