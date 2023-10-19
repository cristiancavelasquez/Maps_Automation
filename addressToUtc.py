# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:43:40 2023

@author: cvelasquez
"""

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import Tk, Label, Entry, Button, messagebox
import sys
import time
import pandas as pd
from selenium.common.exceptions import TimeoutException

def iniciar_busqueda():
    # Obtener los valores de los campos de entrada
    url = 'http://3.12.247.123/closeup-app/public/'
    email = 'mapas@test.com'
    password = '123456'

    # Ruta al chromedriver descargado
    PATH = r"C:\Users\cvelasquez\Documents\automatizaciones\busqueda_utcs\chromedriver.exe"

    # Configurar opciones del driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") # Abre la ventana del navegador maximizada
    options.add_argument("--disable-extensions") # Desactiva las extensiones del navegador

    # Crear un objeto Service con la ruta al chromedriver
    service = Service(PATH)

    # Crear una instancia del driver de Chrome
    driver = webdriver.Chrome(service=service, options=options)

    # Abrir la página web
    driver.get(url)
    

    # Encontrar y hacer clic en el botón
    # Esperar hasta que se cargue el botón de detalles

    # Esperar a que el elemento "loader-wrapper" desaparezca de la página
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loader-wrapper")))

    # Esperar a que el elemento "btn_login" esté presente y sea clicleable
    btn_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_login")))

    # Hacer clic en el botón "btn_login"
    btn_login.click()
    
    # Encontrar el campo de correo electrónico y llenarlo con un valor
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(email)

    # Encontrar el campo de contraseña y llenarlo con un valor
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Esperar a que el elemento "btn_login" esté presente y sea clicleable
    login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login_btn")))

    # Hacer clic en el botón "btn_login"
    login_btn.click()

    # Esperar a que se cargue la página del mapa
    WebDriverWait(driver, 10).until(EC.title_contains("Web App"))
    
    workbook = pd.read_excel(r"C:\Users\cvelasquez\Documents\automatizaciones\busqueda_utcs\DIRECCIONES_ASIGNAR_UTC.xlsx", sheet_name='Hoja1')
    direcciones = []
    for index,row in workbook.iterrows():
        direccion = f"{row['DIRECCIONESCRITA']} {row['CIUDAD']} COLOMBIA"
        direcciones.append(direccion)
         
        
    # Encontrar el campo de búsqueda por su ID
    campo_busqueda = driver.find_element(By.ID, 'search_input')
    
    # Iterar sobre las direcciones y buscar cada una en el mapa
    direccionesApp = []
    lista_utc = []
    for direccion in direcciones:
        # Ingresar la dirección en el campo de búsqueda
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loader-wrapper")))
        campo_busqueda.clear()
        campo_busqueda.send_keys(direccion)
        time.sleep(1)
        # Presionar la tecla Enter
        campo_busqueda.send_keys('\ue015') # código ASCII de la tecla flecha hacia abajo
        campo_busqueda.send_keys('\ue007') # código ASCII de la tecla Enter
        time.sleep(1)
        # Copiar la direccion encontrada en Google Maps
        campo_busqueda = driver.find_element(By.ID, "search_input")
        texto_encontrado = campo_busqueda.get_attribute("value")
        # Hacer clic en el centro del elemento con ID "map"
        mapa = driver.find_element(By.ID, 'map')
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(mapa, 0, 10).click().perform()
        time.sleep(2)
        ##OKK
        try:
            td_utc = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "(//table/tbody/tr[contains(td/text(),'UTC')])[1]/td[2]"))
            ).text
        except TimeoutException:
            td_utc = "no se encontró UTC"
            texto_encontrado="No se encontró dirección"

        direccionesApp.append(texto_encontrado)  
        lista_utc.append(td_utc)
    
    #crear dataframe
    df_final = pd.DataFrame({'Direccion_Edwin': workbook['DIRECCIONESCRITA'], 'Direccion_Encontrada': direccionesApp, 'UTC': lista_utc})
    df_final.to_excel(r"C:\Users\cvelasquez\Documents\automatizaciones\busqueda_utcs\Resultados.xlsx", index=False)
    driver.quit()
    print("Edwin: ya terminó el programa de procesar los datos.")
    
iniciar_busqueda()