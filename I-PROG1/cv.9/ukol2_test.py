import ukol2

soubor = open("data.txt","r")

radky = soubor.readlines()

soubor.close()

seznam = []

for i in range(1,len(radky)):
    radek = radky[i]
    prvky = radek.split(",")

    bod = [ float(prvky[0]), float(prvky[1]), float(prvky[2]) ]

    seznam.append(bod)

matice = ukol2.spocitejVzdalenosti(seznam)

#print(vzdalenosti)

soubor1 = open("matice.txt","w")

for i in range(0,len(matice)):
    for j in range(0,len(matice[0])):
        soubor1.write(str(matice[i][j])+"\t")
    soubor1.write("\n")

soubor1.close()

minimum = ukol2.najdiMin(matice)
print(minimum)

prumVzdal = ukol2.spoctiPrumVzdal(matice)
print(prumVzdal)
