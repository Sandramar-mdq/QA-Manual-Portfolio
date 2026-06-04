from selenium import webdriver
from selenium.webdriver.common.by import By

def abrir_pagina():
    # abrir navegador (precondición técnica)
    driver = webdriver.Chrome()

    # 1. abrir página
    driver.get("https://the-internet.herokuapp.com/login")
    return driver

def hacer_login(driver, usuario, contraseña):
    # ingresar usuario
    driver.find_element(By.ID, "username").send_keys(usuario)

    # ingresar contraseña
    driver.find_element(By.ID, "password").send_keys(contraseña)

    # hacer click
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    
def test_login():
    driver = abrir_pagina()
    hacer_login(driver, "tomsmith", "SuperSecretPassword!")    
 
    #validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in mensaje

    # cerrar navegador
    driver.quit()

def test_login_invalido():
    driver = abrir_pagina()
    hacer_login(driver, "tomsmith", "1234") 

    #validar mensajede error. aqui busca el elemento "flash" y obtiene su texto y assert evalua si es verdadero o no
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your password is invalid" in mensaje

    driver.quit()
    
def test_campos_vacios():
    driver = abrir_pagina()
    hacer_login(driver, "", "") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje

    # cerrar navegador
    driver.quit()
    
def test_usuario_incorrecto():
    driver = abrir_pagina()
    hacer_login(driver, "pepe", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text
   
    assert "Your username is invalid!" in mensaje

    # cerrar navegador
    driver.quit()
    
def test_sin_contraseña():
    driver = abrir_pagina()
    hacer_login(driver, "tomsmith", "") 
    
    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your password is invalid!" in mensaje

    # cerrar navegador
    driver.quit()
    
def test_espacios_en_lugar_de_usuario():
    driver = abrir_pagina()
    hacer_login(driver, "   ", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje

    # cerrar navegador
    driver.quit()
    
def test_usuario_en_mayusculas():
    driver = abrir_pagina()
    hacer_login(driver, "TOMSMITH", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje

    # cerrar navegador
    driver.quit()
    

if __name__ == "__main__":
    test_login()
    test_login_invalido()
    test_campos_vacios()
    test_usuario_incorrecto()
    test_sin_contraseña()
    test_espacios_en_lugar_de_usuario()
    test_usuario_en_mayusculas()
    