from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    

    def abrir(self):
        self.abrir_url("https://practicetestautomation.com/practice-test-login/")

    def preencher_email(self,email):
        self.digitar(self.Email_input, email)

    def preencher_senha(self,password):
        self.digitar(self.PASSWORD_INPUT, password)
    
    def clicar_login(self,):
        self.clicar(self.LOGIN_BUTTON)

    def fazer_login(self, username, password):
        self.digitar(self.EMAIL_INPUT, username)
        self.digitar(self.PASSWORD_INPUT, password)
        self.clicar(self.LOGIN_BUTTON)
