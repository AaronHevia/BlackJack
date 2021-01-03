characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'
]

def Caesar(startText, shiftAmount, cipherDirection):
  endText = ""
  if cipherDirection == "decode":
    shiftAmount *= -1
  for char in startText:
    if char not in alphabet:
      endText += char
    else:    
      index = alphabet.index(char)
      shiftIndex = index + shiftAmount
      endText += alphabet[shiftIndex]    
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