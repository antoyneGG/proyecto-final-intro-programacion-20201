import json
import copy
import math
'''
Nombre: añadirUser
Objetivo: Agrega un nuevo usuario al diccionario global users
Parametros:
	nombre_apellido(str): El nombre y apellido del usuario
	ide(int): Identificacion del usuario
	tipouser(str): El tipo de usuario(Estudiante, Profesor, Personal Administrativo)
	placa(str): Placa del vehiculo
	vehiculo(str): Tipo del vehiculo(Automovil, Automovil Electrico, Motocicleta, Discapacitado)
	plan(str): Plan de pago(Mensualidad, Diario)
'''
def añadirUser(nombre_apellido,ide,tipouser,placa,vehiculo,plan):
	global users
	user = []
	user.append(nombre_apellido)
	user.append(ide)
	user.append(tipouser)
	user.append(placa)
	user.append(vehiculo)
	user.append(plan)
	users["usuarios"].append(user)

'''	
Nombre: añadirVisitante
Objetivo: Agrega informacion de un visitante a una lista separada
Parametros:
	placa(str): Placa del vehiculo
	tvehiculo(str): Tipo del vehiculo(Automovil, Automovil Electrico, Motocicleta, Discapacitado)
'''
def añadirVisitante(placa, tvehiculo):
	global listavisitantes
	visi = []
	visi.append(placa)
	visi.append(tvehiculo)
	listavisitantes.append(visi)

'''
Nombre: validacionDisponibilidad
Objetivo: Suma todos los elementos de lista para validar la cantidad de espacios disponibles total.
Parametros:
	tipov(int): Tipo del vehiculo(1, 2, 3, 4)
Salidas:
	True: Si la suma total es mayor a 0, ademas imprime la cantidad disponible por cada piso. Ejemplo: Piso1: 28
	False: Si la suma total es igual a 0.
'''
def validacionDisponibilidad(tipov):

	lista = consultarEspacioDisponiblePorPiso(tipov)
	sumeme = 0
	for i in range(len(lista)):
		sumeme += lista[i]
	if sumeme == 0:
		print('Lo sentimos, no hay espacios disponibles.')
		return False
	else:
		for i in range(6):
			print('Piso{}: '.format(i+1),lista[i])
		return True

'''
Nombre: consultarEspacioDisponiblePorPiso
Objetivos: Crea una lista de los espacios disponibles por piso segun el tipo de vehiculo dado. 
Ejemplo: [28, 31, 25, 26, 27, 9]
Cada elemento representa la cantidad de espacios disponibles de cada piso por ese tipo de vehiculo. 
Entonces se puede entender que en el piso 1 hay 28 espacios disponibles para ese tipo de vehiculo.
Parametros:
	tipov(int): Tipo del vehiculo
Salidas:
	listacantdisponible(list)
'''
def consultarEspacioDisponiblePorPiso(tipov):
	global parker
	global parkercopia
	listacantdisponible = []
	for pisos in parkercopia.keys():
		cantdisponible = 0
		if pisos != "Piso6":
			for lista in range(10):
				for i in range(10):	
					if parkercopia[pisos][lista][i] == tipov:
						cantdisponible += 1
		else:
			for lista in range(5):
				for i in range(10):
					if parkercopia[pisos][lista][i] == tipov:
						cantdisponible += 1
		listacantdisponible.append(cantdisponible)
	return(listacantdisponible)

'''
Nombre: crearMuestra
Objetivo: Crea una muestra del piso seleccionado mostrando con un 0 los espacios disponibles para ese tipo de vehiculo, 
los espacios que no se encuentren disponibles se mostraran con una X.
Parametros:
	piso(str): Nombre del piso seleccionado. Ejemplo: 'Piso1'
	tipov(int): Tipo del vehiculo(1, 2, 3, 4) 
Salida:
	parkeaderomuestra(dict): Copia modificada del diccionario 'parkeadero'
'''
def crearMuestra(piso,tipov):

	global parker
	global parkeadero
	parkeaderomuestra = copy.deepcopy(parkeadero)
	for i in range(len(parker[piso])):
		for x in range(10):
			if parker[piso][i][x] != tipov:
				parkeaderomuestra[piso][i][x] = 'X'
	return(parkeaderomuestra)

