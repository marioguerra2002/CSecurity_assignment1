import sys
def encryptTransposition(key, text):
  num_columns = len(key)
  while len(text) % num_columns != 0:
    text += " " # Add spaces to the text until it is divisible by the number of columns
  
  matrix = [list(text[i:i+num_columns]) for i in range(0, len(text), num_columns)]
  #create the matrix. i:i+num_columns is the range of the matrix. It is a list of lists. List conversion is done with list(). Each element of the list is a list of num_columns elements.
  print (matrix)

def main():
  key = "2314765"
  input_file = sys.argv[1]
  
  with open(input_file, 'r') as f: # Open the file
    text = f.read() # Read the file
  encryptTransposition(key, text)
  
  

if __name__ == "__main__":
  main()