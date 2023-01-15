 
import random

print("uloha 1")
y = input("zadane cislo: ")
belko = [int(y)] * (50 + int(y))
adam = [None] * len(belko)

#U2
print("uloha 2")
for i in range(0, len(belko)):
    adam[i] = belko[i]
    
print(belko)
print(adam)
input("Enter.............")

# U3
print("uloha 3")
a = 0
for i in range(1, int(y)):
    print(i)
    belko[i] = int(i)
    if(a == 7):
        t = input("stojim a cakam")
    a += 1
    
belko[0] = "belko"
belko.append(int(5000))

print(belko)
input("Enter.............")

#U4
print("uloha 4")
f = open('body250a50.txt', 'r')
print('polozky v subore: ')
print(f.read())
print('koniec poloziek v subore ')

lines = f.readlines()
numbers = []

with open('body250a50.txt') as lines:
    numbers = [int(i) for i in lines]

x = int(y) # z nejakeho zaujimaveho dovodu to ma problem s premenou y

for i in range(0, x and len(numbers)):
    adam[i+1] = numbers[i]
    

adam[0] = 3.1415
print(adam)

hodnota = range(45, 60)
if(adam[5] in hodnota):
    print(f"Hodnota prvku 5: {adam[5]} je v rozsahu 45-60")
else:
    print(f"Hodnota prvku 5: {adam[5]} NENI v rozsahu 45-60")

#U5
print("uloha 5")
list_length = x
sumOfElements=0
countOfElements=0

for i in range(1, list_length+1):
    sumOfElements=sumOfElements+belko[i]

for i in range(1, list_length+1):
    countOfElements += 1

priemer = sumOfElements / countOfElements

sumOfElements2 = 0
countOfElements2 = 0
g = 5
for i in range(0, 13):
    sumOfElements2 = sumOfElements2 + belko[g]
    g += 1

for i in range(0, 13):
    countOfElements2 =+ 1
    g += 1
priemer2 = sumOfElements2 / countOfElements2


belko2_parne = 0
for i in range(1, x):
    if((belko[i]%2) == 0):
        belko2_parne = belko2_parne + belko[i]

print("Sucet je : ", sumOfElements)
print("Pocet je : ", countOfElements)
print("Priemer je : ", priemer)
print("Priemer je od 5 a 17 cisla je  : ", priemer2)
print("Scitane parne cisla z pola: ", belko2_parne)

adam_tupple = tuple(adam)
print(adam_tupple)
adam_tupple = list(adam_tupple)
adam_tupple[3] = 500
adam_tupple = tuple(adam_tupple)
print(adam_tupple)

input("Enter................")

#U6
print("uloha 6")
def sum(y,x, array):
    vysledok = 0
    for i in range(y, x):
        vysledok = vysledok + array[i]
    return vysledok

vysledok = sum(4, int(x), belko)

print("dostali sme: ", vysledok)

#U7
print("uloha 7")
dvojrozmerne_pole = [[18, 21, 23], [14, 15, 63], [27, 81, 19],[37, 81, 79]]
dvojrozmerne_pole[1][2] = 18
print(dvojrozmerne_pole)

#U8
print("uloha 8")
def zobraz_maticu(pole):
    for x in pole: 
        for i in x:  # inner loop  
            print(i, end = " ") # print the elements  
        print()  

zobraz_maticu(dvojrozmerne_pole)

#U9
print("uloha 9")
pocet = 1

with open("belko20.txt",'r+') as belko20:
    belko20.truncate(0)

while True:
    s = open("belko20.txt", "a")
    s.write(str(pocet) + '\n')
    s.close()
    print(pocet)
    pocet += 1
    if(int(pocet) == 21 or int(pocet) > x):
        print("program ukonceny ")
        break
