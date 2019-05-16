import os
import pas

def dbin(x):
    return int(bin(x)[2:])

def encrypt(path, password):

    pas.pas(path, password)
    f=open(path,'rb') 
    lines=f.readlines()
    path_e=path+'.crypto'
    e=open(path_e,'wb')
      
    char=[]
    for l in lines:
        for i in range(len(l)):
            char.append(ord(l[i]))
      
    #---encryption-----------
    for i in range(len(char)):
        if char[i]<253:
            char[i]+=3
        else:
            char[i]+=3
            char[i]-=256
    #----------------------
    for i in range(len(char)):
        e.write(chr(char[i]))
      
    e.close()
    f.close()
    os.remove(path)
    

def decrypt(path, password):
    name=path[:-7]
    char=[]
    f=open(path,'rb')
    d=open(name,'wb')

    lines=f.readlines()
    for l in lines:
        for i in range(len(l)):
            char.append(ord(l[i]))
      
    #---decryption------
    for i in range(len(char)):
        if char[i]>2:
            char[i]-=3
        else:
            char[i]=char[i]+253
        char[i]=chr(char[i])
    #-----------------
    d.writelines(char)

    f.close()
    d.close()
    os.remove(path)

