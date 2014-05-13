radky = int(input("Zadej počet řádků: "))

for i in range(1, radky+1):
    for j in range(1, i+1):
        print("!", end=" ")
    print()    
