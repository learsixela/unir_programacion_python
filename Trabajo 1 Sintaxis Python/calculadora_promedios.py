
# Implementa una función llamada ingresar_calificaciones() que permita
# al usuario introducir el nombre de una materia y su calificación correspondiente.
def ingresar_calificaciones():
    nombres = []
    calificaciones = []

    while True:
        # Solicitar al usuario que ingrese el nombre de la materia
        materia = input("Ingrese el nombre de la materia (o 'salir' para terminar): ").strip()
        if materia.lower() == 'salir':
            break
        # validaciones    
        if materia == "":
            print("El nombre de la materia no puede estar vacío.")
            continue

        if any(m.lower() == materia.lower() for m in nombres):
            print(f"La materia '{materia}' ya existe. Ingrese otra diferente.")
            continue

        while True:
            try:
                # Solicitar la calificación (validando que sea un número entre 0 y 10)
                calificacion = float(input(f"Ingrese la calificación de {materia}: "))
                if calificacion < 0 or calificacion > 10:
                    print("La calificación debe estar entre 0 y 10.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        # Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
        nombres.append(materia)
        calificaciones.append(calificacion)
        # Preguntar si desea continuar ingresando más materias
        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
    # Retornar ambas listas cuando el usuario decida terminar        
    return nombres, calificaciones


# llamado a la función ingresar_calificaciones()
nombres, calificaciones = ingresar_calificaciones()
print(nombres)
print(calificaciones)
