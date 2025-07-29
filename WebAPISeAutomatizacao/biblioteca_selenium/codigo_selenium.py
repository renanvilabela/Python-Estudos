from selenium import webdriver
import time

#abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://github.com/renanvilabela")

navegador.maximize_window()
time.sleep(7)