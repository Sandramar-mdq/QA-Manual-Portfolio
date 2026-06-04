from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def hacer_login(driver, usuario, contraseña):
    # ingresar usuario
    driver.find_element(By.ID, "username").send_keys(usuario)

    # ingresar contraseña
    driver.find_element(By.ID, "password").send_keys(contraseña)

    # hacer click
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    
def test_login(driver):
    hacer_login(driver, "tomsmith", "SuperSecretPassword!")    
 
    #validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in mensaje


def test_login_invalido(driver):
    hacer_login(driver, "tomsmith", "1234") 

    #validar mensajede error. aqui busca el elemento "flash" y obtiene su texto y assert evalua si es verdadero o no
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your password is invalid" in mensaje

    
def test_campos_vacios(driver):
    hacer_login(driver, "", "") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje


    
def test_usuario_incorrecto(driver):
    hacer_login(driver, "pepe", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text
   
    assert "Your username is invalid!" in mensaje


    
def test_sin_contraseña(driver):
    hacer_login(driver, "tomsmith", "") 
    
    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your password is invalid!" in mensaje


    
def test_espacios_en_lugar_de_usuario(driver):
    hacer_login(driver, "   ", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje


    
def test_usuario_en_mayusculas(driver):
    hacer_login(driver, "TOMSMITH", "SuperSecretPassword!") 

    # validar resultado esperado
    mensaje = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in mensaje


