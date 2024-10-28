# Mohamed Nabil Mohamed Abusarea  ID: 20231219
# Mohamed Sheref Abdelazim Rady   ID: 20231142
# Walid Adel Mordy Rohyem         ID: 20231200

def Convert_Numbers_Characters(num):
  if(num == "10"):
    return "A"
  elif(num == "11"):
    return "B"
  elif(num == "12"):
    return "C"
  elif(num == "13"):
    return "D"
  elif(num == "14"):
    return "E"
  elif(num == "15"):
    return "F"
  else:
    return num
def Check_numbers8and9(integer_num):
  numbers="89"
  for i in range(len(integer_num)):
    for j in range(len(numbers)):
      if(integer_num[i]==numbers[j]):
        return 1

  return 0
def Check_numbers_from2to9(integer_num):
  numbers="23456789"
  for i in range(len(integer_num)):
    for j in range(len(numbers)):
      if(integer_num[i]==numbers[j]):
        return 1

  return 0
#some functions to check the inpute number
def Check_Decimal(integer_num):
  for i in range(len(integer_num)):
    if(integer_num[i]=="." or Check_Character_fromAtof(integer_num)):
      return 0
  if(int(integer_num)<0):
    return 0
  else:
    return 1
def Check_Binary(integer_num):
  for i in range(len(integer_num)):
    if(integer_num[i]=="." or Check_Character_fromAtof(integer_num)):
      return 0
  if(int(integer_num)<0):
    return 0
  
  if(Check_numbers_from2to9(integer_num)):
    return 0
  else:
    return 1
def Check_Octal(integer_num):
  for i in range(len(integer_num)):
    if(integer_num[i]=="." or Check_Character_fromAtof(integer_num)):
      return 0
  if(int(integer_num)<0):
    return 0

  if(Check_numbers8and9(integer_num)):
    return 0
  else:
    return 1
def Check_Hexa(integer_num):
  for i in range(len(integer_num)):
    if(integer_num[i]=="." ):
      return 0
  if(integer_num[i]=="-"):
    return 0
  else:
    return 1

def Check_Character_fromAtoD(CharFromUser):
  characters="AaBbCcDd"
  for i in range(len(characters)):
    if(CharFromUser==characters[i]):
      return 1
  return 0  
def Check_Character_fromAtof(integer_num):
  characters="AaBbCcDdEeFf"
  for i in range(len(integer_num)):
    for j in range(len(characters)):
      if(integer_num[i]==characters[j]):
        return 1
    
  return 0  
#some functions to convert from Decimal
def Decimal_To_Binary(decimal):
  temp_binary=""  
  while(decimal!=0): 
    remainder=float(decimal)/2
    if remainder==int(remainder):
       temp_binary += "0"
    elif remainder!=int(remainder):
       temp_binary += "1"
    decimal=int(remainder)
  binary=""
  #i use this for loop to reverse the biary number to be coreect
  for i in range (len(temp_binary)):
   binary += temp_binary[((len(temp_binary))-1)-i]
  return binary
def Decimal_To_octal(decimal):
  temp_octal=""
  while(decimal!=0): 
   remainder=float(decimal)/8
   temp_octal += str(int((remainder- int(remainder))*8))
   decimal=int(remainder)
  octal=""
  for i in range (len(temp_octal)):
   octal += temp_octal[((len(temp_octal))-1)-i]
  return octal
def Decimal_To_Hexa(decimal):
  temp_hexa=""
  while(decimal!=0): 
   remainder=float(decimal)/16
   temp_hexa += Convert_Numbers_Characters(str(int((remainder- int(remainder))*16)))
   decimal=int(remainder)
  hexadecimal=""
  for i in range (len(temp_hexa)):
   hexadecimal += temp_hexa[((len(temp_hexa))-1)-i]
  return hexadecimal
def Decimal_To_Decimal(decimal):
  return decimal
