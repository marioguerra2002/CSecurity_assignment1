import sys
def encryptSubstitution(key, text):
  sum_key = 0
  encrypted_text = "" # Initialize the encrypted text
  for i in range(len(key)):
    sum_key += ord(key[i])
  sum_key = sum_key % 255
  print ("The sum of the key is: ", sum_key)
  for i in range(len(text)):
    if text[i] == " ":
      encrypted_text += " "
    elif text[i] == "\n":
      encrypted_text += "\n"
    else:
      auxiliar = ord(text[i])
      auxiliar = (auxiliar + sum_key) % 255
      auxiliar2 = chr(auxiliar) # Convert the number to letter
      encrypted_text += auxiliar2
  return encrypted_text
def decryptSubstitution(key, text):
  decrypted_text = "" # Initialize the decrypted text
  
  sum_key = 0
  for i in range(len(key)):
    sum_key += ord(key[i])
  sum_key = sum_key % 255
  for i in range(len(text)):
    if text[i] == " ":
      decrypted_text += " "
    elif text[i] == "\n":
      decrypted_text += "\n"
    else:
      auxiliar = ord(text[i])
      auxiliar = (auxiliar - sum_key) % 255
      auxiliar2 = chr(auxiliar) # Convert the number to letter
      decrypted_text += auxiliar2
    
  return decrypted_text
def isMeaningful(text_entry):
    name_file = "text_to_compare.txt"
    path_file = name_file
    # Read the comparator text (the square)
    with open(path_file, 'r') as f:
        text_to_compare = f.read()
    
    
    # Read the text to compare from the commun file
    text_check = text_entry
    
    # Get the first 7 lines of the text to compare
    text_check = text_check.split("\n")
    seven_first_lines = ""
    for i in range(7):
      seven_first_lines += text_check[i]
      seven_first_lines += "\n"
    if text_to_compare == seven_first_lines:
        return True
    else:
        return False
def decryptAndCheckMeaning(text):
    for key in range(54):
        decrypted_text = decryptSubstitution(chr(key), text)
        if isMeaningful(decrypted_text):
          print ("The key is: ", chr(key))
          return decrypted_text
    return None
def encryptTransposition(key, text):
  num_columns = len(key)
  
  original_matrix = []
  begin = 0
  while begin < len(text):
    row = text[begin:begin+num_columns] # Get the row
    if text[begin:begin+num_columns] == "\n": # If the row is a new line
      row = text[begin:begin+num_columns]
    if len(row) < num_columns:
      while len(row) < num_columns: # If the row is not complete, add spaces
        row += " "
    original_matrix.append(list(row))
    begin += num_columns
  
  ## At this point we have the matrix with the text
  ## Now we have to sort it based on the key
  col_dict = {}
  # Save the columns in a vector
  aux_vector = []
  for i in range(len(original_matrix[0])):
    for j in range(len(original_matrix)):
      aux_vector.append(original_matrix[j][i])
    col_dict[i] = aux_vector
    aux_vector = []
  # We have the columns dictionary
  sorted_matrix = []
  for i in range(len(key)):
    sorted_matrix.append(col_dict[int(key[i]) - 1])
  # We have the sorted matrix
  # Invert rows and columns
  inverted_matrix = [list(row) for row in zip(*sorted_matrix)]
  # We have the inverted matrix
  # Convert the matrix to a string (to the text)
  encrypted_text = ""
  for i in range(len(inverted_matrix)):
    for j in range(len(inverted_matrix[i])):
      encrypted_text += inverted_matrix[i][j]
  return encrypted_text
def decryptTransposition(key, text):
  num_columns = len(key)
  
  original_matrix = []
  begin = 0
  while begin < len(text):
    row = text[begin:begin+num_columns] # Get the row
    if text[begin:begin+num_columns] == "\n": # If the row is a new line
      row = text[begin:begin+num_columns]
    if len(row) < num_columns:
      while len(row) < num_columns: # If the row is not complete, add spaces
        row += " "
    original_matrix.append(list(row))
    begin += num_columns
  
  ## At this point we have the matrix with the text
  ## Now we have to sort it based on the key
  col_dict = {}
  # Save the columns in a vector
  aux_vector = []
  for i in range(len(original_matrix[0])):
    for j in range(len(original_matrix)):
      aux_vector.append(original_matrix[j][i])
    col_dict[i] = aux_vector
    aux_vector = []
  # We have the columns dictionary
  sorted_matrix = []
  for i in range(len(key)):
    sorted_matrix.append(col_dict[int(key[i]) - 1])
  # We have the sorted matrix
  # Invert rows and columns
  inverted_matrix = [list(row) for row in zip(*sorted_matrix)]
  # We have the inverted matrix
  # Convert the matrix to a string (to the text)
  decrypted_text = ""
  for i in range(len(inverted_matrix)):
    for j in range(len(inverted_matrix[i])):
      decrypted_text += inverted_matrix[i][j]
  return decrypted_text      
  
def main ():
  method = input ("Enter the method you want to use(substitution or transposition): ")
  operation = input ("Enter the operation you want to use(encrypt or decrypt): ")
  key=""
  input_file = sys.argv[1]
  
  with open(input_file, 'r') as f: # Open the file
    text = f.read() # Read the file
  if method == "substitution":
    if operation == "encrypt":
      key = input ("Enter the key you want to use: ")
      procesed_text = encryptSubstitution(key, text)
    elif operation == "decrypt":
      procesed_text = decryptAndCheckMeaning(text)
    else:
      print("Invalid operation")
      return
  elif method == "transposition":
    if operation == "encrypt":
      key = input ("Enter the key you want to use: ")
      procesed_text = encryptTransposition(key, text)
    elif operation == "decrypt":
      key = input ("Enter the key you want to use: ")
      procesed_text = decryptTransposition(key, text)
    else:
      print("Invalid operation")
      return
  else:
    print("Invalid method")
    return
  if operation == "encrypt":
    out_text = input_file + ".enc"
  elif operation == "decrypt":
    out_text = input_file + ".dec"
  if (procesed_text == None):
    print("The text could not be decrypted")
    return
  with open(out_text, 'w') as file:
    file.write(procesed_text)
  print("File processed successfully. Saved as", out_text)
  
if __name__ == "__main__":
  main() 
  

    
  