# Importa o Selenium para abrir e controlar o navegador
from selenium import webdriver  

# Importa Keys (ENTER, ESC, TAB, etc.) para simular teclas do teclado
from selenium.webdriver import Keys  

# Importa By para localizar elementos na página (por ID, XPATH, CSS, etc.)
from selenium.webdriver.common.by import By  

# Service permite configurar o ChromeDriver (quem "conversa" com o Chrome)
from selenium.webdriver.chrome.service import Service  

# WebDriver Manager baixa automaticamente a versão correta do ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  

# WebDriverWait e ExpectedConditions permitem "esperar" por elementos antes de interagir
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

# TimeoutException é usada para tratar casos em que o elemento não aparece no tempo esperado
from selenium.common.exceptions import TimeoutException  

# Função sleep para dar pequenas pausas no código (esperar carregamentos)
from time import sleep  


# ---------------- FUNÇÃO PARA FECHAR POPUP ----------------
def fechar_popup(driver, timeout=2):
    try:
        popup = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-close.fc-icon-button"))
        )
        popup.click()
        print("Pop-up fechado")
    except TimeoutException:
        pass  # se não aparecer, ignora e continua


# ---------------- CONFIGURAÇÃO DO NAVEGADOR ----------------
# Cria o navegador Chrome usando o ChromeDriver baixado pelo WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  

# Abre a página de cotações da UOL
driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

# Fecha o pop-up inicial, caso apareça
fechar_popup(driver)

sleep(2)


# ---------------- INTERAÇÃO COM A PÁGINA ----------------
# Localiza o campo de busca pelo ID
input_busca = driver.find_element(By.ID, 'filled-normal')

input_busca.clear()
input_busca.click()  # garante foco no campo

# Digita "PETR3.SA" no campo
# input_busca.send_keys('PETR3.SA')

palavra = "PETR3.SA"
for letra in palavra:
    input_busca.send_keys(letra)
    sleep(0.2)  # digitação "humana"



# Fecha pop-up, caso apareça após a digitação
fechar_popup(driver)


# Pressiona ENTER para buscar
# input_busca.send_keys(Keys.ENTER)
# sleep(3)

# Espera a sugestão correta aparecer e clica nela
sugestao = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'PETR3.SA')]"))
)
sugestao.click()


# Fecha pop-up, caso apareça após a busca
fechar_popup(driver)


# ---------------- PEGANDO O VALOR ----------------
# Localiza o span com o valor da cotação
span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
cotacao_valor = span_val.text

print(f'Valor da cotação PETR3: {cotacao_valor}')

# Mantém o navegador aberto até o usuário pressionar ENTER no terminal
input('')