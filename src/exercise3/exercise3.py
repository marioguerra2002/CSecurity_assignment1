import sys
def encryptSubstitution(key, text):
  sum_key = 0
  encrypted_text = "" # Initialize the encrypted text
  for i in range(len(key)):
    sum_key += ord(key[i])
  sum_key = sum_key % 255
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
def encryptTransposition(key, text):
  num_columns = len(key)
  while len(text) % num_columns != 0:
    text += " " # Add spaces to the text until it is divisible by the number of columns
  
  matrix = [list(text[i:i+num_columns]) for i in range(0, len(text), num_columns)] # Create the matrix
  #i:i+num_columns is the range of the matrix. It is a list of lists. List conversion is done with list(). Each element of the list is a list of num_columns elements.
  
def main ():
  method = input ("Enter the method you want to use(substitution or transposition): ")
  operation = input ("Enter the operation you want to use(encrypt or decrypt): ")
  key=""
  key = input ("Enter the key you want to use: ")
  
  input_file = sys.argv[1]
  
  with open(input_file, 'r') as f: # Open the file
    text = f.read() # Read the file
  if method == "substitution":
    if operation == "encrypt":
      procesed_text = encryptSubstitution(key, text)
    elif operation == "decrypt":
      procesed_text = decryptSubstitution(key, text)
  #   else:
  #     print("Invalid operation")
  #     return
  # elif method == "transposition":
  #   if operation == "encrypt":
  #     procesed_text = encryptTransposition(key, text)
  #   elif operation == "decrypt":
  #     procesed_text = decryptTransposition(key, text)
  #   else:
  #     print("Invalid operation")
  #     return
  else:
    print("Invalid method")
    return
  if operation == "encrypt":
    out_text = input_file + ".enc"
  elif operation == "decrypt":
    out_text = input_file + ".dec"
  with open(out_text, 'w') as file:
    file.write(procesed_text)
  print("File processed successfully. Saved as", out_text)
  # # with open(input_file, 'w') as file:
  # #   file.write(procesed_text)
  
if __name__ == "__main__":
  main() 
  

    
  