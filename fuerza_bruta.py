from string import ascii_lowercase

def fuerza_bruta(objetivo):
    intentos = 0
    longitud = len(objetivo)
    letras = list(ascii_lowercase)

    while True:
        intentos += 1
        combinacion = ''.join(letras[:longitud])

        if combinacion == objetivo:
            print(f"La contraseña fue forzada en {intentos} intentos.")
            break

        # Incrementa la combinación de letras
        i = longitud - 1
        while i >= 0:
            letras[i] = chr((ord(letras[i]) - ord('a') + 1) % 26 + ord('a'))
            if letras[i] != 'a':
                break
            i -= 1

if __name__ == "__main__":
    password = input("Ingrese la contraseña: ").lower()
    fuerza_bruta(password)