'''
Nombre: actualizarParqueadero
Objetivo: Actualiza la informacion del parqueadero segun los datos del vehiculo que ha sido retirado.
Parametro:
	placa(str): Placa del vehiculo
'''
def actualizarParqueadero(placa):
	global parkercopia
	global vehiculosEstacionados
	global parkeadero
	for i in range(len(vehiculosEstacionados['vehiculos'])):
		if placa == vehiculosEstacionados['vehiculos'][i][0]:
			piso = vehiculosEstacionados['vehiculos'][i][1]
			fila = vehiculosEstacionados['vehiculos'][i][2]
			columna = vehiculosEstacionados['vehiculos'][i][3]
			tipov = vehiculosEstacionados['vehiculos'][i][4]
	parkercopia[piso][fila][columna] = tipov
	parkeadero[piso][fila][columna] = '0'

'''
Nombre: buscarVehiculoEstacionado
Objetivo: Encuentra el indice correspondiente a la lista del vehiculo retirado a partir de la placa.
Parametros:
	vehiculosEstacionados(dict): Diccionario con una sola llave en la cual guarda una matriz en donde 
	cada lista almacena la informacion de un vehiculo estacionado.
	placa(str): Placa del vehiculo
Salida:
	i(int): Indice correspondiente a la lista del vehiculo
'''
def buscarVehiculoEstacionado(vehiculosEstacionados,placa):
	for i in range(len(vehiculosEstacionados['vehiculos'])):
		if placa == vehiculosEstacionados['vehiculos'][i][0]:
			return(i)

'''
Nombre: agregarVehiculo
Objetivo: Agregar la informacion del vehiculo estacionado a la lista del diccionario 'vehiculosEstacionados'.
Parametros:
	placa(str): Placa del vehiculo
	piso(str): Piso en el que se encuentra el vehiculo. Ejemplo: 'Piso1'
	fila(int): Numero de la fila
	columna(int): Numero de la columna
	tipov(int): Numero del tipo del vehiculo(1, 2, 3, 4)
	tipouser(str): Tipo del usuario(Estudiante, Profesor, Personal Administrativo, Visitante)
'''
def agregarVehiculo(placa,piso,fila,columna,tipov,tipouser):
	global vehiculosEstacionados
	listaVehiculo = []
	listaVehiculo.append(placa)
	listaVehiculo.append(piso)
	listaVehiculo.append(fila)
	listaVehiculo.append(columna)
	listaVehiculo.append(tipov)
	listaVehiculo.append(tipouser)
	vehiculosEstacionados['vehiculos'].append(listaVehiculo)

'''
Nombre: registrar
Objetivo: Solicitar al usuario la informacion necesaria para el registro. Ejemplo:
nombre_apellido: Laura Leon
ide: 1126587
tipoUser: 1('Estudiante')
placa: CHIM777
vehiculo: 1('Automóvil')
planPago: 1('Mensualidad')
'''
def registrar():
	nombre_apellidos = input("Digite su nombre y apellidos\n")
	ide = eval(input("Digite su numero de identificacion\n"))
	tipoUser = eval(input("Seleccione su tipo de usuario: \n1. Estudiante \n2. Profesor \n3. Personal Administrativo\n" ))
	if tipoUser == 1:
		tipoUser = "Estudiante"
	elif tipoUser == 2:
		tipoUser = "Profesor"
	elif tipoUser == 3:
		tipoUser = "Personal Administrativo" 
	placa = input("Digite la placa de su vehiculo\n")
	vehiculo = eval(input("Digite el tipo de su vehiculo: \n1. Automóvil \n2. Automóvil Eléctrico \n3. Motocicleta \n4. Discapacitado\n"))
	if vehiculo == 1:
		vehiculo = "Automóvil"
	elif vehiculo == 2:
		vehiculo = "Automóvil Eléctrico"
	elif vehiculo == 3:
		vehiculo = "Motocicleta"
	elif vehiculo == 4:
		vehiculo = "Discapacitado"
	planPago = eval(input("Digite su plan de pago: \n1. Mensualidad \n2. Diario\n"))
	if planPago == 1:
		planPago = "Mensualidad"
	elif planPago == 2:
		planPago = "Diario"
	if validarID(ide):
#Si el numero de identificacion ingresado ya se encuentra registrado se cancelara el registro y acabara el procedimiento.
		print("Lo sentimos mucho, este usuario ya se encuentra registrado, intente registrarse nuevamente.")
	else:
		añadirUser(nombre_apellidos,ide,tipoUser,placa,vehiculo,planPago)

