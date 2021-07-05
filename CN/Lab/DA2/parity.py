def getParity( n ): 
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return parity 

n=input("Enter the number: ")
n=int(n)
parity_bit=( "1" if getParity(n) else "0")
print ("Even Parity bit of number ", n," = ", parity_bit) 
bit=str("{0:b}".format(n))
bit=bit+str(parity_bit)
print("Encoded Message after appending parity bit: ", bit)

n=input("Enter the Encoded Message to check for Error: ")
n=str(n)
parity_bit=n[-1]
orig=""
for i in range(0,len(n)-1):
    orig=orig+n[i]
orig= int(orig,2)
chk=( "1" if getParity(orig) else "0")
if(chk==parity_bit):
    print("No Error")
else:
    print("Error Detected")