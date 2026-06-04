from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

#usuario valido
driver.find_element(By.ID, "username").send_keys("tomsmith")

#contraseña invalida
driver.find_element(By.ID, "password").send_keys("1234")

#login
driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

#validar mensajede error. aqui busca el elemento "flash" y obtiene su texto y assert evalua si es verdadero o no
mensaje = driver.find_element(By.ID, "flash").text

assert "Your password is invalid" in mensaje

driver.quit

