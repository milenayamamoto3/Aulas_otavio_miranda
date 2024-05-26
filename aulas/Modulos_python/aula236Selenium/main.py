# type: ignore
# a tipagem acima foi ignorada por completo

# Selenium - Automatizando tarefas no navegador

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / "drivers" / "chromedriver.exe"

# Maneira 1

# chrome_options = webdriver.ChromeOptions()
# chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
# chrome_browser = webdriver.Chrome(
#     service=chrome_service,
#     options=chrome_options,
# )

# chrome_browser.get("https://www.google.com")
# sleep(10) #10segundos com o google aberto

# Maneira 2


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless') #não abrir interface browser
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get("https://www.google.com")

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "APjFqb"))
    )

    search_input.send_keys("Hello World!")
    search_input.send_keys(Keys.ENTER)  # comando para 'ENTER'

    # result = todos os resultados id='search'
    result = browser.find_element(By.ID, "search")
    # links = links do resultado pela tag 'a'
    links = result.find_elements(By.TAG_NAME, "a")
    links[0].click()  # executa o click do primeiro link

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
