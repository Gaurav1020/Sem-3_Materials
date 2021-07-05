def intToBinary(var):
    return (bin(var).split("0b")[1])

def binToInteger(var):
    return (int(var,2))

def stringToList(s):
    arr=['']*(len(s))
    for i in range(len(s)):
        arr[i]=s[i]
    return arr

def listToString(arr):  
    string = ""   
    for element in arr:  
        string += element
    return str(string) 

def RemainderDecode(divisor,dividend):
    divisor=stringToList(divisor)
    dividend=stringToList(dividend)
    xorterm=''
    counter=0
    divisor=listToString(divisor)
    while (len(str(xorterm))<=len(divisor)):
        
        if (counter!=len(dividend)):
            xorterm = str(xorterm)+ dividend[counter]
            counter = counter + 1
        if (len(str(xorterm))==len(divisor)):
            xorterm=intToBinary(binToInteger(xorterm)^binToInteger(divisor))
            if (binToInteger(xorterm)==0):
                xorterm=''
        if (counter==len(dividend)):
            if xorterm==divisor:
                xorterm='0'
            return str(xorterm)


def Remainder(divisor, dividend):
    divisor=stringToList(divisor)
    dividend=stringToList(dividend)
    extension=len(divisor) - 1
    for i in range(extension):
        dividend.append('0')
    xorterm=''
    counter=0
    divisor=listToString(divisor)
    while (len(str(xorterm))<=len(divisor)):
        
        if (counter!=len(dividend)):
            xorterm = str(xorterm)+ dividend[counter]
            counter = counter + 1
        if (len(str(xorterm))==len(divisor)):
            xorterm=intToBinary(binToInteger(xorterm)^binToInteger(divisor))
            if (binToInteger(xorterm)==0):
                xorterm=''
        if (counter==len(dividend)):
            if xorterm==divisor:
                xorterm='0'
            return str(xorterm)


def CRCEncoder(divisor, dividend, remainder):
    n=len(divisor)-1
    remainder=str(remainder)
    while len(remainder)<n:
        remainder='0'+remainder
    dividend=dividend+remainder
    return dividend

#Encoding
divisor=str(input("Enter Divisor(in Binary Format): "))
dividend=str(input("Enter Dividend(in Binary Format): "))
print("The Remainder(error detection bit) is: ",Remainder(divisor,dividend))
print("The Encoded Message is: ",CRCEncoder(divisor,dividend,Remainder(divisor,dividend)))

#Decoding
dividend=str(input("Enter Encoded Message(in Binary Format): "))
divisor=str(input("Enter Divisor(in Binary Format): "))
if(RemainderDecode(divisor,dividend)==''):
    n='0'
else:
    n=RemainderDecode(divisor,dividend)
if (int(n)==0):
    print("No Error detected")
else:
    print("Error detected. Packet Trashed")
