from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# abrir o navegador
driver = webdriver.Chrome()
driver.get("https://github.com/renanvilabela")
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    botao_repos = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/renanvilabela?tab=repositories']"))
    )

    botao_repos.click()
    print("Botão de repositórios clicado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

time.sleep(5)
driver.quit()
