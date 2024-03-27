import random
import string

len=int(input("Enter Password Length : "))
print("Choose Character set for Password from these :"
      "1. Digit "
      "2. Letter"
      "3. Special Characters"
      "4. Exit")

Chatacterlist=""

while(True):
      Choice = int(input("Enter a Number : "))
      if(Choice == 1):
            Chatacterlist += string.digits
      elif(Choice == 2):
            Chatacterlist += string.ascii_letters
      elif(Choice == 3):
            Chatacterlist += string.punctuation
      elif(Choice ==4):
            break
      else:
            print("Please Enter a Valid Option")
Password = []
for i in range(len):
      randomchar = random.choice(Chatacterlist)
      Password.append(randomchar)

print("This is your Password : ",Password)


