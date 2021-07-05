import re
import numpy as np

def intToBinary(var):
    binary=bin(var).split("0b")[1]
    while(len(binary)<8):
        binary='0'+binary
    return binary

def intToBinary32(var):
    binary=bin(var).split("0b")[1]
    while(len(binary)<32):
        binary='0'+binary
    return binary

def binToInteger(var):
    return (int(var,2))

def display(temp):
    var=temp
    arr=[]
    for i in range(0,32,8):
        arr.append(binToInteger(var[i:i+8]))
    return arr

def IPv4Format(arr):
    ipv4=str(arr[0])
    for i in range(1,4,1):
        ipv4=ipv4+'.'+str(arr[i])
    return ipv4

def complement(var):
    temp=''
    for i in range(len(var)):
        if var[i]=='0':
            temp=temp+'1'
        else:
            temp=temp+'0'
    return temp

def binaryAND( var1, var2):
    ans=''
    for i in range(len(var1)):
        if var1[i]=='1' and var2[i]=='1':
            ans=ans+'1'
        else:
            ans=ans+'0'
    return ans

def binaryOR( var1, var2):
    ans=''
    for i in range(len(var1)):
        if var1[i]=='1' or var2[i]=='1':
            ans=ans+'1'
        else:
            ans=ans+'0'
    return ans

nsubnet = int(input("Enter number of subnets in the network: "))
subnet_requirements_arr =[]*nsubnet
for i in range (nsubnet):
    print("Enter number of customers in subnet ", i+1, end=" : ")
    ncustomers= int(input())
    print("Enter number of IP addresses required per customer ", end=" : ")
    nIPs= int(input())
    subnet_requirements_arr.append([ncustomers, nIPs])

start_IP=input("Enter starting IP address: ")
segments=re.split('\.|/', start_IP)
try:
    segments[4]
except IndexError:
    errmask=input("Please enter mask of the IP address provided in CIDR notation(IP/mask or /mask for just mask): ")
    segments.append(errmask.split('/')[-1])

binary_IP=''
for i in range(4):
    binary_IP=str(binary_IP)+str(intToBinary(int(segments[i])))
mask=''
for i in range (int(segments[4])):
    mask=mask+'1'
while len(mask)<32:
    mask=mask+'0'
init_mask=[]
for i in range(0,32,8):
    init_mask.append(binToInteger(mask[i:i+8]))
print("Mask: ",init_mask)
start_IP=intToBinary32(binToInteger(binary_IP)&binToInteger(mask))
init_start_IP=display(start_IP)
print("Start IP: ",init_start_IP)
first_address=''
for i in range(4):
    first_address=first_address+intToBinary(init_start_IP[i])
print(first_address)

for i in range(nsubnet):
    print("\n\n\nSubnet ",i+1,"\n")
    nums=range(0,33,1)
    portbits=np.log2(subnet_requirements_arr[i][1])
    if portbits not in nums:
        portbits=int(portbits)+1
    nmask=int(32-portbits)
    mask=''
    for k in range(nmask):
        mask=mask+'1'
    while len(mask)<32:
        mask=mask+'0'
    print("CUSTOMER\t\tSTARTING IP\t\tENDING IP")
    for j in range(subnet_requirements_arr[i][0]):
        print("Customer ", j+1,end='\t\t')
        print(IPv4Format(display(binaryAND(mask, first_address)))+'/'+str(nmask),end='\t\t')
        print(IPv4Format(display(binaryOR(complement(mask),first_address)))+'/'+str(nmask))
        first_address=intToBinary32(binToInteger(binaryOR(complement(mask),first_address))+1)