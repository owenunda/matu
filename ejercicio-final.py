from colorama import Fore, Style, init, Back
import random
init(autoreset=True)

opc = 1
puntajeActualUser = 0
puntajeActualCPU = 0

# logica del juego
def juego(seleccionCPU, opcionUser): 
  
  def eleccionCPU(seleccionCPU):
    if seleccionCPU == 1:
      print(Fore.MAGENTA + f'seleccion de la cpu: Piedra')
    elif seleccionCPU == 2:
      print(Fore.MAGENTA + f'seleccion de la cpu: Papel')
    elif seleccionCPU == 3:
      print(Fore.MAGENTA + f'seleccion de la cpu: Tijera')

  # eleccionCPU(seleccionCPU)
  puntajeCPU = 0
  puntajeUser = 0
  

  # empate
  if seleccionCPU == opcionUser:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== EMPATE ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'Los dos optienen ' + Fore.RED + '0' + Fore.MAGENTA + ' puntos')
    puntajeCPU += 0
    puntajeUser += 0

  # piedra gana tijera
  if opcionUser == 1 and seleccionCPU == 3:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== JUGADOR GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'El jugador optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeUser += 100
  elif opcionUser == 3 and seleccionCPU == 1:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== CPU GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'la cpu optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeCPU += 100

  # tijera gana papel
  if opcionUser == 3 and seleccionCPU == 2:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== JUGADOR GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'El jugador optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeUser += 100
  elif opcionUser == 2 and seleccionCPU == 3:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== CPU GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'la cpu optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeCPU += 100

  # papel gana priedra
  if opcionUser == 2 and seleccionCPU == 1:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== JUGADOR GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'El jugador optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeUser += 100
  elif opcionUser == 1 and seleccionCPU == 2:
    print(Style.BRIGHT + Fore.MAGENTA + '=============== CPU GANA ===============')
    eleccionCPU(seleccionCPU)
    print(Fore.MAGENTA + 'la cpu optiene ' + Fore.GREEN + '100' + Fore.MAGENTA + ' puntos')
    puntajeCPU += 100



  return {
    'user': puntajeUser,
    'cpu': puntajeCPU
  }

while opc != 0:
  seleccionCPU = random.randrange(1, 4)
  print(Style.BRIGHT + Fore.MAGENTA +  '=============== BIENVENIDO ===============')
  print(Fore.GREEN + 'Opciones disponibles\n1. Piedra\n2. Papel\n3. Tijera\n4. Salir (salir de juego)  ')

  # para el color deacuerdo al puntaje
  if(puntajeActualUser <= 0):
    print(Fore.YELLOW + 'Puntaje actual jugador:' + Fore.RED + f' {puntajeActualUser}')
  else:
    print(Fore.YELLOW + 'Puntaje actual jugador:' + Fore.GREEN + f' {puntajeActualUser}')

  if(puntajeActualCPU <= 0):
    print(Fore.YELLOW + 'Puntaje actual CPU:' + Fore.RED + f' {puntajeActualCPU}')
  else:
    print(Fore.YELLOW + 'Puntaje actual CPU:' + Fore.GREEN + f' {puntajeActualCPU}')


  print(Fore.MAGENTA + Style.BRIGHT + '==============================')
  print(Fore.BLUE + 'Selecciona una opcion (1 - 4)' )
  opcionUser = 0
  
  ## validacion de entrada
  while True:
    try:
      entrada = input(': ')
      opcionUser = int(entrada)

      if 1 <= opcionUser <= 4:
        break
      else:
        print(Fore.RED + Style.BRIGHT + 'Opcion fuera de rango! Debe ser un número entre 1 y 4')
    
    except ValueError:
      print(Fore.RED + Style.BRIGHT + 'Entrada no valida, por favor ingresa un numero')

  
  # salida
  if opcionUser == 4:
    print(Fore.MAGENTA + Style.BRIGHT + '=============== Gracias por jugar ===============')
    opc = 0
  else:
    result = juego(seleccionCPU, opcionUser)
    puntajeActualCPU += result["cpu"]
    puntajeActualUser += result["user"]
  

