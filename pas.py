import os
import shutil

def pas(path, password):

    base_file = open('test.txt', 'w')
    chars=[]
    for i in password:
        chars.append(i)
    enc_chars=[]
    for i in chars:
        enc_chars.append(ord(i))
    for i in range(len(enc_chars)):
        if enc_chars[i]<246:
            enc_chars[i]+=10
        else:
            enc_chars[i]-=246
    for i in enc_chars:
        base_file.write(str(i)+'\\')

    base_file.close()
    
    path_list=[]
    for i in range(len(path)):
        path_list.append(path[i])
    path_list.reverse()
    del path_list[:(path_list.index('\\')+1)]
    path_list.reverse()
    path=''
    for i in path_list:
        path+=i

    src = os.getcwd()+'\\test.txt'
    dst = path
    shutil.move(src, dst)

