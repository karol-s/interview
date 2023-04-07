from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_logging_negative():
    service_obj = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    driver.get("https://dev.profil-software.com/estimate-project")

    driver.find_element(By.CSS_SELECTOR, "#first_name").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "#last_name").send_keys("user")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("testusergmail.com")
    driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("777888999")
    driver.find_element(By.CSS_SELECTOR, "#describe").send_keys("My custom project")
    driver.find_element(By.XPATH, "//span[text()='Select all']").click()

    # CLICK COOKIES ACCEPT
    driver.switch_to.alert("")

    driver.find_element(By.CSS_SELECTOR,
                        'div[class="EstimateFormHeader-module--buttonsRow--1b5ce"] button[form="estimation"]').click()

    warning = driver.find_element(By.CSS_SELECTOR, "#email-helper-text").text
    assert warning == "* Please, enter valid email"
