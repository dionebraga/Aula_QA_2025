from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Inicializa o navegador com o WebDriver Manager (dispensa driver manual)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # 1️⃣ Acessar o Google
    driver.get("https://www.google.com")

    # 2️⃣ Localizar e aceitar cookies (se aparecer)
    try:
        aceitar = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aceitar')]"))
        )
        aceitar.click()
    except:
        pass  # se não aparecer, continua normalmente

    # 3️⃣ Buscar por "Instituto Joga Junto"
    caixa_busca = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    caixa_busca.send_keys("Instituto Joga Junto")
    caixa_busca.send_keys(Keys.RETURN)

    # 4️⃣ Aguardar carregamento e clicar no primeiro resultado válido
    primeiro_resultado = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a h3"))
    )
    print("✅ Primeiro resultado encontrado:", primeiro_resultado.text)
    primeiro_resultado.click()

    # 5️⃣ Esperar para visualizar o site
    WebDriverWait(driver, 10).until(EC.title_contains("Joga Junto"))
    print("🌐 Página aberta com sucesso!")

finally:
    # 6️⃣ Fechar navegador
    driver.quit()
