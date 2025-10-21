from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('que estou na página inicial do Google')
def step_open_google(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("https://www.google.com")
    time.sleep(1)

@when('eu pesquiso por "{termo}"')
def step_search_term(context, termo):
    caixa_busca = context.driver.find_element(By.NAME, "q")
    caixa_busca.send_keys(termo)
    caixa_busca.send_keys(Keys.RETURN)
    time.sleep(2)

@then('o primeiro resultado deve conter "{termo}"')
def step_verify_result(context, termo):
    primeiro_resultado = context.driver.find_element(By.CSS_SELECTOR, "h3")
    assert termo.lower() in primeiro_resultado.text.lower()
    print(f"✅ Primeiro resultado encontrado: {primeiro_resultado.text}")
    time.sleep(2)
    context.driver.quit()
