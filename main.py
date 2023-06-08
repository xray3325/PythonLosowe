import random


alfabet = ['0','1','2','3','4','5','6','7','8','9','a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż','!','@','#','$','%','*']
haslo = []
ZnakiSpecjalne = int(input("Czy chcesz użyć znaków specjalnych w swoim haśle? "))
Liczby = int(input("Czy chesz użyć liczb w swoim haśle? "))
Długość = int(input("Podaj długość swojego hasła: "))
i = 0;
while i < Długość:
    if ZnakiSpecjalne == 1 and Liczby == 1:
        letter = random.randrange(0,48)
    elif ZnakiSpecjalne == 1 and Liczby == 0:
        letter = random.randrange(10,48)
    elif ZnakiSpecjalne == 0 and Liczby == 1:
        letter = random.randrange(0,42)
    elif ZnakiSpecjalne == 0 and Liczby == 0:
        letter = random.randrange(10,42)
    if bool(random.getrandbits(1)) == True:
        haslo.append(alfabet[letter])
    else:
        haslo.append(alfabet[letter].capitalize())
    i += 1
print(*haslo, sep='')