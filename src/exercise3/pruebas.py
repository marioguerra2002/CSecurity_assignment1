import sys

def main():
  if len(sys.argv) < 2:
    print("Debe proporcionar el nombre del archivo como argumento.")
    return

  archivo = sys.argv[1]

  try:
    with open(archivo, 'r') as f:
      contenido = f.read()
      # Utiliza el contenido del archivo aquí
    text_output = ""
    for i in range(len(contenido)):
      if contenido[i].isupper(): # Si es mayúscula
        #imaginemos que la key tiene como valor 4. Hay que convertir la letra a número, sumarle 4 y convertirlo de nuevo a letra
        #Para convertir de letra a número, se puede usar la función ord()
        #Para convertir de número a letra, se puede usar la función chr()
        print ("Valor de i: ", contenido[i])
        auxiliar = ord(contenido[i]) # Convertir la letra a número
        auxiliar = (auxiliar + 4) % 256 # Aplicar la key.El 256 es porque hay 256 caracteres en ASCII
        print ("Valor de auxiliar: ", auxiliar)
        print ("\n")
        auxiliar = chr(auxiliar)
        text_output += auxiliar
      elif contenido[i].islower(): # Si es minúscula
        auxiliar = ord(contenido[i])
        auxiliar = (auxiliar + 4) % 256
        auxiliar = chr(auxiliar)
        text_output += auxiliar 
      elif contenido[i] == " ":
        text_output += " "
      elif contenido[i] == "\n":
        text_output += "\n"
      else:
        print("El archivo contiene caracteres no válidos.")
        return
      out_file = archivo + ".enc"
      with open(out_file, 'w') as file:
        file.write(text_output)
      print("El archivo se ha encriptado correctamente.") 
        
        
  except FileNotFoundError:
    print(f"No se encontró el archivo: {archivo}")

if __name__ == "__main__":
  main()
