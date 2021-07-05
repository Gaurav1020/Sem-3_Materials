def calcRedundantBits(m): 
    for i in range(m): 
        if(2**i >= m + i + 1): 
            return i 

def DecodeProcessing(arr):
    del arr[0]
    temp=(reverseArray(arr))
    return temp

def reverseArray(arr):
    temp=['']*len(arr)
    for i in range(len(arr)):
        temp[i]=arr[-(i+1)]
    return temp

def getParity( n ): 
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return parity 

def intToBinary(var):
    return (bin(var).split("0b")[1])

def binToInteger(var):
    return (int(var,2))

def listToString(arr):  
    string = ""   
    for element in arr:  
        string += element
    return string 

def arrRedundantPosition(r):
    arrRedundantPos=[]
    for i in range(r):
        arrRedundantPos.append(2**i-1)
    return arrRedundantPos

def getParitybit(arr, r):
    temp=''
    for i in range(len(arr)):
        if (i & r == r) :
            temp += arr[i]
    return "1" if getParity(binToInteger(temp)) else "0"

def Hamming(message):
    print("Original message is: ", message)
    message=intToBinary(message)
    print("Message in binary is: ",message)
    m=len(message)
    r=calcRedundantBits(m)
    print("Number of redundant bits is: ",r)
    n=m+r
    arr=["0"]*n
    arrRedundantPos=arrRedundantPosition(r)
    counter=0
    for i in range(n):
        if i not in arrRedundantPos:
            counter= counter+1
            arr[i]=message[-counter]
    arr.insert(0,'START')
    for i in range(len(arrRedundantPos)):
        arrRedundantPos[i] = arrRedundantPos[i]+1
    for i in arrRedundantPos:
        arr[i]=getParitybit(arr,i)
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr.pop(-1)
    HammingArr=reverseArray(arr)
    print("The Hamming Code encoded message is: ",listToString(HammingArr))

def checkArrayRedundantBits(arr):
    n=len(arr)
    arr=[]
    for i in range(n):
        if 2**i < n:
            arr.append(2**i)
    return arr
#Encoding
n=int(input("Enter the number which you want to encode(in Decimals): "))
Hamming(n)


#Decoding
n=input("Enter the Encoded Message: ")
print("The Encoded Message is: ", n)
arr=['']*(len(n))
for i in range(len(n)):
    arr[i]=n[i]
arr=reverseArray(arr)
RedArr=checkArrayRedundantBits(arr)
arr.insert(0,'START')
ErrorPos=[]
for i in RedArr:
    ErrorPos.append(getParitybit(arr, i))
if binToInteger(listToString(reverseArray(ErrorPos)))==0:
    print("No Error Found")
    arr=DecodeProcessing(arr)
else:
    errordet=binToInteger(listToString(reverseArray(ErrorPos)))
    print("Error Found at ",errordet, " position from the left(Big Endian)")
    arr=DecodeProcessing(arr)
    if (arr[-(errordet)]=='1'):
        arr[-errordet]='0'
    else:
        arr[-errordet]='1'
    print("The Corrected Encoded Message is: ",listToString(arr))
CArrBin=[]
for i in range(len(RedArr)):
    RedArr[i]=-RedArr[i]
for i in range(len(arr)):
    if -(i+1) not in RedArr:
        CArrBin.append(arr[-(i+1)])
CArrBin=reverseArray(CArrBin)
print("The Decoded Message in binary is: ", listToString(CArrBin))
print("The Message Recieved is: ", binToInteger(listToString(CArrBin)))