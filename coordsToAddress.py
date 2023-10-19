# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:25:29 2023

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
    
    url = 'https://www.google.com/maps/'
    PATH = r"C:\Users\cvelasquez\Documents\automatizaciones\busqueda_utcs\chromedriver.exe"
    
    workbook = pd.read_excel("cordsToAdress.xlsx")
    direcciones = []
    for index,row in workbook.iterrows():
        direccion = f"{row['LATITUD']},{row['LONGITUD']}"
        direcciones.append(direccion)
    
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
    
    campo_busqueda = driver.find_element(By.ID, 'searchboxinput')
    
    lista_direcciones_google = []
    
    for direccion in direcciones:
        campo_busqueda.clear()
        campo_busqueda.send_keys(direccion)
        time.sleep(1)
        # Presionar la tecla Enter
        campo_busqueda.send_keys('\ue015') # código ASCII de la tecla flecha hacia abajo
        campo_busqueda.send_keys('\ue007') # código ASCII de la tecla Enter
        time.sleep(2)
    
        campo_direccion = driver.find_element(By.CLASS_NAME, 'DkEaL').text
        lista_direcciones_google.append(campo_direccion)
    
    
    workbook["DIRECCIONGOOGLE"]=lista_direcciones_google
    
    workbook.to_excel("Resultados_Cords_to_adress.xlsx", index=False)
    print("Edwin: ya acabó de encontrar las direcciones en base a las cordenadas.")


    
    
    
    
    
iniciar_busqueda()