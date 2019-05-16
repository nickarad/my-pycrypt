from Tkinter import *
import os
import method_3


class ADialog:
    
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="What do you want to do?").pack()
        
        b = Button(top, text="Encrypt a file", command=self.encrypt)
        b.pack(pady=5)
        c = Button(top, text="Decrypt a file", command=self.decrypt)
        c.pack(pady=5)

    def encrypt(self):

        self.option = 'encrypt'
        self.top.destroy()
        
    def decrypt(self):

        self.option = 'decrypt'
        self.top.destroy()
        

class ADialog_2:
    
    def __init__(self, parent):

        
        top = self.top = Toplevel(parent)

        Label(top, text="Enter the path of the file").pack()
        self.e = Entry(top)
        self.e.pack(padx=15)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        self.enable = 'False'
        while True:                             
            try:
                open(self.e.get())
                self.path = self.e.get()
                self.top.destroy()
                break
            except IOError:
                self.enable = 'True'
                self.top.destroy()
                break

            
class ADialog_2_error:
    
    def __init__(self, parent):

        
        top = self.top = Toplevel(parent)

        Label(top, text="Invalid path! Please enter a valid path.").pack()
        self.e = Entry(top)
        self.e.pack(padx=15)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        self.enable = 'False'
        while True:                             
            try:
                open(self.e.get())
                self.path = self.e.get()
                self.top.destroy()
                break
            except IOError:
                self.enable = 'True'
                self.top.destroy()
                break
            

class ADialog_3:
    
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        if dial.option=='encrypt':

            Label(top, text="Enter a protection password").pack()
            self.e = Entry(top)
            self.e.pack(padx=15)

            b = Button(top, text="OK", command=self.ok)
            b.pack(pady=5)
        
        else:
            
            Label(top, text="Enter the protection password").pack()
            self.e = Entry(top)
            self.e.pack(padx=15)
            
            path_list=[]
            for i in range(len(dial_2.path)):
                path_list.append(dial_2.path[i])
            path_list.reverse()
            del path_list[:(path_list.index('\\')+1)]
            path_list.reverse()
            self.path_2=''
            for i in path_list:
                self.path_2+=i
            self.file = open(self.path_2+'\\test.txt')
            contents=self.file.read()
            s=0
            pas=''
            for i in range(len(contents)):
                if contents[i]!='\\':
                    s=10*s+int(contents[i])
                elif contents[i]=='\\':
                    pas+=chr(s-10)
                    s=0

            self.pas=str(pas)

            self.file.close()

            b = Button(top, text="OK", command=self.check)
            b.pack(pady=5)

    def ok(self):

        self.enable = 'False'
        self.password = self.e.get() 
        self.top.destroy()

    def check(self):

        self.enable = 'False'
        if self.pas == self.e.get():
            self.password = self.e.get()
            os.remove(dial_3.path_2+'\\test.txt')
            self.top.destroy()
        else:
            self.enable = 'True'
            self.top.destroy()

class ADialog_3_error:
    
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Wrong password! Pleas enter the correct password").pack()
        self.e = Entry(top)
        self.e.pack(padx=15)
            
        path_list=[]
        for i in range(len(dial_2.path)):
            path_list.append(dial_2.path[i])
        path_list.reverse()
        del path_list[:(path_list.index('\\')+1)]
        path_list.reverse()
        self.path_2=''
        for i in path_list:
            self.path_2+=i
        self.file = open(self.path_2+'\\test.txt')
        contents=self.file.read()
        s=0
        pas=''
        for i in range(len(contents)):
            if contents[i]!='\\':
                s=10*s+int(contents[i])
            elif contents[i]=='\\':
                pas+=chr(s-10)
                s=0

        self.pas=str(pas)

        self.file.close()

        b = Button(top, text="OK", command=self.check)
        b.pack(pady=5)

    def check(self):

        self.enable = 'False'
        if self.pas == self.e.get():
            self.password = self.e.get()
            os.remove(dial_3.path_2+'\\test.txt')
            self.top.destroy()
        else:
            self.enable = 'True'
            self.top.destroy()



class ADialog_4:
    
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="You want to "+dial.option+' the file located in '+str(dial_2.path)).pack()
        pas=''
        for i in str(dial_3.password):
            pas+='x'
        Label(top, text="Got password "+pas).pack()
        Label(top, text="Ready to start?").pack()
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        
        if dial.option=='encrypt':
            method_3.encrypt(dial_2.path, dial_3.password)
        else:
            method_3.decrypt(dial_2.path, dial_3.password)
        
        self.top.destroy()


root = Tk()
root.wm_geometry("400x300+20+40")

message=StringVar()
message.set("Complete the form")
Label(root, textvariable=message).pack(padx=30)
root.update()

dial = ADialog(root)
root.wait_window(dial.top)

dial_2 = ADialog_2(root)
root.wait_window(dial_2.top)
#
#Untill the user inserts a valid path dial_2.enable will be True and class ADialog_2_error will be repeated again and again
#
while dial_2.enable == 'True':
    dial_2 = ADialog_2_error(root)
    root.wait_window(dial_2.top)
    
dial_3 = ADialog_3(root)
root.wait_window(dial_3.top)
#
#While decrypting untill the user inserts a valid password dial_3.enable will be True and class ADialog_3_error will be repeated again and again
#
while dial_3.enable == 'True':
    dial_3 = ADialog_3_error(root)
    root.wait_window(dial_3.top)

dial_4 = ADialog_4(root)
root.wait_window(dial_4.top)

message.set("File "+dial.option+'ed!')

Button(root, text="Done", command=root.destroy).pack()
root.update()


root.mainloop()



