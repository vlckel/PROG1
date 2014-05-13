import random

soubor = open("data.txt","w")

soubor.write("x,y,z\n")

for i in range(0,100):
    x = random.randint(40,50)
    y = (random.random() * 5) + 25
    z = random.gauss(5,4)
    retezec = str(x) + "," + str(y) + "," + str(z) + "\n"
    soubor.write(retezec)

soubor.close()
