#using input
myDbValues=("Keren","Purple")
un=input("Enter Username:   ")
psw=input("Enter password:  ")


if un==myDbValues[0] or psw==myDbValues[1]:
    print("Login Succesful")
else:
    print("Incorrect username or password")

