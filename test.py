from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()

def home():
    url="http://3.146.35.171/"
    driver.get(url)
    time.sleep(6)

def first_access_denied(): 
    btn_register_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[3]/button')
    btn_register_activity.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)


    btn_search_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[4]/button')
    btn_search_activity.click() 
    time.sleep(3)


    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #Intento acceder con usuario inexistente 

def user_not_existant():

    field_name = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[1]')
    field_name.send_keys('UsuarioInexistente')
    time.sleep(1) 

    field_password = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[2]')
    field_password.send_keys('contraseñaincorrecta')
    time.sleep(1)

    btn_logIn = driver.find_element(By.XPATH, '//*[@id="log"]/form/button')
    btn_logIn.click() 
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #Acceso con usuario registrado
def first_registered_user():
    btn_access = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[2]/button')
    btn_access.click()
    time.sleep(3)

    field_name = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[1]')
    field_name.send_keys('Camilo')
    time.sleep(1)

    field_password = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[2]')
    field_password.send_keys('123')
    time.sleep(1)

    btn_logIn = driver.find_element(By.XPATH, '//*[@id="log"]/form/button')
    btn_logIn.click()
    time.sleep(6)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    #aqui ya ingrese
    #Añadiendo actividad

    btn_register_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[3]/button')
    btn_register_activity.click()
    time.sleep(6)

    field_start_hour = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[1]/input')
    field_start_hour.send_keys('7:00 a.m')
    time.sleep(1)

    field_end_hour = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[2]/input')
    field_end_hour.send_keys('8:30 a.m')
    time.sleep(1)

    field_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[3]/input')
    field_activity.send_keys('Revisión de Material de Impresión')
    time.sleep(1)

    field_description = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[4]/input')
    field_description.send_keys('Se revisa el inventario de todos los materiales de impresión')
    time.sleep(1)

    btn_add_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/button')
    btn_add_activity.click() 
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #actividad añadida
    #consulta de actividades

    btn_search_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[4]/button')
    btn_search_activity.click() 
    time.sleep(6)

    field_search_user = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/input')
    field_search_user.send_keys('Camilo') 
    time.sleep(1)

    btn_check_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/button')
    btn_check_activity.click()
    time.sleep(10)

    link_logOut = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[2]/button')
    link_logOut.click() 
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #segundo usuario registrado
def second_registered_user():
    btn_access = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[2]/button')
    btn_access.click()
    time.sleep(6)

    field_name = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[1]')
    field_name.send_keys('Alejandro')
    time.sleep(1)

    field_password = driver.find_element(By.XPATH, '//*[@id="log"]/form/input[2]')
    field_password.send_keys('sfT#')
    time.sleep(1)

    btn_logIn = driver.find_element(By.XPATH, '//*[@id="log"]/form/button')
    btn_logIn.click()
    time.sleep(6)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    #aqui ya ingrese
    #Añadiendo actividad

    btn_register_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[3]/button')
    btn_register_activity.click()
    time.sleep(6)

    field_start_hour = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[1]/input')
    field_start_hour.send_keys('1:00 p.m')
    time.sleep(1)

    field_end_hour = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[2]/input')
    field_end_hour.send_keys('3:00 p.m')
    time.sleep(1)

    field_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[3]/input')
    field_activity.send_keys('Impresión de pieza: dinosaurio')
    time.sleep(1)

    field_description = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/table/tbody/tr[2]/td[4]/input')
    field_description.send_keys('Se imprime la pieza:dinosaurio de color verde con marrón.')
    time.sleep(1)

    btn_add_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/button')
    btn_add_activity.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #actividad añadida
    #consulta de actividades

    btn_search_activity = driver.find_element(By.XPATH, '//*[@id="home-nav"]/li[4]/button')
    btn_search_activity.click() 
    time.sleep(6)

    field_search_user = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/input')
    field_search_user.send_keys('Alejandro') 
    time.sleep(1)

    btn_check_activity = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[1]/button')
    btn_check_activity.click() 
    time.sleep(10)

    link_logOut = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form[2]/button')
    link_logOut.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)

home()
first_access_denied()
user_not_existant()
first_registered_user()
second_registered_user()