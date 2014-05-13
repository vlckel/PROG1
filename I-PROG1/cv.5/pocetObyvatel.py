file = open("kraje.csv","r")

lines = file.readlines()

pocetObyvatel = 0

for i in range(1,len(lines)):
    colums = lines[i].split(sep=";")
    rozdilKraj = int(colums[3])  - int(colums[4])
    print(colums[2]," ",rozdilKraj)
    pocetObyvatel += rozdilKraj
    #print(colums[3])

print("Pocet obyvatel je",str(pocetObyvatel))
