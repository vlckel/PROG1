import random

cisla = []

for i in range(0,10000):
    cisla.append(random.randint(0,100))


indexy = []
cislaInterval = []
for j in range(0,len(cisla)):
    hodnota = cisla[j]
#for hodnota in cisla:
    if hodnota>=25 and hodnota<=37:
        indexy.append(j)
    if hodnota>=90 and hodnota<=95:
       cislaInterval.append(hodnota)
       

print(indexy)
print(cislaInterval)
