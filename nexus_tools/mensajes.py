import pywhatkit # type: ignore


def validar_numero(numero: str) -> str | None:
    numero = numero.strip().replace("+", "")

    if not numero.isdigit():
        print(f"Error: '{numero}' contiene caracteres no válidos.")
        return None

    if not (10 <= len(numero) <= 13):
        print(f"Error: {numero} debe tener entre 10 y 13 dígitos.")
        return None

    if numero.startswith('58'):
        numero_final = '+' + numero
    elif numero.startswith('4'):
        numero_final = '+58' + numero
    else:
        numero_final = '+' + numero #considerando numero internacional

    return numero_final


def notificaciones(mensaje: str, numeros: str) -> str:

    try:
        for i in range(len(numeros)):
            numero = validar_numero(numeros[i])
            if numero is None:
                continue  # Saltar números inválidos
        
            pywhatkit.sendwhatmsg_instantly(numero, mensaje, wait_time=20, tab_close=True)

        print(f'Se han enviado los mensajes de notificacion')
    
    except Exception as e:
        return (f'No fue posible enviar las notificaciones debida a {e}. Intente nuevamente mas tarde')