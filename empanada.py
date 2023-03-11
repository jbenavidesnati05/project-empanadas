opcion = 1 
empanadas = []

while opcion != 0:
    print("***********Empanadas***********")
    print("Opcion 1 = Ingresar una empanada")
    print("Opcion 2 = Mostrar todos los registros")
    print("Opcion 3 = Buscar una empanada")
    print("Opcion 4 = Editar una empanada por id")
    print("Opcion 5 = Eliminar una empanada")
    print("PRESIONE O PARA SALIR ")
    opcion = int(input("Escoja una opcion"));

    if(opcion==1):
        empanada = {}
        empanada['id']                  = int(input("Digite el id: "))
        empanada['nombre']              = (input("Digite el nombre: "))
        empanada['precio']              = float|(input("Digite el precio: "))
        empanada['popularidad']         = int(input("Digite la popularidad: "))
        empanada['fechaVencimiento']    = (input("Digite la fecha de la empanada: "))

        empanadas.append(empanada);
        print("Empanada registrada con exito")

    elif(opcion==2):
        for empanada in empanadas:
            print(empanada)

    elif(opcion==3):
        buscarId = int(input("Ingrese el id de la empanada a buscar :"))
        for empanada in empanadas:
            if(buscarId==empanada['id']):
                print("empanada encontrada")
                print(empanada)

    elif(opcion==4):
        buscarId = int(input("Ingrese el id de la empanada a buscar :"))
        for empanada in empanadas:
            if(buscarId==empanada['id']):
                print("empanada encontrada")
                print(empanada)
                print(empanada['precio'])
                precioNuevo = float(input("Digita el precio nuevo: "))
                empanada["precio"]=precioNuevo


    elif(opcion==5):
        pass
    elif(opcion==0):
        pass
    else:
        print("Opcion invalida")