import unittest
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPalindrome(unittest.TestCase):
    # Setup
    def setUp(self):
        filePath = 'credenciales.xls'
        self.df = pandas.read_excel(filePath)
        self.user = self.df['usuario'][0]
        self.pwd = self.df['contraseña'][0]
        self.url = 'https://www.linkedin.com'
        self.driver = webdriver.Chrome()
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        print(self.driver.execute_script("return navigator.userAgent;"))
    
    # Test user not exist
    def test_user_not_exist(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        
        button_login = "/html/body/nav/div/a[2]"
        self.driver.find_element_by_xpath(button_login).click()

        new_url = self.driver.current_url
        self.driver.get(new_url)
        
        input_username = '//*[@id="username"]'
        self.driver.find_element_by_xpath(input_username).send_keys(self.user)

        input_password = '//*[@id="password"]'
        self.driver.find_element_by_xpath(input_password).send_keys(self.pwd)

        button_log = '//*[@id="organic-div"]/form/div[3]/button'
        self.driver.find_element_by_xpath(button_log).click()

        #self.assertEquals("https://www.linkedin.com/checkpoint/lg/login-submit", self.driver.current_url)
        expected_message = "No se ha encontrado ninguna cuenta de LinkedIn asociada a este email. Vuelve a intentarlo." 
        error_selector = self.driver.find_element_by_xpath('//*[@id="error-for-username"]')
        # import ipdb; ipdb.set_trace()
        self.assertEquals(expected_message, error_selector.text)

    # Test user not exist
    def test_password_is_incorrect(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        
        button_login = "/html/body/nav/div/a[2]"
        self.driver.find_element_by_xpath(button_login).click()

        new_url = self.driver.current_url
        self.driver.get(new_url)
        
        input_username = '//*[@id="username"]'
        self.driver.find_element_by_xpath(input_username).send_keys(self.user)

        input_password = '//*[@id="password"]'
        self.driver.find_element_by_xpath(input_password).send_keys(self.pwd)

        button_log = '//*[@id="organic-div"]/form/div[3]/button'
        self.driver.find_element_by_xpath(button_log).click()

        #self.assertEquals("https://www.linkedin.com/checkpoint/lg/login-submit", self.driver.current_url)
        expected_message = "Esa no es la contraseña. " 
        error_selector = self.driver.find_element_by_xpath('//*[@id="error-for-password"]')
        self.assertEquals(expected_message, error_selector.text)    
        
    

if __name__=='__main__':
    unittest.main()