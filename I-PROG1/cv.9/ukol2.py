import math

def spocitejVzdalenosti(body):

    matice = []

    for i in range(0,len(body)):
        bod = body[i]
        radek = []

        for j in range(0,len(body)):
            bod2 = body[j]

            vzdalenost1 = math.sqrt((bod[0]-bod2[0])**2 + (bod[1]-bod2[1])**2)
            vzdalenost = math.sqrt(vzdalenost1**2 + (bod[2]-bod2[2])**2)

            radek.append(vzdalenost)

        matice.append(radek)

    return(matice)


def najdiMin(matice):
    minimum = 9999

    for i in range(0,len(matice)):
        for j in range(0, len(matice[0])):
            if i!=j:
               if matice[i][j]<minimum:
                   minimum = matice[i][j]
    return(minimum)

def spoctiPrumVzdal(matice):
    suma = 0
    pocet = 0
    
    for i in range(0,len(matice)):
        for j in range(0, len(matice[0])):
            if i!=j:
                suma = suma + matice[i][j]
                pocet = pocet + 1

    prumer = suma / pocet
    return(prumer)

#body = [ [0,0,0],
#         [1,1,1],
#         [2,2,2]]

#vzdalenosti = spocitejVzdalenosti(body)

#print(vzdalenosti)

