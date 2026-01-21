# -----------------------------------------------------------------
# Universidad Fidélitas
# Curso: Programación Básica
# Proyecto Final: Administrador de Tareas Personales
# Grupo #2
# Integrantes: Luis Rodriguez, Carlos Rivera y Esteban Gamboa
# Docente: Joshua Loria
# ------------------------------------------------------------------

# Usuarios y claves autorizados
usuariosAutorizados = ["admin", "luis", "carlos"]
contrasenaAutorizadas = ["123", "123456", "123456"]

# Arreglos los datos de las tareas
nombresTareas = []
categoriasTareas = []
prioridadesTareas = []
estadosTareas = []

# --- Módulo de Inicio de Sesión ---
#Valida las credenciales del usuario dándole hasta 3 intentos
def inicioSesion():
    print("--- Bienvenido al Administrador de Tareas Personales ---")

    autenticado = False
    intentos = 0
    maxIntentos = 3

    while not autenticado and intentos < maxIntentos:
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su clave: ")


        for j in range(len(usuariosAutorizados)):
            if nombreUsuario == usuariosAutorizados[j] and contrasena == contrasenaAutorizadas[j]:
                autenticado = True
        
        if autenticado:
            print("\n¡Autenticación exitosa! Bienvenido, " + nombreUsuario + ".")
        else:

            intentos = intentos + 1 
            if intentos < maxIntentos:
                intentosRestantes = maxIntentos - intentos
                print("Error: Usuario o clave incorrectos. Le quedan", intentosRestantes, "intentos.")
            else:
                print("Ha superado los 3 intentos fallidos. El programa se cerrará.")


    return autenticado


# --- Módulos de Registro de tareas ---
#Solicita al usuario nombre y categoria de una tarea y la registra.
def registrarTarea():
    print("\n--- Módulo 1: Registro de Tareas ---")
    
    nombre = input("Ingrese el nombre de la tarea: ")
    categoriaValida = False
    
    while not categoriaValida:
        categoriaTemp = input("Ingrese la categoría (Salud, Trabajo, Educacion, Personal): ")
        
        if categoriaTemp == "Salud" or categoriaTemp == "Trabajo" or categoriaTemp == "Educacion" or categoriaTemp == "Personal":
            nombresTareas.append(nombre)
            categoriasTareas.append(categoriaTemp)
            prioridadesTareas.append("Baja")
            estadosTareas.append("Pendiente")
            print("\n¡Tarea '" + nombre + "' registrada exitosamente!")
            
            categoriaValida = True
        else:
            print("Categoría no válida. Por favor, intente de nuevo.")


#Modifica el estado o prioridad de una tarea existente
def modificarTarea():
    print("\n--- Módulo 2: Asignación de Prioridad y Estado ---")
    
    if len(nombresTareas) == 0:
        print("No hay tareas para modificar. Por favor, registre una tarea primero.")
        return

    # Lista de tareas existentes
    print("Listado de tareas registradas:")
    for i in range(len(nombresTareas)):
        print(str(i + 1) + ". " + nombresTareas[i] + " | Prioridad: " + prioridadesTareas[i] + " | Estado: " + estadosTareas[i]) 

    # Seleccionar una tarea valida ---
    numTareaModificar = 0
    seleccionValida = False
    while not seleccionValida:
        seleccionStr = input("\nIngrese el número de la tarea que desea modificar: ")
        seleccion = int(seleccionStr)
        if seleccion > 0 and seleccion <= len(nombresTareas):
            numTareaModificar = seleccion - 1
            seleccionValida = True  
        else:
            print("Selección no válida. Ingrese un número de la lista.")

    # --- Loop modificar ---
    opcionMod = ""
    opcionValida = False
    while not opcionValida:
        opcionTemp = input("¿Qué desea modificar? (1. Estado, 2. Prioridad, 3. Ambas): ")
        if opcionTemp == "1" or opcionTemp == "2" or opcionTemp == "3":
            opcionMod = opcionTemp
            opcionValida = True  
        else:
            print("Opción no válida. Ingrese 1, 2 o 3.")

    # Modificar Estado ---
    if opcionMod == "1" or opcionMod == "3":
        estadoValido = False
        while not estadoValido:
            estadoTemp = input("Ingrese el nuevo estado (Pendiente, Activa, Completada): ")
            if estadoTemp == "Pendiente" or estadoTemp == "Activa" or estadoTemp == "Completada":
                estadosTareas[numTareaModificar] = estadoTemp
                print("El estado de la tarea", numTareaModificar + 1, "ha sido actualizado.")
                estadoValido = True  
            else:
                print("Estado no válido. Intente de nuevo.")

    #Modificar Prioridad
    if opcionMod == "2" or opcionMod == "3":
        prioridadValida = False
        while not prioridadValida:
            prioridadTemp = input("Ingrese la nueva prioridad (Baja, Media, Alta): ")
            if prioridadTemp == "Baja" or prioridadTemp == "Media" or prioridadTemp == "Alta":
                prioridadesTareas[numTareaModificar] = prioridadTemp
                print("La prioridad de la tarea", numTareaModificar + 1, "ha sido actualizada.")
                prioridadValida = True 
            else:
                print("Prioridad no válida. Intente de nuevo.")

