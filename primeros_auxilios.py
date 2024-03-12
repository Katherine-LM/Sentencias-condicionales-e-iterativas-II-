def primeros_auxilios():
    print("Inicio, ¿Responde a estímulos?")
    respuesta_estimulos = input("Respuesta (Sí/No): ").lower()

    if respuesta_estimulos == "sí":
        print("Valorar la necesidad de llevarlo al hospital más cercano. Fin")
    else:
        print("Abrir la vía aérea.")


        
        print("¿Respira?")
        respuesta_respira = input("Respuesta (Sí/No): ").lower()

        if respuesta_respira == "sí":
            print("Permitirle posición de suficiente ventilación. Fin")
        else:
            print("Administrar 5 ventilaciones y llamar a la ambulancia.")


            
            print("¿Signos de vida?")
            respuesta_signos_vida = input("Respuesta (Sí/No): ").lower()

            if respuesta_signos_vida == "no":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
            else:
                print("Reevaluar a la espera de la ambulancia")

                
            print("¿Llegó la ambulancia?")
            respuesta_ambulancia = input("¿Llegó la ambulancia? (Sí/No): ").lower()

            if respuesta_ambulancia == "sí":
                    print("Fin de la aplicación")
            else:
                    print("Nuevamente revisar signos de vida.")




if __name__ == "__main__":
    print("Bienvenido a la aplicación de primeros auxilios.")
    primeros_auxilios()
