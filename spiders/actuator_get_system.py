from selenium import webdriver


""""
    Função responsável por acessar o sistema alvo
"""

def get_system(url, xpath):
    """
       Existe um bug do ChromeDriver ao rodar o selenium pela linha de comando,
       as linhas 13 e 14 contornam esse problema
       """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    return driver, driver.find_elements_by_xpath(xpath)
