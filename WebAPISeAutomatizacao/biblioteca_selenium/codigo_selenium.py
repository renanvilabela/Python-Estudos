from selenium import webdriver
import time

#abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://www.hashtagtreinamentos.com/")

navegador.maximize_window()
botao_verde = navegador.find_element("class name", "botao-verde")

botao_verde.click()

time.sleep(10)