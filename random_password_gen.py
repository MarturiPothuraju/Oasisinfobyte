import tkinter as tk
import random
import pyperclip as ppc
global pass_word
def random_password_set(pass_len,cust_char,cust_int,cust_sym,cap_l):
    pass_lis=[]
    pass_len1=int(pass_len)
    i=0
    try:
        while i<pass_len1:
            a=None
            x=random.choices([1,2,3])[0]
            if (cap_l)and (i<pass_len1):
                a=random.choices(cap_l)
                pass_lis.append(a[0])
                cap_l.remove(a[0])
                i+=1
            match(x):
                case(1):
                    if (cust_char)and (i<pass_len1):
                        a=random.choices(cust_char)
                        pass_lis.append(a[0])
                        cust_char.remove(a[0])
                        i+=1
                case(2):
                    if (cust_int)and (i<pass_len1):
                        a=random.choices(cust_int)
                        pass_lis.append(a[0])
                        cust_int.remove(a[0])
                        i+=1
                case(3):
                    if (cust_sym)and (i<pass_len1):
                        a=random.choices(cust_sym)
                        pass_lis.append(a[0])
                        cust_sym.remove(a[0])
                        i+=1
            if (cap_l)and (i<pass_len1):
                a=random.choices(cap_l)
                pass_lis.append(a[0])
                cap_l.remove(a[0])
                i+=1
    except:
        pass_lis=["Some thing wrong entered"]
    return pass_lis

def random_password_as_user():
    pass_lent=pass_len.get()
    cust_char1=str_char(cust_char.get())
    cust_int1=str_char(cust_int.get())
    cust_sym1=str_char(cust_sym.get())
    if(check_num_char_sym(pass_lent,cust_char1,cust_int1,cust_sym1)):
        cap_l=[i for i in cust_char1 if (i==i.upper())]
        cust_char2=[i for i in cust_char1 if (i==i.lower())]
        pass_list=random_password_set(pass_lent,cust_char2,cust_int1,cust_sym1,cap_l)
        global pass_word
        pass_word=''
        if(int(pass_lent)<=len(pass_list)):
            for i in range(int(pass_lent)):
                pass_word+=pass_list[i]
            msg4=tk.Message(window,text='The password is: '+pass_word,font=20,padx=20,pady=100)
            msg4.grid(row=5,column=1)
        else:
            pass_word=None
            msg4=tk.Message(window,text='*Elements are less then the length of pass word',font=20,padx=20,pady=100)
            msg4.grid(row=5,column=1)
    else:
        msg4=tk.Message(window,text='\t\t\t\t\t\t\t\t',font=20,padx=20,pady=100)
        msg4.grid(row=5,column=1)
def str_char(str1):
    str2=[i for i in str1]
    return str2
def copy_clip():
    global pass_word
    if (pass_word):
        ppc.copy(pass_word)
def check_num_char_sym(pass_len,char1,int1,sym1):
    ret1=True
    ret2=True
    ret3=True
    ret=False
    for i in char1:
        
        if (i.isalpha()):
            ret1=True
        else:
            ret1=False
            break
        if (i== i.upper()):
            ret=(ret or True)
            
        else:
            ret=(ret or False)
    if (not(ret1)):
        msg1=tk.Message(window,text='*Enter only charectors without space',padx=1,pady=45)
        msg1.grid(row=1,column=3)
    elif(ret==True):
        msg1=tk.Message(window,text='\t\t\t\t',padx=2,pady=80)
        msg1.grid(row=1,column=3)
    else:
        msg1=tk.Message(window,text='*Enter atleast one capital letter\t',padx=2,pady=60)
        msg1.grid(row=1,column=3)
    if (pass_len.isnumeric()):
        msg6=tk.Message(window,text=' \t\t\t\t\t\t',padx=1,pady=45)
        msg6.grid(row=0,column=3)
        ret4=True
    else:
        ret4=False
        msg6=tk.Message(window,text='*Enter a valid number ',padx=1,pady=45)
        msg6.grid(row=0,column=3)
    for i in int1:
        if (i.isnumeric()):
            msg1=tk.Message(window,text='\t\t\t\t\t\t',padx=1,pady=45)
            msg1.grid(row=2,column=3)
            ret2=True
        else:
            ret2=False
            msg1=tk.Message(window,text='*Enter only numbers without space',padx=2,pady=50)
            msg1.grid(row=2,column=3)
            break
    for i in sym1:
        if (not(i.isalpha()or i.isnumeric())):
            msg1=tk.Message(window,text='\t\t\t\t\t\t',padx=2,pady=45)
            msg1.grid(row=3,column=3)
            ret3=True
        else:
            ret3=False
            msg1=tk.Message(window,text='*Enter only symbols without space',padx=2,pady=50)
            msg1.grid(row=3,column=3)
            break
    return (ret1 and ret2 and ret3 and ret and ret4)
"""______________________________________________________________________________"""
window=tk.Tk()
window.title('Radom password generator')
window.geometry('800x800')
msg1=tk.Message(window,text='Enter the number: ',padx=20,pady=25)
msg1.grid(row=0,column=0)
pass_len=tk.Entry(window)
pass_len.grid(row=0,column=1)
msg1=tk.Message(window,text='Enter the charectors: ',padx=20,pady=25)
msg1.grid(row=1,column=0)
cust_char=tk.Entry(window)
cust_char.grid(row=1,column=1)
msg2=tk.Message(window,text='Enter the numbers: ',padx=20,pady=25)
msg2.grid(row=2,column=0)
cust_int=tk.Entry(window)
cust_int.grid(row=2,column=1)
msg3=tk.Message(window,text='Enter the symbols: ',padx=20,pady=40)
msg3.grid(row=3,column=0)
cust_sym=tk.Entry(window)
cust_sym.grid(row=3,column=1)
button=tk.Button(window,text="Get password",command=random_password_as_user)
button.grid(row=4,column=0)
button1=tk.Button(window,text="Copy password",command=copy_clip)
button1.grid(row=4,column=1)
"""_______________________________________________________________________"""

window.mainloop()
