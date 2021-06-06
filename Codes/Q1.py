# 19BDS0042 SAMARTH GUPTA

def Rbits(data, r): 
    j = 0
    k = 1
    m = len(data) 
    res = ''
    for i in range(1, m + r+1): 
        if(i == 2**j): 
            res = res + '0'
            j += 1
        else: 
            res = res + data[-1 * k]
            k+=1
            
    return res[::-1]
def hamming(m): 
    for i in range(m): 
        if(2**i >= m + i + 1): 
            return i 
def Pbits(arr, r): 
    n = len(arr)
    l=[]
    z=[]
    for i in range(r): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        z.append(val)  
                  
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    l.append(z)
    l.append(arr)
    return l

def Error(arr, nr): 
    n = len(arr) 
    res = 0
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 
        res = res + val*(10**i) 
        return int(str(res), 2) 
print("Enter Message To Be Send = ")
data = input()
m = len(data) 
r = hamming(m) 
arr = Rbits(data, r)
p = Pbits(arr, r)
z=p[0]
arr=p[1]
print("Message To Be Send = ",data)
print("Length of Message Bit = ",m)
print("Generated Check Bit at Sender Side =  ",z)
print("length of The Check Bit = ",r)
print("Message Bits + Sender Check Bits = ",arr)
print("Length of Code Word = ",len(arr))
print("Enter the Recieved Message = ")
arr1=input()
arr5=arr1
r1 = hamming(m) 
arr1 = Rbits(arr1, r1)
p1 = Pbits(arr1, r1)
z1=p1[0]
arr1=p1[1]
print("Recieved Message (After Adding Check Bit) = ",arr1)
print("Receiver Side Check Bits = ",z1)
correction=Error(arr1,r1)
print("Postion of Error = ",correction,"th bit")
if(correction=='1'):
    print("No Errors")
else:
    if(arr1[correction]=='0'):
        arr1=arr1[:correction]+arr[correction:]
print("Corrected Code = ",arr1)