# --- Módulo Ver tareas activas ---
#Lista todas las tareas activas
def verTareasActivas():
    print("\n--- Módulo 3: Listado de Tareas Activas o Pendientes ---")

    if len(nombresTareas) == 0:
        print("No hay tareas para mostrar.")
        return
        
    tareasEncontradas = False
    print("Tareas activas y pendientes:")
    for i in range(len(estadosTareas)):
        if estadosTareas[i] != "Completada":
            print(str(i + 1) + ". " + nombresTareas[i] + " | Categoría: " + categoriasTareas[i] + " | Prioridad: " + prioridadesTareas[i] + " | Estado: " + estadosTareas[i])
            tareasEncontradas = True
    
    if not tareasEncontradas:
        print("¡Felicidades! No tiene tareas pendientes o activas.")

# --- Módulo de reportes ---
#Lista de reportes de las tareas
def moduloReportes():
    print("\n--- Módulo 4: Módulo de Informes ---")

    if len(nombresTareas) == 0:
        print("No hay tareas para generar informes.")
        return

    reporteGenerado = False
    
    while not reporteGenerado:
        print("\nSeleccione un informe:")
        print("1. Porcentaje de tareas completadas")
        print("2. Tareas por categoría")
        opcion = input("Ingrese su opción (1 o 2): ")

        if opcion == "1":
            tareasCompletadas = 0
            for estado in estadosTareas:
                if estado == "Completada":
                    tareasCompletadas = tareasCompletadas + 1
            
            porcentaje = (tareasCompletadas / len(nombresTareas)) * 100
            print("\nInforme: El", int(porcentaje), "% de las tareas han sido completadas.")
            
            reporteGenerado = True

        elif opcion == "2":
            contSalud = 0
            contTrabajo = 0
            contEducacion = 0
            contPersonal = 0

            for categoria in categoriasTareas:
                if categoria == "Salud":
                    contSalud = contSalud + 1
                elif categoria == "Trabajo":
                    contTrabajo = contTrabajo + 1
                elif categoria == "Educacion":
                    contEducacion = contEducacion + 1
                elif categoria == "Personal":
                    contPersonal = contPersonal + 1
            
            print("\nInforme de conteo de tareas por categoría:")
            print("- Salud:", contSalud)
            print("- Trabajo:", contTrabajo)
            print("- Educación:", contEducacion)
            print("- Personal:", contPersonal)

            reporteGenerado = True
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

# --- Programa Principal ---

if inicioSesion():

    salirDelPrograma = False
    
    while not salirDelPrograma: 
        print("\n" + "===================")
        print("   MENÚ PRINCIPAL   ")
        print("===================")
        print("1. Registrar nueva tarea")
        print("2. Modificar tarea (prioridad y estado)")
        print("3. Ver tareas activas y pendientes")
        print("4. Ver informes de tareas")
        print("5. Salir")
        
        opcionMenu = input("Seleccione una opción: ")

        if opcionMenu == "1":
            registrarTarea()
        elif opcionMenu == "2":
            modificarTarea()
        elif opcionMenu == "3":
            verTareasActivas()
        elif opcionMenu == "4":
            moduloReportes()
        elif opcionMenu == "5":
            print("Gracias por usar el Administrador de Tareas. ¡Hasta pronto!")
            
            salirDelPrograma = True
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")