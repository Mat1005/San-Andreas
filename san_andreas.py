import os
import random
print("San Andreas")
input()
os.system("cls")
username = input("Inserisci nome utente: ")
print()
print("Grazie per aver risposto alla nostra chiamata", username, "!")
print("La città di San Francisco è alle prese con un terremoto di magnitudo 9.6!")
print("Rimangono 20 dispersi da soccorrere in 40 tentativi prima dell'arrivo della scossa! Buon Lavoro!")
print()
print("ISTRUZIONI")
print("gadgets: hai a disposizione 3 gadgets")
print("Razzo di segnalazione: puoi sapere se in quella casella c'è qualcuno o no. Utilizzo: 5")
print("Scanner termico: puoi sapere se in quella colonna c'è qualcuno o no. Utilizzo: 1")
print("Segnalatore acustico: puoi sapere se in quella line c'è qualcuno o no. Utilizzo: 1")
print("")
print("x: disperso salvato")
print("o: edificio vuoto")
print("!: presenza disperso")
input()
os.system("cls")
a = "[ ][A][B][C][D][E][F][G][H][I][J]"
b = "[0][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
c = "[1][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
d = "[2][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
e = "[3][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
f = "[4][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
g = "[5][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
h = "[6][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
i = "[7][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
j = "[8][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
k = "[9][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"

table = [a,b,c,d,e,f,g,h,i,j,k]

ran10 = [1,2,3,4,5,6,7,8,9,10]

dictionary={"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J": 10}

box_occupated = []
counter = 0
while counter < 20:
    first_lett = random.choice(ran10)
    first_n = random.choice(ran10)
    if str(first_lett) + "," + str(first_n-1) not in box_occupated:
        box_occupated.append(str(first_lett) + "," + str(first_n-1))
        counter = counter + 1

list_gadgets = [1, 1, 1, 1, 1, 2, 3]
counter = 0
while True:
    os.system("cls")
    if counter == 40 or len(box_occupated) == 0:
        break
    for e in table:
        print(e)
    print("Dispersi rimasti:", len(box_occupated))
    print("Tentativi rimasti:", 40-counter)
    print()
    if list_gadgets != []:
        yes_or_no = input("Vuoi usare un gadget?").upper()
        if yes_or_no == "SI":
            if 1 in list_gadgets:
                print("1. Razzo di segnalazione")
            if 2 in list_gadgets:
                print("2. Scanner termico")
            if 3 in list_gadgets:
                print("3. Segnalatore acustico")
            gadget = int(input("Seleziona un gadget inserendo il numero:"))
            if gadget not in list_gadgets:
                print("Gadget non utilizzabile")
                continue
            else:
                if gadget == 1:
                    print("Inserisci le coordinate in cui vuoi lanciare il razzo (es: A-5)")
                    drop = input()
                    drop = drop.split("-")
                    first_lett = dictionary[str(drop[0])]
                    first_n = int(drop[-1])
                    if str(first_lett) + "," + str(first_n) not in box_occupated:
                        line = table[first_n+1]
                        line = line[:3*first_lett+1] + "o" + line[3*first_lett+2:]
                        table[first_n+1] = line
                        print(str(first_lett) + "," + str(first_n))
                    elif str(first_lett) + "," + str(first_n) in box_occupated:
                        line = table[first_n+1]
                        line = line[:3*first_lett+1] + "!" + line[3*first_lett+2:]
                        table[first_n+1] = line
                        print(str(first_lett) + "," + str(first_n))
                    list_gadgets.remove(1)
                elif gadget == 2:
                    print("Inserisci la colonna in cui vuoi ispezionare con lo scanner (es: A)")
                    first_lett = input()            
                    for n in range(10):
                        if str(dictionary[first_lett]) + "," + str(n) not in box_occupated:
                            line = table[n+1]
                            line = str(line[:3*dictionary[first_lett]+1]) + "o" + str(line[3*dictionary[first_lett]+2:])
                            table[n+1] = line
                            print(str(first_lett) + "," + str(n))
                        elif str(dictionary[first_lett]) + "," + str(n) in box_occupated:
                            line = table[n+1]
                            line = str(line[:3*dictionary[first_lett]+1]) + "!" + str(line[3*dictionary[first_lett]+2:])
                            table[n+1] = line
                            print(str(first_lett) + "," + str(n))
                    list_gadgets.remove(2)
                elif gadget == 3:
                    print("Inserisci la line in cui vuoi ispezionare con il segnalatore (es: 5)")
                    first_n = int(input())
                    for l in dictionary:
                        if str(dictionary[l]) + "," + str(first_n) not in box_occupated:
                            line = table[first_n+1]
                            line = str(line[:3*dictionary[l]+1]) + "o" + str(line[3*dictionary[l]+2:])
                            table[first_n+1] = line
                            print(str(l) + "," + str(first_n))
                        elif str(dictionary[l]) + "," + str(first_n) in box_occupated:
                            line = table[first_n+1]
                            line = str(line[:3*dictionary[l]+1]) + "!" + str(line[3*dictionary[l]+2:])
                            table[first_n+1] = line
                            print(str(l) + "," + str(first_n))
                    list_gadgets.remove(3)
                continue
    print("Inserisci le coordinate in cui vuoi esplorare(es: A-5)")
    drop = input()
    drop = drop.split("-")
    first_lett = dictionary[str(drop[0])]
    first_n = int(drop[-1])
    if str(first_lett) + "," + str(first_n) not in box_occupated:
        line = table[first_n+1]
        line = line[:3*first_lett+1] + "o" + line[3*first_lett+2:]
        table[first_n+1] = line
        print(str(first_lett) + "," + str(first_n))
    elif str(first_lett) + "," + str(first_n) in box_occupated:
        line = table[first_n+1]
        line = line[:3*first_lett+1] + "x" + line[3*first_lett+2:]
        table[first_n+1] = line
        print(str(first_lett) + "," + str(first_n))
        box_occupated.remove(str(first_lett) + "," + str(first_n))
    counter += 1
for e in table:
    print(e)
if counter == 40:
    print("Hai dato il massimo", username, "ma le forze della natura hanno avuto la meglio!")
    if len(box_occupated) < 20:
        print("Grazie per aver salvato", 20-len(box_occupated), "persone")
elif len(box_occupated) == 0:
    print("Complimenti", username, "hai portato a termine la tua missione!")
