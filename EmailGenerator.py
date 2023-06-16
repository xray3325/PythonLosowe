from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

alfabet = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z','!','@','#','$','%','*','&','?']

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()

def Generuj():
    imie = GenerujImNaNi()
    nazwisko = GenerujImNaNi()
    haslo = GenerujHaslo()
    dzien = random.randrange(1,28)
    rok = random.randrange(1960,2000)
    Utworz(imie, nazwisko, haslo, dzien, rok)

def GenerujImNaNi():
    wynik = []
    i = random.randrange(8,12)
    while i > 0:
        wynik.append(alfabet[random.randrange(10, 33)])
        i -= 1
    return ''.join(wynik)

def GenerujHaslo():
    haslo = []
    i = random.randrange(18,24)
    while 0 < i:
        if random.randint(0,1) == 0: haslo.append(alfabet[random.randrange(0,41)]); haslo.append(alfabet[random.randrange(0,41)].capitalize())
        i -= 1
    return(''.join(haslo))

def Utworz(imie, nazwisko, haslo, dzien, rok):
    driver.get('https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe')
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/button[3]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[1]/input').send_keys(imie)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(nazwisko)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[1]/input').send_keys(dzien)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[3]/input').send_keys(rok)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[5]/div[1]/input').send_keys()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(haslo)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="rePassword"]').send_keys(haslo)
    time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, 'icon-arrow-right-full').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/ul/li[6]/span[1]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/div[2]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/ul/li[1]/span[1]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/div[1]/div[1]/label/div/div').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/button').click()

    ZapisaneKonta(imie, nazwisko, haslo)

def ZapisaneKonta(imie, nazwisko, haslo):
    login = '%s.%s' % (imie, nazwisko)
    file = open('/home/xray/Desktop/programowanie/KontaInteria.txt', 'a')
    file.write('login: ' + login + ' haslo: ' + haslo + '\n')
    file.close()

Generuj()