'''
Nombre: validarID
Objetivos: Valida si el numero de identificacion se encuentra registrado o no.
Parametro:
	ide(int): Numero de identificacion
Salidas:
	True: Si se encuentra un usuario registrado con el mismo numero de identificacion.
	False: Si no se encuentra registrado este numero de identificacion.
'''
def validarID(ide):
	global users
	for i in range(len(users['usuarios'])):
		if ide == users['usuarios'][i][1]:
			return True 
	return False

'''
Nombre: validarPlaca
Objetivos: Valida si la placa ya se encuentra registrada o no.
Parametro:
	placa(str): Placa del vehiculo
Salidas:
	True: Si se encuentra un usuario registrado con la misma placa.
	False: Si no se encuentra la placa registrada.
'''
def validarPlaca(placa):
	global users
	for i in range(len(users['usuarios'])):
		if placa == users['usuarios'][i][3]:
			return True
	return False

'''
Nombre: validarPlacaEstacionada
Objetivos: Valida si el vehiculo se encuentra estacionado segun su placa.
Parametro:
	placa(str): Placa del vehiculo
Salidas:
	True: Si la placa corresponde con algun vehiculo estacionado.
	False: Si la placa no corresponde a ningun vehiculo estacionado.
'''
def validarPlacaEstacionada(placa):
	global vehiculosEstacionados
	for i in range(len(vehiculosEstacionados['vehiculos'])):
		if placa == vehiculosEstacionados['vehiculos'][i][0]:
			return True
	return False

'''
Nombre: buscarTipoVehiculo
Objetivo: Buscar el tipo del vehiculo a partir de su placa.
Parametro:
	placa(str): Placa del vehiculo
Salidas:
	1(int): Si el tipo corresponde a 'Automóvil'.
	2(int): Si el tipo corresponde a 'Automóvil Eléctrico'.
	3(int): Si el tipo corresponde a 'Motocicleta'.
	4(int): Si el tipo corresponde a 'Discapacitado'.
'''
def buscarTipoVehiculo(placa):
	global users
	for i in range(len(users['usuarios'])):
		if placa == users['usuarios'][i][3]:
			if (users['usuarios'][i][4]) == 'Automóvil':
				return(1)
			elif (users['usuarios'][i][4]) == 'Automóvil Eléctrico':
				return(2)
			elif (users['usuarios'][i][4]) == 'Motocicleta':
				return(3)
			elif (users['usuarios'][i][4]) == 'Discapacitado':
				return(4)

'''
Nombre: buscarTipoUser
Objetivo: Busca el tipo de usuario a partir de la placa.
Parametro:
	placa(str): Placa del vehiculo
Salidas:
	users['usuarios'][i][2](Tipo de usuario): Si la placa corresponde a la placa de un usuario registrado.
	'Visitante'(str): Si la placa no corresponde a ninguna placa de los usuarios registrados.
'''
def buscarTipoUser(placa):
	global users
	for i in range(len(users['usuarios'])):
		if placa == users['usuarios'][i][3]:
			return(users['usuarios'][i][2])
	return('Visitante')

'''
Nombre: buscarPlanPago
Objetivo: Busca el plan de pago a partir de la placa.
Parametro:
	placa(str): Placa del vehiculo.
Salida:
	users['usuarios'][i][5]: El plan de pago del usuario correspondiente a la placa.
'''
def buscarPlanPago(placa):
	global users
	for i in range(len(users['usuarios'])):
		if placa == users['usuarios'][i][3]:
			return(users['usuarios'][i][5])

