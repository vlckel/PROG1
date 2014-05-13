def divisionCheck(number):
    for i in range(3,10):
        if number%i == 0:
            print("Číslo",number,"je bezezbytku dělitelné číslem",i)


number = float(input("Zadej číslo: "))
divisionCheck(number)
