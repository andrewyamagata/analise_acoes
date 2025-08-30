from selenium import webdriver  
from selenium.webdriver import Keys  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import TimeoutException  
from time import sleep  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  

driver.get('https://finance.yahoo.com/')

sleep(2)

input_busca = driver.find_element(By.ID, 'ybar-sbq')

input_busca.send_keys('PETR3.SA')

input_busca.send_keys(Keys.ENTER)

sleep(3)

span_val = driver.find_element(By.CSS_SELECTOR, "span[data-testid='qsp-price']")
cotacao_valor = span_val.text

print(f'Valor da cotação PETR3: {cotacao_valor}')

input('')

