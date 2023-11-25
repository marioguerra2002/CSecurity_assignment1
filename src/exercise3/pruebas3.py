import sys

def main():
  key = "421635"
  input_file = sys.argv[1]
  num_columns = len(key)
  
  with open(input_file, 'r') as f: # Open the file
    text = f.read() # Read the file
  num_row = len(key)
  for i in range(len(text)):
    print(text[i])
  
  matrix_text = []
  begin = 0
  while begin < len(text):
    row = text[begin:begin+num_columns]
    if text[begin:begin+num_columns] == "\n":
      row = text[begin:begin+num_columns]
    if len(row) < num_columns:
      while len(row) < num_columns:
        row += " "
    matrix_text.append(list(row))
    begin += num_columns
  print("Matriz original:")
  for row in matrix_text:
    print(row)
  ## en este punto ya tenemos la matriz con el texto
  ## ahora hay que ordenarla en base a la key
  col_dict = {}
  print(len(matrix_text))
  #guardar en vector las columnas
  aux_vector = []
  print(len(matrix_text[0]))
  for i in range(len(matrix_text[0])):
    for j in range(len(matrix_text)):
      aux_vector.append(matrix_text[j][i])
    col_dict[i] = aux_vector
    aux_vector = []  
  print(col_dict)
  # tenemos el diccionario de columnas (siuuuu)
  matrix_sorted = []
  for i in range(len(key)):
    matrix_sorted.append(col_dict[int(key[i]) - 1])
  print("Matriz ordenada:")
  for row in matrix_sorted:
    print(row)
  # tenemos la matriz ordenada (siuuuu)
  # invertimos filas y columnas
  matrix_inverted = [list(row) for row in zip(*matrix_sorted)]
  print("Matriz invertida:")
  for row in matrix_inverted:
    print(row)
  # tenemos la matriz invertida (siuuuu)
  # convertimos la matriz en un string
  encrypted_text = ""
  for i in range(len(matrix_inverted)):
    for j in range(len(matrix_inverted[i])):
      encrypted_text += matrix_inverted[i][j]
  print(encrypted_text)
  
  

if __name__ == "__main__":
  main()