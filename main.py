import requests
import csv
from datetime import datetime
import os


parametros = {
    "units": "metric",
    "APPID": "5ef77eb6cacb1849c90dd5c757eb501"
}


respuesta = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=48.8566&lon=2.3522&appid=5ef77eb6cacb1849c90dd5c757eb501c&lang=es&units=metric",
    params=parametros
)


if respuesta.status_code == 200:
    datos = respuesta.json()
    
    print("Ciudad :    ",datos["name"])   
    print("Pais   :    ",datos["sys"]["country"])  
    print("Zona Horaria:",datos["timezone"])   
    print('-' * 15)
    weather_info = datos["weather"][0]
    print("Condición del clima:", weather_info["main"])
    print("Descripción:", weather_info["description"])
    print("Ícono del clima:", weather_info["icon"])
    print('-' * 15)
    print("La temperatura actual es:",datos["main"]["temp"],"ºC")
    print("La temperatura mínima es:",datos["main"]["temp_min"],"ºC")
    print("La temperatura máxima es:",datos["main"]["temp_max"],"ºC")
    print("La presión es:",datos["main"]["pressure"],"hPa")
    print("La humedad es:",datos["main"]["humidity"],"%")
    print('-' * 15)
    print("Visibilidad :    ",datos["visibility"]) 
    print("Vientos     :    ",datos["wind"]["speed"])


    temp_actual = datos["main"]["temp"]
    temp_min = datos["main"]["temp_min"]
    temp_max = datos["main"]["temp_max"]
    presion = datos["main"]["pressure"]
    humedad = datos["main"]["humidity"]

    weather_info = datos["weather"][0]
    condicion_clima = weather_info["main"]
    descripcion = weather_info["description"]

    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    hora_hoy = datetime.now().strftime('%H:%M:%S')

    directorio = '/home/sebas/Api'  
    nombre_archivo = 'clima-paris-hoy.csv'
    ruta_archivo = os.path.join(directorio, nombre_archivo)

    os.makedirs(directorio, exist_ok=True)
    
    with open(ruta_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
       
        if archivo.tell() == 0:
            escritor_csv.writerow([
                'Fecha', 'hora' , 'Temperatura Actual (ºC)', 'Temperatura Mínima (ºC)', 
                'Temperatura Máxima (ºC)', 'Presión (hPa)', 'Humedad (%)', 
                'Condición del Clima', 'Descripción'
            ])
        
        escritor_csv.writerow([
            fecha_hoy, hora_hoy ,temp_actual, temp_min, temp_max, presion, humedad, 
            condicion_clima, descripcion
        ])
    
    print('-' * 15)
    print(f"Datos guardados en {ruta_archivo}")
    print(' ' * 15)
else:
    print("Error al conectar con el API")




