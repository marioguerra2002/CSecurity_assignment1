def main ():
  method = input ("Enter the method you want to use(substitution or transposition): ")
  operation = input ("Enter the operation you want to use(encrypt or decrypt): ")
  key = input ("Enter the key you want to use: ")
  text = input ("Enter the text you want to use: ")
  with open(text, 'r') as file: # Open the file
    file = text.read() # Read the file
  if method == "substitution":
    if operation == "encrypt":
      procesed_text = encryptSubstitution(key, text)
    elif operation == "decrypt":
      procesed_text = decryptSubstitution(key, text)
    else:
      print("Invalid operation")
      return
  elif method == "transposition":
    if operation == "encrypt":
      procesed_text = encryptTransposition(key, text)
    elif operation == "decrypt":
      procesed_text = decryptTransposition(key, text)
    else:
      print("Invalid operation")
      return
  else:
    print("Invalid method")
    return
  if operation == "encrypt":
    out_text = text + ".enc"
  elif operation == "decrypt":
    out_text = text + ".dec"
  with open(out_text, 'w') as file:
    file.write(procesed_text)
  print("File processed successfully. Saved as ", out_text)
  

    
  