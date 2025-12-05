import os
import subprocess
import time

def ejecutar_comando(comando):
    """Ejecuta un comando ADB y retorna su salida"""
    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        return resultado.strip()
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"

def verificar_dispositivos():
    """Verifica los dispositivos conectados por ADB"""
    return ejecutar_comando("adb devices")

def obtener_info_dispositivo():
    """Obtiene información básica del dispositivo"""
    info = {
        "Modelo": ejecutar_comando("adb shell getprop ro.product.model"),
        "Versión Android": ejecutar_comando("adb shell getprop ro.build.version.release"),
        "Número de Serie": ejecutar_comando("adb shell getprop ro.serialno"),
        "Nivel de Batería": ejecutar_comando("adb shell dumpsys battery | grep level")
    }
    return info
def consola_dispositivo():
    """Comando de shell para conectarse"""
    print("Entrando en la shell...")
    ejecutar_comando("adb shell")
    
def main():
    print("=== Script de Control ADB ===")
    
    # Iniciar el servidor ADB si no está corriendo
    print("\nIniciando servidor ADB...")
    ejecutar_comando("adb start-server")
    time.sleep(2)
    
    # Verificar dispositivos conectados
    print("\nBuscando dispositivos conectados...")
    dispositivos = verificar_dispositivos()
    print(dispositivos)
    
    if "device" not in dispositivos:
        print("No se encontraron dispositivos conectados.")
        return
    
    # Obtener información del dispositivo
    print("\nObteniendo información del dispositivo...")
    info = obtener_info_dispositivo()
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
    
   # Conectarse como shell al dispositivo
   consola = consola_dispositivo()
if __name__ == "__main__":
    main()
