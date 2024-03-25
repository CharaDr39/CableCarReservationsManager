UsuarioIng=""
ContraIng=""
Usuario=""
Contra=""

                                                                #Def de logueo
def logueo(UsuarioIng, ContraIng):
    intentos = 0
    intentos_máximos = 3
    print("Bienvenido al Logueo, por Favor, Ingrese su usuario y contraseña!\n")
    Decision_logueo = "no"
    login = "No"

    # Asignación de las variables de usuario y contraseña
    Usuario, Contra = "", ""

    while intentos < intentos_máximos and login == "No" and Decision_logueo == "no":
        Usuario = input("Ingrese su nombre de usuario: ")
        Contra = input("Ingrese su contraseña: ")
        Decision_logueo = input("Su información es correcta? ")

        if Decision_logueo=="si":
            if Usuario == UsuarioIng and ContraIng == Contra:
                login = "Si"
            else:
                print("Error en el usuario o contraseña. Por favor, inténtelo de nuevo.")
                print()
                intentos += 1

    if login == "Si":
        print("Logueo exitoso.")
        input("Presione enter para continuar.")
    elif login == "No" and intentos >= intentos_máximos:
        input("Su usuario está bloqueado. Presione enter para volver al menú.")

                                                                #Def de Módulo de registro
def registro():

    print("Bienvenido a Registro, por Favor, Ingrese su informacion abajo\n")
    d_reg="no"
    datos=[]
    while d_reg == "no":
        if d_reg == "no":
            datos=[]
        datos.append(input("Porfavor ingrese su nombre y apellido:"))
        datos.append(input("Porfavor ingrese su Cedula:"))
        datos.append(input("Porfavor ingrese su Edad:"))
        datos.append(input("Porfavor ingrese su Sexo:"))
        datos.append(input("Porfavor ingrese su Direccion:"))
        datos.append(input("Porfavor ingrese su Numero de telefono:"))
        datos.append(input("Porfavor ingrese su Correo Electronico:"))

        print("\nGracias!Ahora creemos su usuario\n")

        datos.append(input("Ingrese su nombre de usuario:"))
        datos.append(input("Ingrese su contraseña:"))

        print()
        print("Nombre y apellido:",datos[0])
        print("Cedula:",datos[1])
        print("Edad:",datos[2])
        print("Sexo:",datos[3])
        print("Direccion:",datos[4])
        print("Telefono:",datos[5])
        print("Correo:",datos[6])
        print("Usuario:",datos[7])

        d_reg=input("¿Su informacion es corresta (si/no)")
        if d_reg == "si":
            break

    input("Registro completo! Presione Enter para volver al menu principal")
    return datos
   
                                                                #Def de Módulo de reservas
def reservas():
    print("Módulo de reservas\n")

    # Definir capacidades de los teleféricos por horario
    capacidades = [10, 15, 10, 15]

    # Cantidad de personas reservadas por horario
    reservas_por_horario = [0, 0, 0, 0]

    # Cantidad de teleféricos reservados por horario
    telefericos_por_horario = [0, 0, 0, 0]

    # Recaudación total
    recaudacion_total = 0

    # Tarifas
    tarifas_nacional_normal = 5000
    tarifas_nacional_niño_adulto_mayor = 2500
    tarifas_extranjero_normal = 7000
    tarifas_extranjero_niño_adulto_mayor = 3500

    d_reg = "no"

    while d_reg == "no":
        # Reiniciamos las variables de reserva si la información no es correcta
        if d_reg == "no":
            cantidad_personas = int(input("Ingrese la cantidad de personas que viajarán: "))
            condicion = input("Ingrese la condición (nacional o extranjero): ")
            edad = int(input("Ingrese la edad de la persona: "))
            horario = input("Ingrese el horario en el que desea reservar (8:00 am, 10:00 am, 12:00 md, 2:00 pm): ")
            print()

            # El número de reserva se crea a partir de la cantidad de personas y la edad, y para que se vea más bonito se multiplica por 1234
            n_reserva = cantidad_personas * edad * 1234

            # Verificar disponibilidad y asignar teleférico
            i_horario = -1
            if horario == "8:00 am":
                i_horario = 0
            elif horario == "10:00 am":
                i_horario = 1
            elif horario == "12:00 md":
                i_horario = 2
            elif horario == "2:00 pm":
                i_horario = 3

            capacidad = capacidades[i_horario]
            reservas = reservas_por_horario[i_horario]
            telefericos = telefericos_por_horario[i_horario]

            espacios_disponibles = capacidad - (reservas // 6) * 6

            if cantidad_personas <= espacios_disponibles:
                numero_teleferico = (telefericos // 6) + 1
                espacios_reservados = cantidad_personas

                # Calcular monto a pagar
                if condicion == "nacional":
                    if edad < 18 or edad >= 65:
                        monto_total = cantidad_personas * tarifas_nacional_niño_adulto_mayor
                    else:
                        monto_total = cantidad_personas * tarifas_nacional_normal
                else:
                    if edad < 18 or edad >= 65:
                        monto_total = cantidad_personas * tarifas_extranjero_niño_adulto_mayor
                    else:
                        monto_total = cantidad_personas * tarifas_extranjero_normal

                recaudacion_total += monto_total
                print()
                print("Reserva exitosa. Número de teleférico:", numero_teleferico, "Espacios:", espacios_reservados)
                print()
                print("Su número de reserva:", n_reserva)
                print()
                print("Monto a pagar:", monto_total, "colones")
            else:
                print("No hay suficiente espacio en el horario escogido. Por favor, elija otro horario.")
                print()

        d_reg = input("¿Su informacion es correcta? (si/no): ")
        print()

    input("Presione Enter para volver al menú principal\n")

    return condicion, cantidad_personas, edad, horario, monto_total, n_reserva

def facturacion(datos, n_reserva):
    print()
    print("-----Módulo de facturación-----")
    print("Datos del cliente:")
    print("Nombre:", datos[0])
    print("Número de identificación:", datos[1])
    print("Número de reservación:", n_reserva)
    print()
    print("Datos de la reserva:")
    print("Cantidad de personas:", cantidad_personas)
    print("Condición:", condicion)
    print("Horario:", horario)
    print()
    print("Detalles de la factura:")
    print("Monto a pagar por cada persona:", monto_total / cantidad_personas)
    print("Factura total:", monto_total)
    print("--------------------------------")
    print()
    input("Presione Enter para volver al menú principal\n")

                                                                 #Zona principal   
                                                                 
Decision = int(input("Estas son sus opciones:\n1. Logueo\n2. Módulo de Registro del Cliente \n3. Módulo de reservas\n4. Módulo de facturación\n5. Módulo de Informes\n6. Salir \nTome su decisión: "))

while Decision != 6:
    if Decision == 1:
        logueo(datos[7], datos[8])

    elif Decision == 2:
        datos = registro()

    elif Decision == 3:
       condicion, cantidad_personas, edad, horario, monto_total, n_reserva = reservas()

    elif Decision == 4:
        if datos:
            facturacion(datos, n_reserva)
        else:
            input("Por favor, inicie sesión primero.\n")

    Decision = int(input("Estas son sus opciones:\n1. Logueo\n2. Módulo de Registro del Cliente \n3. Módulo de reservas\n4. Módulo de facturación\n5. Módulo de Informes\n6. Salir \nTome su decisión: "))

if Decision == 6:
    print("Usted ha salido del sistema.")
