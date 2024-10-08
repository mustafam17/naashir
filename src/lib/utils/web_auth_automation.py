from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pydantic import HttpUrl

from config.environment import CHROME_BINARY_PATH
from lib.utils.url_helpers import parse_auth_code_from_url


def get_auth_code_from_request_url(
    auth_request_url: HttpUrl, email: str, password: str
):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    chrome_options.binary_location = CHROME_BINARY_PATH

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    driver.get(auth_request_url)

    # Input email and click next button
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "loginfmt"))
    )
    email_input = driver.find_element("name", "loginfmt")
    email_input.send_keys(email)
    driver.find_element("id", "idSIButton9").click()

    # Input password and click Sign In button
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "passwd"))
    )
    password_input = driver.find_element("name", "passwd")
    password_input.send_keys(password)
    driver.find_element("id", "idSIButton9").click()

    # Click "No" button to the remember password prompt
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "declineButton"))
    )
    driver.find_element("id", "declineButton").click()

    # Allow redirection and collect URL
    WebDriverWait(driver, 10).until(lambda d: d.current_url != auth_request_url)
    redirect_url = driver.current_url
    auth_code = parse_auth_code_from_url(redirect_url)

    driver.quit()

    return auth_code
