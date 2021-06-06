# 19BDS0042 SAMARTH GUPTA

def division(divident, generator_polynomial): 
    z = len(generator_polynomial) 
    tmp = divident[0 : z] 
    while z < len(divident): 
        if tmp[0] == '1': 
            tmp = append(generator_polynomial, tmp) + divident[z] 
        else: 
            tmp = append('0'*z, tmp) + divident[z]  
        z += 1
    if tmp[0] == '1': 
        tmp = append(generator_polynomial, tmp) 
    else: 
        tmp = append('0'*z, tmp) 
    crc_checkword = tmp 
    return crc_checkword 
def generator_polynomial(div):
     d={}
     d['x']=10
     return eval(div,d)
def append(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
def code_append(word, key): 
    length = len(key) 
    final_append = word + '0'*(length-1) 
    print("")
    print("FINAL APPENDING RESULT :",final_append)
    remainder = division(final_append, key) 
    crc_codeword = word + remainder
    return crc_codeword   
def receiver_side(word,key):
    length=len(key) 
    final_append=word+'0'*(length-1)
    remainder=division(final_append,key)
    return remainder
Bit_Stream = str(input("ENTER BIT STREAM : "))
div=input("ENTER GENERATOR POLYNOMIAL (DIVISOR) (ENTER IN POLYNOMIAL FORM) :");
key =str(generator_polynomial(div));
bit_receiver = code_append(Bit_Stream,key) 
print("")
print("BIT STREAM TRANSMITTED :" + bit_receiver)
Bit_Recieved = str(input("ENTER MESSAGE BIT RECIEVED BY RECIEVER  : "))
final= receiver_side(Bit_Recieved,key)
if(int(final)==0):
    print("")
    print("THE REMAINDER IS 0 AND HENCE ,THERE IS NO ERROR IN DATA TRANSMITTED.")
else:
    print("")
    print("THERE IS ERROR DURING TRANSMISSION BECAUSE REMAINDER = " + str(final))

