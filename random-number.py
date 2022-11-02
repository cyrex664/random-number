from random import randrange

magic_number = randrange(0, 100)

i = 0

while (True):
    answer = int(input("Podaj swoją propozycję liczby: "))
    if(answer > magic_number):
        print("Podana liczba jest za duża")
        continue
    elif(answer < magic_number):
        print("Podana liczba jest za mała")
        continue
    else:
        print("Brawo! Odgadłeś liczbę!")
        break