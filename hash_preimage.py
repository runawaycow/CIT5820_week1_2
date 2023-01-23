import hashlib
import os
import string
import random

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    lenth = len(target_string) 
    itt = 2**(lenth+2)  
    target = int(target_string, 2)
    #print(target_string, target, lenth)
    #print('=================') 
    bits = 1 << lenth 
    letters = string.ascii_letters   
    for i in range(0, itt): 
      string_1 =  ''.join(random.choice(letters) for i in range(lenth+1) )
      hashcode_1 = hashlib.sha256(string_1.encode('utf-8')).hexdigest()
      test = int(bin(int(hashcode_1,16) & (bits - 1)),2)
      #print(test)
      if target == test:
        #print(string_1, test)
        #print(bin(int(hashcode_1,16)))
        return string_1

    nonce = b'\x00'

    return( nonce )
