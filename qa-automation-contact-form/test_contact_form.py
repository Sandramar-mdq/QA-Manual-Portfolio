import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://cac-tpfinal-turismo-completo.netlify.app/templates/formulario")
    yield driver
    driver.quit()

#completar form
def completar_form(driver, nombre, apellido, telefono, email, partida=None, vuelta=None):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "nombre").send_keys(nombre)
    driver.find_element(By.ID, "apellido").send_keys(apellido)
    driver.find_element(By.ID, "telefono").send_keys(telefono)
    driver.find_element(By.ID, "email").send_keys(email)
    #driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
    
    if partida is not None:
    
    if vuelta is not None:
    

def enviar_form(driver):
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    
#enviar form happy path. Validar el texto en nueva página (Formspree)
def test_envio_form_completo(driver):
    completar_form(driver, 
                   "andreas", 
                   "benitez",
                   "221323223", 
                   "andreasben@hotmail.com")
    enviar_form(driver)
    
    wait = WebDriverWait(driver, 10)

    mensaje = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    ).text

    assert "El formulario ha sido enviado con éxito." in mensaje



#enviar form con todos los datos vacios. Mensaje con alert de JavaScript
def test_todos_campos_vacios(driver):
    completar_form(driver, "", "", "", "")
    enviar_form(driver)

    alerta = driver.switch_to.alert
    assert "Por favor completá todos los campos obligatorios" in alerta.text

    alerta.accept()



#enviar form con nombre vacío. validación nativa HTML5, viene del navegador. required → campo vacío
def test_form_nombre_vacio(driver):
    completar_form(driver, 
                   "", #nombre vacio
                   "Dominguez", 
                   "22345123", 
                   "sandramarmdq@gmail.com")
    enviar_form(driver)
    
    #validar mensajede error
    campo_nombre = driver.find_element(By.ID, "nombre")
    mensaje = campo_nombre.get_attribute("validationMessage")

    assert "Completa este campo" in mensaje



#enviar form con email vacio, Mensaje con alert de JavaScript
def test_email_vacio(driver):
    completar_form(driver, 
                   "Sandra", 
                   "Villar", 
                   "123456", 
                   "")  #email vacio
    enviar_form(driver)

    alerta = driver.switch_to.alert
    assert "Por favor completá todos los campos obligatorios" in alerta.text

    alerta.accept()



#enviar form con formato email incorrecto. Validación nativa del navegador (HTML5). type = email
def test_email_invalido(driver):
    completar_form(driver, 
                   "Sandra", 
                   "Villar", 
                   "123456", 
                   "sandramdqgmail.com") #email con formato incorrecto
    enviar_form(driver)

    campo_email = driver.find_element(By.ID, "email")
    mensaje = campo_email.get_attribute("validationMessage")

    assert "@" in mensaje

def test_fecha_regreso_anterior_a_partida(driver):
    completar_form(driver, 
                   "Nahuel", 
                   "Mauger", 
                   "221434343", 
                   "nahu@gmail.com", 
                   "2026-04-30", # Partida 
                   "2026-04-14") # Vuelta (antes)
    
    enviar_form(driver)
    
    wait = WebDriverWait(driver, 10)

    mensaje = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    ).text

    assert "El formulario ha sido enviado con éxito." in mensaje      #Envia normalmente el formulario, con las fechas mal.


    
def test_fecha_partida_en_pasado(driver):
    completar_form(driver, 
                    "Rigoberto", 
                    "Tanatis", 
                    "22122113312", 
                    "rigober@gmail.com", 
                    "2026-03-12") # PARTIDA: fecha anterior a la el sistema
    
    enviar_form(driver)
    
    wait = WebDriverWait(driver, 10)
    mensaje =wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    ).text
    
    assert  "El formulario ha sido enviado con éxito." in mensaje      #El sistema permite fechas inválidas
    
    
    


    


