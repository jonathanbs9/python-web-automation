import pandas
import time
from selenium import webdriver
from selenium.webdriver.support.by import By
from selenium.webdriver.suport.ui import WebDriverWait
from selenium.webdriver.support import expected_conditiones as ec


excel_credenciales = ""
df = pandas.read_excel(excel_credenciales)
user = df['usuario'][0]
pwd = df['contraseña'][0]

url = 'https://www.linkedin.com/'

# Selectores
boton_inicio_sesion =  ''
selector_usuario = ''
selector_contraseñ = '' 
boton_login = ''

# Navegador 
driver = webdriver.Chrome()

# Maximizar pantalla
driver.maximize_window()

driver.get(url)
driver.find