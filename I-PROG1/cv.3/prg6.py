radky = int(input("Zadej počet řádků: "))
prvky = int(input("Zadej počet prvků: "))

for i in range(0, radky):
    for j in range(0, prvky):
        hodnota = i*prvky + j 
        print(hodnota, end=" ")
    print()    
