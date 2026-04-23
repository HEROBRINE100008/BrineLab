import random
import string
import os

def generar_diccionario_interactivo():
    print("--- Generador de Diccionarios para Pruebas de Estrés ---")
    
    # 1. Preguntar al usuario la cantidad
    try:
        cantidad = int(input("¿De cuántas líneas quieres el diccionario? (Ej: 100000000 para 100M): "))
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")
        return

    nombre_archivo = "stress_test_final.txt"
    objetivo = "msfadmin"
    
    # 2. Calcular la posición (siempre en el último 1% del total)
    inicio_rango_final = int(cantidad * 0.99)
    posicion_objetivo = random.randint(inicio_rango_final, cantidad - 1)
    
    print(f"Generando {cantidad} entradas... El objetivo estará después de la línea {inicio_rango_final}.")
    
    prefijos = ['admin', 'root', 'msf', 'user', 'guest', 'security', 'lab']
    caracteres = string.ascii_lowercase + string.digits
    
    # 3. Escritura optimizada con buffer
    try:
        with open(nombre_archivo, 'w', buffering=10**7) as f:
            for i in range(cantidad):
                if i == posicion_objetivo:
                    f.write(f"{objetivo}\n")
                else:
                    # Alternar tipos de datos aleatorios
                    r = i % 3
                    if r == 0:
                        # Números aleatorios
                        f.write(f"{random.randint(100000, 999999999)}\n")
                    elif r == 1:
                        # Prefijo + cadena corta
                        word = ''.join(random.choices(caracteres, k=5))
                        f.write(f"{random.choice(prefijos)}{word}\n")
                    else:
                        # Cadena alfanumérica pura
                        f.write(f"{''.join(random.choices(caracteres, k=10))}\n")
                
                # Mostrar progreso cada 10% para no saturar la consola
                intervalo_progreso = cantidad // 10 if cantidad >= 10 else 1
                if (i + 1) % intervalo_progreso == 0:
                    print(f"Progreso: {((i + 1) / cantidad) * 100:.0f}% completado...")

        tamano_mb = os.path.getsize(nombre_archivo) / (1024 * 1024)
        print(f"\n¡Éxito! Archivo '{nombre_archivo}' creado ({tamano_mb:.2f} MB).")
        print(f"La contraseña '{objetivo}' está oculta cerca del final.")
        
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

if __name__ == "__main__":
    generar_diccionario_interactivo()
