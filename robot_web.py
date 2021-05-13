import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import ipdb; ipdb.set_trace()

excel_credenciales = "credenciales.xls"
df = pandas.read_excel(excel_credenciales)
user = df['usuario'][0]
pwd = df['contraseña'][0]

url = 'https://www.linkedin.com/'

# Selectores

boton_inicio_sesion =  'body > nav > div > a.nav__button-secondary'
selector_usuario = 'username'
selector_contraseña = '//*[@id="password"]' 
boton_login = '#organic-div > form > div.login__form_action_container > button'



# Navegador 
driver = webdriver.Chrome()

# Maximizar pantalla
driver.maximize_window()
driver.get(url)

# Acciones de la página. Hace click en el boton para ir a la página de inicio de sesión
driver.find_element_by_css_selector(boton_inicio_sesion).click()

# Ingresamos usuario y contraseña a los campos
driver.find_element_by_id(selector_usuario).send_keys("user")
driver.find_element_by_xpath(selector_contraseña).send_keys(pwd)
driver.find_element_by_css_selector(boton_login).click()

# Realizamos una espera de 5 segundos
#time.sleep(5)

# Cerramos el driver
#driver.quit()