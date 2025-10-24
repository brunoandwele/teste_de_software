import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    """Testa buscas no Google com diferentes termos."""
    driver = chrome_driver
    driver.get("https://www.google.com")

    # Caixa de pesquisa
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(termo_busca)
    search_box.submit()

    # Espera simples (poderia usar WebDriverWait)
    time.sleep(2)

    page_text = driver.page_source.lower()
    assert termo_busca.lower() in page_text, f"'{termo_busca}' não encontrado nos resultados."