'''
Nombre: ingresarVehiculo
Objetivos: 
	1. Solicita la placa, si no se encuentra registrada se categoriza al usuario como visitante y se le solicita la informacion del vehiculo.
	2. Si hay disponibilidad para su tipo de vehiculo se le solicita al usuario que seleccione un piso.
	3. Muestra al usuario el piso seleccionado con los espacios disponibles para su tipo de vehiculo y vacios.
	4. Solicita la posicion en la que el usuario desee ingresar el vehiculo segun la fila y la columna.
	5. Actualiza la posicion seleccionada en el parqueadero y posteriormente muestra el nuevo parqueadero.
'''
def ingresarVehiculo():
	global listacantdisponible
	global parkercopia
	placa = input('Ingrese la placa de su vehiculo\n')
	if not validarPlaca(placa):
		tipoUser ='Visitante'
		vehiculo = eval(input("Digite el tipo de su vehiculo: \n1. Automóvil \n2. Automóvil Eléctrico \n3. Motocicleta \n4. Discapacitado\n"))
		tipov = vehiculo
		if vehiculo == 1:
			vehiculo = "Automóvil"
		elif vehiculo == 2:
			vehiculo = "Automóvil Eléctrico"
		elif vehiculo == 3:
			vehiculo = "Motocicleta"
		elif vehiculo == 4:
			vehiculo = "Discapacitado"
		planPago = 'Diario'
		añadirVisitante(placa,vehiculo)
	else:
		tipov = buscarTipoVehiculo(placa)
	if validacionDisponibilidad(tipov):
		piso = eval(input('Seleccione el numero del piso que desea: \n'))
		if piso == 1:
			pisoSelect = "Piso1"
		elif piso == 2:
			pisoSelect = "Piso2"
		elif piso == 3:
			pisoSelect = "Piso3"
		elif piso == 4:
			pisoSelect = "Piso4"
		elif piso == 5:
			pisoSelect = "Piso5"
		elif piso == 6:
			pisoSelect = "Piso6"
		parkM = crearMuestra(pisoSelect,tipov)
		for i in range(len(parkM[pisoSelect])):
			print(parkM[pisoSelect][i])
		print('A continuacion seleccione la ubicacion en la cual desea ingresar su vehiculo: ')
		control = True
		while control:
			fila = (eval(input('Seleccione la fila: '))-1)
			columna = (eval(input('Seleccione la columna: '))-1)
			if parkM[pisoSelect][fila][columna] == 'X':
				print('Este espacio no se encuentra disponible.')
			else:
				control = False
		parkeadero[pisoSelect][fila][columna] = 'X'
		for i in range(len(parkeadero[pisoSelect])):
			print(parkeadero[pisoSelect][i])
		parkercopia[pisoSelect][fila][columna] = 0
		tipoUser = buscarTipoUser(placa)
		agregarVehiculo(placa,pisoSelect,fila,columna,tipov,tipoUser)

'''
Nombre: retirarVehiculo
Objetivos: Solicita placa y numero de horas para generar el cobro respectivo a partir del tipo de usuario y su plan de pago,
y posteriormente elimina la informacion del vehiculo de la lista de 'vehiculosEstacionados['vehiculos']'.
'''
def retirarVehiculo():
	global vehiculosEstacionados
	placa = input('Ingrese su placa: \n')
	if not validarPlacaEstacionada(placa):
		print('Este vehiculo no se encuentra estacionado. \n')
	else:
		nHoras = eval(input('Ingrese el numero de horas: \n'))
		tipoUser = buscarTipoUser(placa)
		if tipoUser == 'Visitante':
			planPago = 'Diario'
		else:
			planPago = buscarPlanPago(placa)
		if planPago == 'Mensualidad':
			print('No debe realizar ningun pago, vuelva pronto.')
		else:
			if tipoUser == 'Estudiante':
				valor = math.ceil(nHoras)*1000
			elif tipoUser == 'Personal Administrativo':
				valor = math.ceil(nHoras)*1500
			elif tipoUser == 'Profesor':
				valor = math.ceil(nHoras)*2000
			elif tipoUser == 'Visitante':
				valor = math.ceil(nHoras)*3000
			print('El valor a pagar por el retiro de su vehiculo es {}'.format(valor))
		actualizarParqueadero(placa)
		index = buscarVehiculoEstacionado(vehiculosEstacionados,placa)
		del vehiculosEstacionados['vehiculos'][index]

