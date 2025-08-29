# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

# input('')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Mantém navegador aberto
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.google.com")
    input("Pressione Enter para sair...")

except WebDriverException as e:
    print("❌ Erro do WebDriver:", e)
except Exception as e:
    print("❌ Erro inesperado:", e)
