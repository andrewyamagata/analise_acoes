from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

input_busca = driver.find_element(By.ID, 'filled-normal')
input_busca.send_keys('PETR3.SA')
sleep(3)

input_busca.send_keys(Keys.ENTER)
sleep(3)

span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
cotacao_valor = span_val.text
print(f'Valor da cotação PETR3: {cotacao_valor}')

input('')