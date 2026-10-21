
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

# Crea una función que reciba una lista de calificaciones y devuelva el promedio de todas ellas.
def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

# Crea una función que reciba una lista de calificaciones y un umbral (por defecto 5.0), 
# y devuelva dos listas: una  con los índices de las materias aprobadas y otra con los índices de las reprobadas.
def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

# Implementa una función encontrar_extremos(calificaciones) 
# que identifique el índice de la calificación más alta 
# y el índice de la más baja en la lista de calificaciones.
def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    alta_indice = calificaciones.index(max(calificaciones))
    baja_indice = calificaciones.index(min(calificaciones))
    return alta_indice, baja_indice


# llamado a la función ingresar_calificaciones()
nombres, calificaciones = ingresar_calificaciones()
print(nombres)
print(calificaciones)
# llamado a la función calcular_promedio()
promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")
# llamado a la función determinar_estado()
aprobadas, reprobadas = determinar_estado(calificaciones , 5.0)
print(f"Índices de materias aprobadas: {aprobadas}")
print(f"Índices de materias reprobadas: {reprobadas}")
# llamado a la función encontrar_extremos()
alta_indice, baja_indice = encontrar_extremos(calificaciones)
print(f"Índice de la calificación más alta: {alta_indice}")
print(f"Índice de la calificación más baja: {baja_indice}")
