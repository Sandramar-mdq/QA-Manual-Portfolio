from selenium import webdriver
from selenium.webdriver.common.by import By

# abrir navegador (precondición técnica)
driver = webdriver.Chrome()

# 1. abrir página
driver.get("https://the-internet.herokuapp.com/login")

# 2. ingresar usuario
driver.find_element(By.ID, "username").send_keys("tomsmith")

# 3. ingresar contraseña
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# 4. hacer click
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# 5. validar resultado esperado
mensaje = driver.find_element(By.ID, "flash").text

#if "You logged into a secure area!" in mensaje:
#    print("TEST PASÓ")
#else:
#    print("TEST FALLÓ")

assert "You logged into a secure area!" in mensaje

# cerrar navegador
driver.quit()