def Decimal_To_ANYTHING(integer_num):
  CharFromUser= menu3()
  while(Check_Character_fromAtoD(CharFromUser)==0):#Test=Aa-Bb-Cc-Dd-other character
    CharFromUser=input("please enter a valid choise(A/B/C/D): ")
  if(CharFromUser == "A" or CharFromUser ==  "a"):#input 12345
    while(Check_Decimal(integer_num)==0):
      print("Error,Invalid number")
      menu2()
    print("The result is : ",Decimal_To_Decimal(integer_num))
    menu1()
  elif(CharFromUser == "B" or CharFromUser ==  "b"):#input 45
    while(Check_Decimal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Decimal_To_Binary(integer_num))#output  101101
    menu1()
  elif(CharFromUser == "C" or CharFromUser ==  "c"):#input 45
    while(Check_Decimal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Decimal_To_octal(integer_num))#output 55
    menu1()
  elif(CharFromUser == "D" or CharFromUser ==  "d"):#input 245
    while(Check_Decimal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Decimal_To_Hexa(integer_num))#output F5
    menu1()

#some functions to convert from Octal
def Octal_To_Octal(octal):
  return octal
def Octal_To_Decimal(octal):
 decimal = 0
 octal=int(octal)
 for i in range(len(str(octal))):
  decimal += (octal % 10 )*(8**i)
  octal = int(octal / 10)
 return decimal
def Octal_To_Binary(octal):
  binary = ""
  octal_len = len(octal)
  i = 0
  while i<octal_len:
      if octal[i] == '0':
          binary+= "000"
      elif octal[i] == '1':
          binary+= "001"
      elif octal[i] == '2':
          binary+="010"
      elif octal[i] == '3':
          binary+="011"
      elif octal[i] == '4':
          binary+="100"
      elif octal[i] == '5':
          binary+="101"
      elif octal[i] == '6':
          binary+="110"
      elif octal[i] == '7':
          binary+="111"
      i = i+1

  return binary
def Octal_To_Hexa(octal):
  Hexa=""
  bin=str(Octal_To_Binary(octal))
  bin_len=len(bin)
  while(bin_len %4 !=0):
   bin = "0"+ bin
   bin_len = len(bin)
  for i in range(bin_len):
    digit_for_hex = ""
    digit_for_hex +=bin[i]
    if((len(digit_for_hex))%4 == 0 ):
      Hexa += str(Binary_To_Decimal(digit_for_hex))

  return Hexa
