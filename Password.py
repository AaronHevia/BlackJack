import random
import getpass

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
characters = lower + upper + number + chars


#Shuffle characters to create Individual Account Cipher.
def Shuffle():  
  random.shuffle(characters)  
  accountCipher = characters + characters  
  return accountCipher
  

#Create and Verify Password.
def CreatePWD():
  while True:
    password = getpass.getpass("Enter a Password (Password must contain):  ")
    verify = getpass.getpass("Retype your Password:  ")
    if password != verify:
      print("Your Passwords don't match.")
    else:
      break

  return password


#Create and Verify PIN. 
def CreatePIN():  #TODO:  Finalize PIN Verification.
  while True:
    pin = int(getpass.getpass("Enter a 3 to 6 digit PIN:  "))
    verify = int(getpass.getpass("Retype your PIN:  "))
    if pin != verify:
      print


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
  shift = shift % 72
  Caesar(startText=text, shiftAmount=shift, cipherDirection=direction)  
  reload = input("Do you want to cypher again? Type 'yes' or 'no'.").lower()  
  if reload == "yes":
    Run()
  else:
    print("Goodbye!")