def vypocet(retezec):
    prvky = retezec.split(" ")
    cislo1 = float(prvky[0])
    cislo2 = float(prvky[2])

    if prvky[1] == "+":
        vysledek = cislo1 + cislo2
    elif prvky[1] == "-":
        vysledek = cislo1 - cislo2
    elif prvky[1] == "*":
        vysledek = cislo1 * cislo2
    elif prvky[1] == "/":
        vysledek = cislo1 / cislo2
    elif prvky[1] == "**":
        vysledek = cislo1 ** cislo2
    else:
        raise NotImplementedError("Nerozpoznany operator")

    return(vysledek)

testRetezec = "46.48 * 417.4"
vysledek = vypocet(testRetezec)
print(vysledek)
