from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .base_page import BasePage

class DashboardPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")

    def esta_logado(self): # Retorna True/False
        if "/logged-in-successfully/" in self.driver.current_url:
            return True
        else:
            return False

    def obter_mensagem_boas_vindas(self):
        return self.obter_texto(self.SUCCESS_MESSAGE)