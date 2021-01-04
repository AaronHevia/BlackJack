import random
import getpass

characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'
]

#Shuffle characters to create Individual Account Cipher.
def Shuffle():
  accountCipher = []  
  random.shuffle(characters)  
  accountCipher.append(characters)
  accountCipher.append(characters)
  return accountCipher
  

#Create and Verify Password.
def CreatePWD():
  while True:
    password = getpass.getpass("Enter a Password:  ")
    verify = getpass.getpass("Retype your Password:  ")
    if password != verify:
      print("Invalid entry.")
    else:
      break

  return password

#Create and Verify PIN.

#Create character list.

#Validate Account.

#Forgot Password.

#Forgot PIN.

def Caesar(startText, shiftAmount, cipherDirection):
  endText = ""
  if cipherDirection == "decode":
    shiftAmount *= -1
  for char in startText:
    if char not in characters:
      endText += char
    else:    
      index = characters.index(char)
      shiftIndex = index + shiftAmount
      endText += characters[shiftIndex]    
  print(f"Here's the {cipherDirection}d result:  {endText}")

def Run():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))  
  shift = shift % 26
  Caesar(startText=text, shiftAmount=shift, cipherDirection=direction)  
  reload = input("Do you want to cypher again? Type 'yes' or 'no'.").lower()  
  if reload == "yes":
    Run()
  else:
    print("Goodbye!")