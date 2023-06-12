from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

alfabet = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z','!','@','#','$','%','*','&','?']

driver = webdriver.Chrome("chromedriver")

def Generuj():
    imie = GenerujImNaNi()
    nazwisko = GenerujImNaNi()
    nick = GenerujImNaNi()
    haslo = GenerujHaslo()
    dzien = random.randrange(1,28)
    miesiac = random.randrange(1,12)
    rok = random.randrange(1960,2000)
    Utworz(imie, nazwisko, nick, haslo, dzien, miesiac, rok)

def GenerujImNaNi():
    wynik = []
    i = random.randrange(8,12)
    while i > 0:
        wynik.append(alfabet[random.randrange(10, 33)])
        i -= 1
    return ''.join(wynik)

def GenerujHaslo():
    haslo = []
    i = random.randrange(20,28)
    while 0 < i:
        if random.randint(0,1) == 0: haslo.append(alfabet[random.randrange(0,41)]); haslo.append(alfabet[random.randrange(0,41)].capitalize())
        i -= 1
    return(''.join(haslo))

def Utworz(imie, nazwisko, nick, haslo, dzien, miesiac, rok):
    driver.get('https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe')
    driver.find_element(By.CLASS_NAME, '_2E5n5j0h7xvs07').send_keys(imie)

Generuj()
