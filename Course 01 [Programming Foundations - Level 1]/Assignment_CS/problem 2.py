# Walid Adel Mordy Rohym         ID/ 20231200                        
# Mohammed Nabil Mohammed        ID/ 20231219
# Mohammed Sheref Abdelazim Rady ID/ 20231142 

#************ Multiplication on Binary number *************
def multi_binary(num1,num2):
    # 2)check if the input is a binary number or not.
    while True: 
        if all(digit=='0' or digit=='1' for digit in num1):
            break 
        else:
            print('Please, Enter a Binary digits (1s and 0s)')
            num1=input()
    # 4)check if the input is a binary number or not.
    while True: 
        if all(digit=='0' or digit=='1' for digit in num1):
            break 
        else:
            print('Please, Enter a Binary digits (1s and 0s)')
            num2=input()
    length=len(num1)
    result=[]
    retu_resul=0
    for i in range(length):
        result.append(2**i)
    for i in range(length):
        retu_resul+=((result[i]))*(int(num1[(length-1)-i]))
    length=len(num2)
    result=[]
    retu_resul2=0
    for i in range(length):
        result.append(2**i)
    for i in range(length):
        retu_resul2+=((result[i]))*(int(num2[(length-1)-i]))
    end_result=retu_resul*retu_resul2
    resul=''
    final_result=''
    while end_result!=0:
        remainder=end_result%2
        if remainder==0:
            resul+='0'
        elif remainder !=0:
            resul+='1'
        end_result//=2
    length=len(resul)
    for i in range(length):
        final_result+=resul[(length-1)-i]
    return final_result
#********** One`s Complemnt************
def one_comp(num):
    while True:    #Check if the input is valid or not.
        if all(i=='0'or i=='1'for i in num ):
            break
        else: 
            print('Invalid input, Please, Enter a Binary number (0s and 1s) only.  ')
            num=input('Please, Enter the number: ')
    result=''
    for i in num:
        if i=='1':
            result+="0"
        elif i=='0':
            result+='1'
    return result
#*********** Subtraction of two binary numbers **************
def subtract(num1_str,num2_str):
    max_len = max(len(num1_str), len(num2_str))
    num1_str = num1_str.zfill(max_len)
    num2_str = num2_str.zfill(max_len)
    num1 = int(num1_str)
    num2 = int(num2_str)
    # initial values of some variables
    borrow = 0
    result = 0
    position = 1
    subtraction_digits = []
    while num1 > 0 or num2 > 0 or borrow > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        digit_subtraction = digit1 - digit2 + borrow
        subtraction_digits.insert(0, str(digit_subtraction % 2))
        borrow = digit_subtraction // 2
        position *= 10
        num1 //= 10
        num2 //= 10
    # the final output
    return "".join(subtraction_digits)
#********** Sum of two binary numbers ***************
def summ(num1_str,num2_str):
    #(Sum of two binary numbers)
    num1 = int(num1_str)
    num2 = int(num2_str)
    # initial values for some variables
    carry = 0
    result = 0
    position = 1
    sum_digits = []
    while num1 > 0 or num2 > 0 or carry > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        digit_sum = digit1 + digit2 + carry
        sum_digits.insert(0, str(digit_sum % 2))
        carry = digit_sum // 2
        position *= 10
        num1 //= 10
        num2 //= 10
    # The final output
    return "".join(sum_digits)
#***************** Two's complement ******************
def two_comp(num):
    # (Two's complement)
    # Check if the input is a valid binary number
    while True:
        if all(i == '0' or i == '1' for i in num):
            break
        else:
            print('Invalid input, Please, Enter a Binary number (0s and 1s) only. ')
            num = input('Please, Enter the binary number: ')
    # One's complement
    result = ''
    for i in num:
        if i == '1':
            result += '0'
        elif i == '0':
            result += '1'
    # Add 1 to get two's complement
    carry = 1
    two_complement = ''
    if str(num) == '0' * len(str(num)):
        for i in reversed(result):
            x = "1" + str(num)
            print("Two's complement is:", x)
            break
    else:
        for i in reversed(result):
            bit_sum = int(i) + carry
            two_complement += str(bit_sum % 2)
            carry = bit_sum // 2
        two_complement = two_complement[::-1]
        return two_complement
#*************** Binary Calculator *******************
def stage():
        number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
        number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
            print(multi_binary(number1,number2))
        else:
            print('Invalid input! please type a valid number')
def menu2():
    desire=input('''****** Please select the operation ******
    A) Compute One`s comlement
    B) Compute two`s complement
    C) Adition
    D) Subtraction
    M) multiplication
    -------> ''').lower()
    if desire =='a':
        number=input('---> Please, Enter the binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number): 
            print(one_comp(number))
        else:
           print('Invalid input! please type a valid number') 
           number=input('---> Please, Enter the binary number which it`s digits (0s and 1s): ')
        #Check 
           if all(i=='0' or i=='1' for i in number): 
              print(one_comp(number))
    elif desire=='b':
        number=input('---> Please, Enter the binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number): 
            print(two_comp(number))
        else:
            print('Invalid input! please type a valid number')
            number=input('---> Please, Enter the binary number which it`s digits (0s and 1s): ')
        #Check 
            if all(i=='0' or i=='1' for i in number): 
               print(two_comp(number))
    elif desire=='c':
        number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
        number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
            print(summ(number1,number2))
        else:
            print('Invalid input! please type a valid number')
            number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
            number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
            if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
                print(summ(number1,number2))
    elif desire=='d':
        number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
        number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
            print(subtract(number1,number2))
        else:
            print('Invalid input! please type a valid number')
            number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
            number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
            if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
                print(subtract(number1,number2))
    elif desire =='m':
        number1=input('---> Please, Enter the first binary number which it`s digits (0s and 1s): ')
        number2=input('---> Please, Enter the second binary number which it`s digits (0s and 1s): ')
        #Check 
        if all(i=='0' or i=='1' for i in number1) and all(i=='0' or i=='1' for i in number2): 
            print(multi_binary(number1,number2))
        else:
            print('Invalid input! please type a valid number')
            stage()
    else:
        print('Invalid input please follow the instructions')
        menu2()
def menu1():
    choice=input('''--->To insert a number press (A)
---> To exit program press (B): ''').upper()
    if choice =='A':
            menu2()
            menu1()
    elif choice =='B':
            print('Thanks for using the App') 
    else:
        print('''Invalid input!
    Please, Follow the instructions ''')
        menu1()
        
menu1()