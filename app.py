# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:55:19 2022

@author: Adithyan.A.S
"""
from tkinter import *
from tkinter import messagebox
from flask import Flask


x=Tk()
x.geometry('1000x400')
x.resizable(0,0)
jok=StringVar()
jokl=StringVar()
var1=IntVar()
var2=StringVar()
def xi(h):
    #codes
    code=["!","@","X","Y","Z","A","B","o","+","/","%","]",":",";","n","-","_","$","^","~","=","l",".","a","b","q"]
    code2=['😀', '😃', '😄', '😁', '😅', '😂', '🤣', '😇', '🙂', '🙃', '🙂', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤫', '🤥', '😶', '😐', '😑']
    code2[10]="😮"
    code3= ['🍏', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🫐', '🍈', '🍒', '🍑', '🥭'  , '🍍', '🥥', '🥝', '🍅', '🍆', '🥑', '🥦', '🥬', '🥒', '🌶', '️', '🫑', '🌽']
    code_secret=['😀', '😛', '😝', '🥺', '😢', '😭', '😜', '😄', '😠', '😤', '🤨', '😅', '😂', '😎', '🤯', '🥵', '🥶', '🥳', '😒', '😌', '😍', '🥰', '😚', '😋', '😩', '😫']
    if h==1:
        code1=code
    elif h==2:
        code1=code2
    elif h==3:
        code1=code3
    elif h==0:
        messagebox.showwarning("information",'Select the appropriate code number')
    return code1
def code_EE():
    alpha=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    code=["!","@","X","Y","Z","A","B","o","+","/","%","]",":",";","n","-","_","$","^","~","=","l",".","a","b","q"]
    code2=['😀', '😃', '😄', '😁', '😅', '😂', '🤣', '😇', '🙂', '🙃', '🙂', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤫', '🤥', '😶', '😐', '😑']
    code2[10]="😮"
    code_secret=['😀', '😛', '😝', '🥺', '😢', '😭', '😜', '😄', '😠', '😤', '🤨', '😅', '😂', '😎', '🤯', '🥵', '🥶', '🥳', '😒', '😌', '😍', '🥰', '😚', '😋', '😩', '😫']
    qq=""
    encode=jokl.get()
    encoded=encode.lower()
    for i in range(len(encoded)):
        if encoded[i] in alpha:
            a=alpha.index(encoded[i])
            import random
            xx=code.index(random.choice(code))
            yy=a-xx
            if xx==a:
                pass
            elif yy<0:
                xx+=yy
                yy=a-xx
                if yy!=0 and yy!=1:
                    aj=[1,2]
                    oli=random.choice(aj)
                    yy-=oli
                    xx+=oli
            zz=random.choice(code_secret)
            qq+=code[xx]
            qq+=code2[yy]
            qq+=zz
        else:
            qq+=encoded[i]*3
    try:
        import pyperclip as pwd
        pwd.copy(qq)
    except:
        pass
    var2.set("")
    e2.insert(0,qq)
    return qq
def code_DD():
    alpha=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    code=["!","@","X","Y","Z","A","B","o","+","/","%","]",":",";","n","-","_","$","^","~","=","l",".","a","b","q"]
    code2=['😀', '😃', '😄', '😁', '😅', '😂', '🤣', '😇', '🙂', '🙃', '🙂', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤫', '🤥', '😶', '😐', '😑']
    code2[10]="😮"
    code_secret=['😀', '😛', '😝', '🥺', '😢', '😭', '😜', '😄', '😠', '😤', '🤨', '😅', '😂', '😎', '🤯', '🥵', '🥶', '🥳', '😒', '😌', '😍', '🥰', '😚', '😋', '😩', '😫']
    y=jokl.get()
    vav=""
    lst=[]
    for i in range(0,len(y),3):
        vav+=y[i]+y[i+1]+y[i+2]
        if len(vav)==3:
            lst.append(vav)
            vav=""
    ola=""
    for j in lst:
        
        if j[0] in code and j[1] in code2 and j[2] in code_secret:
            ww=code.index(j[0])
            kk=code2.index(j[1])
            ss=ww+kk
            ola+=alpha[ss]
        else:
            ola+=j[0]
    try:
        import pyperclip as pwd
        pwd.copy(ola)
    except:
        pass
    var2.set('')
    e2.insert(0,ola)
def code_e():
    j=jok.get()
    x=var1.get()
    if j=='CoDe' and x!=4:
        pass
    elif j=='CoDe@2' and x==4:
        code_EE()
        raise
    else:
        messagebox.showwarning("information","Incorrect Password")
        jok.set("")
        jokl.set("")
        var1.set(0)
        var2.set('')
        raise Exception('Invalid password')
    alpha=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    y=jokl.get()
    var2.set("")
    code=xi(x)
    qq=''
    encoded=y
    encode=encoded.lower()
    for j in range(len(encode)):
        if encode[j] in alpha:
            z=alpha.index(encode[j])
            qq+=code[z]
        else:
            qq+=encode[j]
    try:
        import pyperclip as psw
        psw.copy(qq)
    except:
        pass
    e2.insert(0,f'{qq}')
    return qq
def code_d():
    j=jok.get()
    x=var1.get()
    if j=='CoDe' and x!=4:
        pass
    elif j=='CoDe@2' and x==4:
        code_DD()
        return
    else:
        messagebox.showwarning("information","Incorrect Password")
    jok.set("")
    jokl.set("")
    var1.set(0)
    var2.set('')
    return
    y=jokl.get()
    var2.set("")
    alpha=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    code=xi(x)
    qw=''
    decode=y
    for j in range(len(decode)):
        if decode[j] in code :
            zz=code.index(decode[j])
            qw+=alpha[zz]
        else:
            qw+=decode[j]
    e2.insert(0,f'{qw}')
    return qw
x.title('Confidential Chat')
a1=Label(x,text='WELCOME',font='Algerian 20 bold')
b1=Label(x,text='Password:',font='arial 15 bold')
b2=Entry(x,textvariable=jok,show='*',font='arial 15')
c1=Label(x,text='Code Number:',font='arial 15 bold')
c2=Checkbutton(x, text = "code_1(Symbols)",font='arial 10 bold', variable = var1, \
                onvalue = 1, offvalue = 0, height=5, \
                width = 20)
c3=Checkbutton(x, text = "code_2(Emojis)",font='arial 10 bold',variable = var1, \
                onvalue = 2, offvalue = 0, height=5, \
                width = 20)
c4=Checkbutton(x, text = "code_3(Fruits)",font='arial 10 bold', variable = var1, \
                onvalue = 3, offvalue = 0, height=5, \
                width = 20)
c5=Checkbutton(x, text = "code_4(Complicated)",font='arial 10 bold', variable = var1, \
                onvalue = 4, offvalue = 0, height=5, \
                width = 20)
d1=Label(x,text='Enter the Text:',font='arial 15 bold')
d2=Entry(x,textvariable=jokl,font='arial 15')
e1=Label(x,text='Output:',font='arial 15 bold')
e2=Entry(x,textvariable=var2,font='arial 15')
f1=Button(text="Encode",command=code_e,height=3,width=10,bg='yellow')
f2=Button(text='Decode',command=code_d,height=3,width=10,bg='green')
a1.grid(row=1,column=3,sticky=W,pady=2)
b1.grid(row=2,column=0,sticky=W,pady=2)
b2.grid(row=2,column=1,sticky=W,pady=2)
c1.grid(row=3,column=0,sticky=W,pady=2)
c2.grid(row=3,column=1,sticky=W,pady=2)
c3.grid(row=3,column=2,sticky=W,pady=2)
c4.grid(row=3,column=3,sticky=W,pady=2)
c5.grid(row=3,column=4,sticky=W,pady=2)
d1.grid(row=4,column=0,sticky=W,pady=2)
d2.grid(row=4,column=1,sticky=W,pady=2)
e1.grid(row=5,column=0,sticky=W,pady=2)
e2.grid(row=5,column=1,sticky=W,pady=2)
f1.place(x=410,y=300)
f2.place(x=480,y=300)
x.mainloop()
