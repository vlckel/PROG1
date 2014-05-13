def najdiPodretezce(L, S):
    seznam = []
    for retezec in L:
        if S in retezec:
            seznam.append(retezec)
        #print(retezec)
    return(seznam)

seznam = ["test1","test2","test4","test42","tset1"]
retezec = "test"
vysledek = najdiPodretezce(seznam, retezec)
print(vysledek)
retezec = "4"
vysledek = najdiPodretezce(seznam, retezec)
print(vysledek)
