def flip(c):
    return '1' if (c == '0') else '0'

def maximum(a, b): 
    if a >= b: 
        return a 
    else: 
        return b

def getOnes(bina):  
    ones = ""   
    for i in range(len(bina)): 
        ones += flip(bina[i]) 
    return ones

def intToBinary(var):
    return (bin(var).split("0b")[1])

def binToInteger(var):
    return (int(var,2))

def BinaryAddition(binarr):
    sum=0
    for i in range(len(binarr)):
        temp=binToInteger(binarr[i])
        sum=sum+temp
    return(bin(sum).split('0b')[1])

def additionCompression(bina,length):
    arr=['']*2
    counter=0
    while len(bina)>length:
        while (counter < length):
            arr[1]=bina[len(bina)-(counter+1)]+str(arr[1])
            counter=counter+1
        while(counter>=length and counter<len(bina)):
            arr[0]=bina[len(bina)-(counter+1)]+str(arr[0])
            counter=counter+1
        bina=BinaryAddition(arr)
    while len(bina)<length:
        bina='0'+bina
    return getOnes(bina)

#CHECKSUM SENDING SIDE
n=input("Enter the number of numbers: ")
n=int(n)
arr=['']*n
length=0
for i in range(n):
    arr[i]=input("Enter Number (in integer without conversion to binary): ")
    arr[i]=intToBinary(int(arr[i]))
    length=maximum(length,len(arr[i]))
for i in range(n):
    while len(arr[i])<length:
        arr[i]='0'+arr[i]
Sum=BinaryAddition(arr)
print("Sum of the numbers:",Sum)
checksum=additionCompression(Sum,length)
print("Ones complement after compressing the addition: ",checksum)
arr.append(checksum)
print("Encoded Message:", arr)


#CHECKSUM RECIEVING SIDE
n=input("Enter the no. of words in the packet received (including checksum): ")
n=int(n)
arr=['']*n
for i in range(n-1):
    print("Enter ",i+1," word in binary: ")
    arr[i]=input()
print("Enter checksum in binary: ")
arr[n-1]=input()
Sum=BinaryAddition(arr)
length=len(arr[0])
Check=additionCompression(Sum,length)
if binToInteger(Check)==0:
    print("No Error found")
    print("The encoded message is: ")
    for i in range(n-1):
        print(binToInteger(arr[i]),"\t")
else:
    print("Error Detected")