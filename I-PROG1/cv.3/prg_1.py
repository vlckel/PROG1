pocetRadku = int(input("Zadej počet řádků: "))
pocetPrvku = int(input("Zadej počet prvků: "))

for i in range(0,pocetRadku):
    for j in range(0,pocetPrvku):
        hodnota = i*pocetPrvku + j
        print(hodnota, end=" ")
    print()