'''
Nombre: reportes
Objetivos:
	1. Generar reporte de la cantidad de vehiculos estacionados segun el tipo de usuario.
	2. Generar reporte de la cantidad de vehiculos estacionados segun el tipo de vehiculo.
	3. Generar reportes del porcentaje de ocupacion de los vehiculos estacionados por piso.
	4. Generar reporte del porcentaje de ocupacion global del parqueadero.
'''
def reportes():
	global vehiculosEstacionados
	contEst = 0
	contProf = 0
	contPers = 0
	contVist = 0
	contAut = 0
	contAutElec = 0
	contMotto = 0
	contDisc = 0
	contP1 = 0
	contP2 = 0 
	contP3 = 0
	contP4 = 0
	contP5 = 0
	contP6 = 0
	for i in range(len(vehiculosEstacionados['vehiculos'])):
		if vehiculosEstacionados['vehiculos'][i][5] == 'Estudiante':
			contEst += 1
		elif vehiculosEstacionados['vehiculos'][i][5] == 'Profesor':
			contProf += 1
		elif vehiculosEstacionados['vehiculos'][i][5] == 'Personal Administrativo':
			contPers += 1
		elif vehiculosEstacionados['vehiculos'][i][5] == 'Visitante':
			contVist += 1
		if vehiculosEstacionados['vehiculos'][i][4] == 1:
			contAut += 1
		elif vehiculosEstacionados['vehiculos'][i][4] == 2:
			contAutElec += 1
		elif vehiculosEstacionados['vehiculos'][i][4] == 3:
			contMotto += 1
		elif vehiculosEstacionados['vehiculos'][i][4] == 4:
			contDisc += 1
		if vehiculosEstacionados['vehiculos'][i][1] == 'Piso1':
			contP1 += 1
		elif vehiculosEstacionados['vehiculos'][i][1] == 'Piso2':
			contP2 += 1
		elif vehiculosEstacionados['vehiculos'][i][1] == 'Piso3':
			contP3 += 1
		elif vehiculosEstacionados['vehiculos'][i][1] == 'Piso4':
			contP4 += 1
		elif vehiculosEstacionados['vehiculos'][i][1] == 'Piso5':
			contP5 += 1
		elif vehiculosEstacionados['vehiculos'][i][1] == 'Piso6':
			contP6 += 1

	file = open('reportes.txt','w')
	file.write('Reporte de vehiculos estacionados segun tipo de usuario:\n')
	file.write('Estudiantes: '+str(contEst)+'\n')
	file.write('Profesores: '+str(contProf)+'\n')
	file.write('Personal Administrativo: '+str(contPers)+'\n')
	file.write('Visitantes: '+str(contVist)+'\n')
	file.write('Reporte de vehiculos estacionados segun tipo de vehiculo: \n')
	file.write('Automoviles: '+str(contAut)+'\n')
	file.write('Automoviles Electricos: '+str(contAutElec)+'\n')
	file.write('Motocicletas: '+str(contMotto)+'\n')
	file.write('Automoviles para discapacitados: '+str(contDisc)+'\n')
	file.write('Reporte de porcentaje de ocupacion por piso: \n')
	file.write('Piso 1: '+str(((contP1*100)/100))+'%\n')
	file.write('Piso 2: '+str(((contP2*100)/100))+'%\n')
	file.write('Piso 3: '+str(((contP3*100)/100))+'%\n')
	file.write('Piso 4: '+str(((contP4*100)/100))+'%\n')
	file.write('Piso 5: '+str(((contP5*100)/100))+'%\n')
	file.write('Piso 6: '+str(((contP6*100)/50))+'%\n')
	file.write('Reporte de porcentaje de ocupacion global del parqueadero: \n')
	file.write('Porcentaje de ocupacion global: '+str(((contP1+contP2+contP3+contP4+contP5+contP6)*100)/550)+'%')
	file.close()

'''
Nombre: menu
Objetivo: Permite al usuario seleccionar la opcion que desee.
'''
def menu():
	selec = int(input('Selecciones la opcion que desee realizar:\n1.Registrar vehiculo\n2.Ingresar vehiculo\n3.Retirar vehiculo\n4.Cerrar y generar reportes\n'))
	if selec == 1:
		registrar()
		menu()
	elif selec == 2:
		ingresarVehiculo()
		menu()
	elif selec == 3:
		retirarVehiculo()
		menu()
	elif selec == 4:
		reportes()
		print('Gracias por utilizar nuestro servicio.')

archiwo = open('usuarios.json','r')
users = json.load(archiwo)

file = open('tiposParqueaderos.json','r')
parker = json.load(file)

parkeadero = {'Piso1':[],'Piso2':[],'Piso3':[],'Piso4':[],'Piso5':[],'Piso6':[]}
for pisos in parkeadero.keys():
	if pisos != 'Piso6':
		for o in range(10):
			fila = []
			for i in range(10):
				fila.append('0')
			parkeadero[pisos].append(fila)
	else:
		for o in range(5):
			fila = []
			for i in range(10):
				fila.append('0')
			parkeadero[pisos].append(fila)

listavisitantes = []
parkercopia = copy.deepcopy(parker)
vehiculosEstacionados = {'vehiculos':[]}

print('BIENVENIDO AL SISTEMA DE PARQUEO DE LA PONTIFICIA UNIVERSIDAD JAVERIANA CALI')
menu()
