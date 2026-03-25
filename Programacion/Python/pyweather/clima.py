import requests

def obtener_clima(latitud, longitud):
    # Construimos la URL con los datos exactos que pediste
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=relative_humidity_2m,apparent_temperature"

    try:
        # Hacemos la llamada a la API
        respuesta = requests.get(url)
        
        # Verificamos que la conexión haya sido exitosa (Código 200)
        respuesta.raise_for_status() 

        # Convertimos la respuesta JSON en un diccionario de Python
        datos = respuesta.json()

        # Extraemos la humedad y la sensación térmica
        humedad = datos["current"]["relative_humidity_2m"]
        sensacion_termica = datos["current"]["apparent_temperature"]

        # Imprimimos los resultados en pantalla
        print("--- 🌤️  Reporte Rápido ---")
        print(f"💧 Humedad del aire: {humedad}%")
        print(f"🌡️ Sensación Térmica: {sensacion_termica}°C")
        print("----------------------------")

    except requests.exceptions.RequestException as e:
        # Esto es el "Plan B" por si falla tu internet o la API
        print(f"❌ Ocurrió un error al intentar obtener el clima: {e}")

# Coordenadas de ejemplo (República Dominicana)
lat = 18.506875
lon = -70.029112

# Ejecutamos la función
obtener_clima(lat, lon)
