Lista = []

art = {}

Lista.append(art)

#-----------------------------------------------------------------------------------------------

def alta ():
  cod_articulo = input("Indique el condigo del articulo ")
  nombre = input("Indique el nombre del articulo ")
  descripcion = input("Indique la descripcion del articulo ")
  precio = input("Indique el precio del articulo ")

  if precio.isdigit():
    
    art = {
      "cod_articulo" : cod_articulo,
      "nombre" : nombre,
      "descripcion" : descripcion,
      "precio" :precio
    }

    Lista.append(art.copy())

  else:
    print("El precio debe ser numerico")

#-----------------------------------------------------------------------------------------------

def listado ():
  i = 0
  for art in Lista:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
   
    print("\n","Posicion: " , i)
    i = i + 1
    for k,v in art.items():        #acedemos a cada llave(k), valor(v) de cada diccionario
        print(k, v)
    print("\n")    

#-----------------------------------------------------------------------------------------------

def baja ():
  print("Introduce la posicion del articulo que desea borrar")
  i = input()
  if i.isdigit():
    i = int(i)
    if (i < len(Lista) and i >= 0):
      i = int(i)
      print("¿Esta seguro que desea borrar ese articulo? Escriba si para borrarlo")
      conf = input()
      if conf == "si":
        Lista.pop(i)
      else:
        print("No se elimino")
    else:
      print("No puede indicar esos valores")
  else:
    print("No es un numero")

#-----------------------------------------------------------------------------------------------

def modificar ():
  listado()
  print("\n", "Indique que posicion desea modificar")
  pos = input()
  if not pos.isdigit():
    print("No ha seleccionado una posicion valida")
  else:
    artSelect = Lista[int(pos)]
    print("\n")
    for k,v in artSelect.items():
        print(k, v)
    
    keyArt = input("Introduce la clave que desea modificar: ")
    valueArt = input("Introduce el valor que desea modificar: ")

    if keyArt == "precio":
      if valueArt.isdigit():
        valueArt = int(valueArt)

        updtArt = {keyArt : valueArt}
        Lista[int(pos)].update(updtArt)

      else:
          print("No es un valor valido")

    else:
      updtArt = {keyArt : valueArt}
      Lista[int(pos)].update(updtArt)


#-----------------------------------------------------------------------------------------------
  
def buscar():
  KeySrch = input("Introduzca una clave que desee buscar: ")
  valueSrch = input("Introduzca un valor que desee buscar: ")

  for i in Lista:
    for k, v in i.items():
      if k == KeySrch and valueSrch == v:
        print(i)


def menu():
  print("Introduce un numero del 1 al 6 de lo que desee acceder")
  print("1 Alta")
  print("2 Baja")
  print("3 Listado")
  print("4 Modificar")
  print("5 Busqueda")
  print("6 Salir")
  slct = input()
  if slct.isdigit():
    slct = int(slct)
    if slct > 0 and slct <=6:
      if slct == 1:
        alta()
        menu()
      if slct == 2:
        baja()
        menu()
      if slct == 3:
        listado()
        menu()
      if slct == 4:
        modificar()
        menu()
      if slct == 5:
        buscar()
        menu()
      if slct == 6:
        print("Se saldra del programa")
    else:
      print("Introdujo mal el valor")
  else:
    print("valor no valido")


menu()

