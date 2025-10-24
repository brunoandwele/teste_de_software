import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_login_credenciais_valida():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("student", "Password123")

        assert "Logged In Successfully" in driver.page_source
        print("Login Efetuado com sucesso!")
    finally:
        driver.quit()

def test_login_email_invalido():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("teacher", "Password123")

        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")
    finally:
        driver.quit()

def test_login_senha_incorreta():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("student", "test123")

        assert "Your password is invalid!" in driver.page_source
        print("Senha informada inválida")
    finally:
        driver.quit()

def test_login_sem_preencher_campos():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("", "")

        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")
    finally:
        driver.quit()

def test_login_verificar_mensagens_erro_apropriadas():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("student", "Password123")

        assert "Logged In Successfully" in driver.page_source
        print("Login Efetuado com sucesso!")

        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("teacher", "Password123")

        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")

        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("student", "test123")

        assert "Your password is invalid!" in driver.page_source
        print("Senha informada inválida")

        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("", "")

        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")

    finally:
        driver.quit()