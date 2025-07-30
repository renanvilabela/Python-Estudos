from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# abrir o navegador
navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")
navegador.maximize_window()

# espera o botão carregar
wait = WebDriverWait(navegador, 20)
botao_verde = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "botao-verde")]')))

# força o clique via JavaScript
navegador.execute_script("arguments[0].click();", botao_verde)

time.sleep(10)
