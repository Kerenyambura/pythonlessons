#using input
"""myDbValues=("Keren","Purple")
un=input("Enter Username:   ")
psw=input("Enter password:  ")


if un==myDbValues[0] or psw==myDbValues[1]:
    print("Login Succesful")
else:
    print("Incorrect username or password")"""

raffleNumbers= (13,7)
ticketnumber=input("Enter ticket number:    ")

ticketnumber=int(ticketnumber)
print(type(ticketnumber))

if ticketnumber==raffleNumbers[0] or ticketnumber==raffleNumbers[1]:
    print("Welcome to the party")
else:
    print("Shame")