def Octal_To_ANYTHING(integer_num):
  CharFromUser= menu3()
  while(Check_Character_fromAtoD(CharFromUser)==0):
    CharFromUser=input("please enter a valid choise(A/B/C/D): ")
  if(CharFromUser == "A" or CharFromUser ==  "a"):
    while(Check_Octal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Octal_To_Decimal(integer_num))
    menu1()
  elif(CharFromUser == "B" or CharFromUser ==  "b"):
    while(Check_Octal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Octal_To_Binary(integer_num))
    menu1()
  elif(CharFromUser == "C" or CharFromUser ==  "c"):
    while(Check_Octal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Octal_To_Octal(integer_num))
    menu1()
  elif(CharFromUser == "D" or CharFromUser ==  "d"):
    while(Check_Octal(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Octal_To_Hexa(integer_num))
    menu1()

#Some functions to convert from Binary
def Binary_To_Binary(binary):
 return binary 
def Binary_To_Hexa(binary):
  binary = int(binary)
  decimal = 0
  pwr = 0
  if binary == 0:
      print("The hexadecimal equivalence of this number is: 0")
  else:
      while binary > 0:
          # Use % to get the remainder and // to get the integer from the division
          digit = binary % 10
          if digit != 0 and digit != 1:
              print("Error, the binary numbers contain 0s and 1s only")
              binary = int(input("Enter the binary number you want to convert: "))
          else:
              decimal += digit * (2 ** pwr)
              binary //= 10
              pwr += 1
      # Convert decimal to hexadecimal
      hexadecimal = ""
      while decimal > 0:
          remainder = decimal % 16
          if remainder < 10:
              hexadecimal += str(remainder)
          else:
              hexadecimal += chr(ord('A') + remainder - 10)
          decimal //= 16
      
      return (hexadecimal[::-1])
def Binary_To_Octal(binary):
  octal = ""
  slot = ""
  while((len(binary)%3)!=0):
    binary = "0" + binary
  for i in range((len(binary))):
   slot = slot + binary[i]
   if(i%3):
     if slot == "000":
         octal+= "0"
         slot = ""
       
     elif slot == "001":
         octal+= "1"
         slot = ""
       
     elif slot == "010":
         octal+="2"
         slot = ""
       
     elif slot == "011":
         octal+= "3"
         slot = ""
     elif slot == "100":
         octal+= "4"
         slot = ""
     elif slot == "101":
         octal+= "5"
         slot = ""
     elif slot == "110":
         octal+= "6"
         slot = ""
     elif slot == "111":
         octal+= "7"
         slot = ""
  return octal
def Binary_To_Decimal(binary):
  length=len(binary)
  result=0
  for i in range (length):
     num1=int(binary[(length-1)-i])
     if num1!=0:
          result+=2**i    
  return result
def Binary_To_ANYTHING(integer_num):
  CharFromUser= menu3()
  while(Check_Character_fromAtoD(CharFromUser)==0):
    CharFromUser=input("please enter a valid choise(A/B/C/D): ")
  if(CharFromUser == "A" or CharFromUser ==  "a"):
    while(Check_Binary(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Binary_To_Decimal(integer_num))
    menu1()
  elif(CharFromUser == "B" or CharFromUser ==  "b"):
    while(Check_Binary(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Binary_To_Binary(integer_num))
    menu1()
  elif(CharFromUser == "C" or CharFromUser ==  "c"):
    while(Check_Binary(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Binary_To_Octal(integer_num))
    menu1()
  elif(CharFromUser == "D" or CharFromUser ==  "d"):
    while(Check_Binary(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Binary_To_Hexa(integer_num))
    menu1()

#Some functions to convert from Hexa
def Hexa_To_Hexa(Hexa):
  return Hexa
def Hexa_To_Decimal(Hexa):
  #  *** from Hexadecimel to Decimal ***
  Hexa = Hexa.lower()
  length=len(Hexa)
  #A,B,C,D,E,F=10,11,12,13,14,15
  result=[]
  use_num=[]
  end_resul=0
  for i in range(length):
      result.append(16**i)

  for y in Hexa :
          if y=='a':
             y=10
          elif y=='b':
             y=11
          elif y=='c':
             y=12
          elif y=='d':
             y=13
          elif y=='e':
             y=14
          elif y=='f':
             y=15

          use_num.append(str(y))
  for i in range (length):
        end_resul+=((result[i])*(int(use_num[(length-1)-i])))

  return end_resul
def Hexa_To_Binary(hexa_num):
  #**** From Hexadecimal to Binary ****
  binary = ""
  hexlen = len(hexa_num)
  check=0
  i = 0
  while i<hexlen:
      if hexa_num[i] == '0':
          binary+= "0000"
      elif hexa_num[i] == '1':
          binary+= "0001"
      elif hexa_num[i] == '2':
          binary+="0010"
      elif hexa_num[i] == '3':
          binary+="0011"
      elif hexa_num[i] == '4':
          binary+="0100"
      elif hexa_num[i] == '5':
          binary+="0101"
      elif hexa_num[i] == '6':
          binary+="0110"
      elif hexa_num[i] == '7':
          binary+="0111"
      elif hexa_num[i] == '8':
          binary+="1000"
      elif hexa_num[i] == '9':
          binary+="1001"
      elif hexa_num[i] == 'A' or hexa_num[i] == 'a':
          binary+="1010"
      elif  hexa_num[i] == 'B'or hexa_num[i] == 'b':
          binary+="1011"
      elif hexa_num[i] == 'C' or hexa_num[i] == 'c':
          binary+="1100"
      elif hexa_num[i] == 'D' or hexa_num[i] == 'd':
          binary+="1101"
      elif hexa_num[i] == 'E' or hexa_num[i] == 'e':
          binary+="1110"
      elif hexa_num[i] == 'F'or hexa_num[i] == 'f':
          binary+="1111"
      i = i+1
  
  return binary
def Hexa_To_Octal(hexa_num):
  #From Hexadecimal to Octal
  octal =""
  check = 0
  decnum = 0
  hexa_numlen = len(hexa_num)
  hexa_numlen = hexa_numlen-1
  i = 0
  while hexa_numlen>=0:
      rem = hexa_num[hexa_numlen]
      if rem>='0' and rem<='9':
          rem = int(rem)
      elif rem>='A' and rem<='F':
          rem = ord(rem)
          rem = rem-55
      elif rem>='a' and rem<='f':
          rem = ord(rem)
          rem = rem-87
      else:
          check = 1
          break
      decnum += (rem * (16 ** i))
      hexa_numlen = hexa_numlen-1
      i = i+1

  if check==0:
      i = 0
      oct_num = []
      while decnum!=0:
          rem = decnum%8
          oct_num.insert(i, rem)
          i = i+1
          decnum = int(decnum/8)
      i = i-1
      while i>=0:
          octal+= str(oct_num[i])
          i = i-1
  return octal
def Hexa_To_ANYTHING(integer_num):
  CharFromUser= menu3()
  while(Check_Character_fromAtoD(CharFromUser)==0):
    CharFromUser=input("please enter a valid choise(A/B/C/D): ")
  if(CharFromUser == "A" or CharFromUser ==  "a"):
    while(Check_Hexa(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Hexa_To_Decimal(integer_num))
    menu1()
  elif(CharFromUser == "B" or CharFromUser ==  "b"):
    while(Check_Hexa(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Hexa_To_Binary(integer_num))
    menu1()
  elif(CharFromUser == "C" or CharFromUser ==  "c"):
    while(Check_Hexa(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Hexa_To_Octal(integer_num))
    menu1()
  elif(CharFromUser == "D" or CharFromUser ==  "d"):
    while(Check_Hexa(integer_num)==0):
     print("Error,Invalid number")
     menu2()
    print("The result is : ",Hexa_To_Hexa(integer_num))
    menu1()
#Functions to dispaly menu1 , menu2 and menu3
def menu1():
  print("** numbering system converter **")
  print("A) insert a new number")
  print("B) Exit program")
  choice = input("please insert your choise (A/B): ")#Test=Aa-Bb-other character-numbers
  if(choice == "A" or choice ==  "a"):
     menu2()
  elif(choice == "B" or choice ==  "b"):
    exit()
  else:
   print("please select a valid choice. \n")
   menu1()
def menu2():
  integer_num = input("Insert a  number : ")
  print("** Please select the base you want to convert a number from**")
  print("A) Decimal")
  print("B) Binary")
  print("C) Octal")
  print("D) Hexadecimal")
  CharFromUser=input("please enter the character : ")
  while(Check_Character_fromAtoD(CharFromUser)==0):#Test=Aa-Bb-Cc-Dd-other characters
    CharFromUser=input("please enter a valid choise(A/B/C/D): ")
  if(CharFromUser == "A" or CharFromUser ==  "a"):
     Decimal_To_ANYTHING(integer_num)
  elif(CharFromUser == "B" or CharFromUser ==  "b"):
    Binary_To_ANYTHING(integer_num)
  elif(CharFromUser == "C" or CharFromUser ==  "c"):
    Octal_To_ANYTHING(integer_num)
  elif(CharFromUser == "D" or CharFromUser ==  "d"):
    Hexa_To_ANYTHING(integer_num)
def menu3():
  print("** Please select the base you want to convert a number to **")
  print("A) Decimal")
  print("B) Binary")
  print("C) Octal")
  print("D) Hexadecimal")
  CharFromUser=""
  CharFromUser= input("enter the character : ")
  return CharFromUser
  
menu1()