from pynput import keyboard


def al_presionar(tecla):
    try:
        print(f'\rTecla alfanumérica presionada: {tecla.char}', end="")
    except AttributeError:
        print(f'\rTecla especial presionada: {tecla}', end="")


def al_soltar(tecla):
    # Si presionas la tecla Escape, el programa se detiene
    if tecla == keyboard.Key.esc:
        print("\nSaliendo...")
        return False


# Activa el escuchador de eventos en segundo plano
with keyboard.Listener(
        on_press=al_presionar,
        on_release=al_soltar) as escuchador:
    escuchador.join()
