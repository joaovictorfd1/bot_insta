import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv_handler import CSVHandler

escolha = int(input("Qual o numero de seguidores por comentario?"))
url = str(input("Qual é a URL?"))


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path="P:\Python\Programas\BOT_Instagram\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_password = driver.find_element_by_xpath(
            "//input[@name='password']")
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)
        time.sleep(30)
        contador_comentarios = 0
        for i in range(1, 1000):
            self.comentar_sorteio(True)
            contador_comentarios = contador_comentarios + 1
            print(contador_comentarios)

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    def comentar_sorteio(self, repetir=False):
        driver = self.driver
        time.sleep(30)
        driver.get(url)

        try:
            csv = CSVHandler()
            if escolha == 1:
                comentarios = csv.open_csv("P:\\Python\\Programas\\BOT_Instagram\\planilhas\\111.csv")
            elif escolha == 2:
                comentarios = csv.open_csv("P:\\Python\\Programas\\BOT_Instagram\\planilhas\\2.csv")
            else:
                comentarios = csv.open_csv("P:\\Python\\Programas\\BOT_Instagram\\planilhas\\333normal.csv")
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2, 5))
            self.digite_como_uma_pessoa(
                random.choice(comentarios), campo_comentario)
            print(campo_comentario)
            time.sleep(random.randint(30, 40))
            driver.find_element_by_xpath(
                "//button[contains(text(), 'Publicar')]").click()
            time.sleep(60)
        except Exception as e:
            print(e)
            time.sleep(5)


joaoBot = InstagramBot('joaovictorffd1@gmail.com', ')
joaoBot.login()

