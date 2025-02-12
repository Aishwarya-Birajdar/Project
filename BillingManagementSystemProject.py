from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Billing Management System')
root.geometry('1280x720')
bg_color='#2D9290'

#======================Variable========================

Bread=IntVar()
Wine=IntVar()
Rice=IntVar()
Milk=IntVar()
total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()

#===============================Function=============

def calculate_total():
    if Bread.get()== 0 and Wine.get()== 0 and Rice.get()== 0 and Milk.get()== 0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        w=Wine.get()
        r=Rice.get()
        m=Milk.get()

        t=float(b*1.89+w*8.99+r*2.18+m*4.50)
        total.set(b+w+r+m)
        total_cost.set('$'+ str(round(t,2)))

        cb.set('$'+ str(round(b*1.89,2)))
        cw.set('$'+ str(round(w*8.99,2)))
        cr.set('$'+ str(round(r*2.18,2)))
        cm.set('$'+ str(round(m*4.50,2)))

def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items \tNumber of Items \tCost of Items')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t {cb.get()}')
    textarea.insert(END,f'\n\nWine\t\t{Wine.get()}\t {cw.get()}')
    textarea.insert(END,f'\n\nRice\t\t{Rice.get()}\t {cr.get()}')
    textarea.insert(END,f'\n\nMilk\t\t{Milk.get()}\t {cm.get()}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\n\nTotal Price\t\t{total.get()}\t {total_cost.get()}')
    textarea.insert(END,'\n================================')

def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')

def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Chocklet.set(0)
    Rice.set(0)
    Milk.set(0)
    total.set(0)

    cb.set('')
    cm.set('')
    cr.set('')
    cw.set('')
    total_cost.set('')
    
def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()



title=Label(root,text='Billing Management System',bg=bg_color,fg='white',font=('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#================================Product Details==================
F1=LabelFrame(root,text='Product Details',font=('times new romman',18,'bold'),fg='gold',bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=800,height=500)

#========================Heading====================
itm=Label(F1,text='Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='Cost of Items',font=('Helvetic',25,'bold','underline'),fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=20,pady=15)

#========================Product======================
bread=Label(F1,text='Bread',font=('times of rommon',20,'bold'),fg='lawngreen',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cb)
cb_txt.grid(row=1,column=2,padx=20,pady=15)


wine=Label(F1,text='Chocklet',font=('times of rommon',20,'bold'),fg='lawngreen',bg=bg_color)
wine.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Wine)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cw)
cw_txt.grid(row=2,column=2,padx=20,pady=15)


rice=Label(F1,text='Rice',font=('times of rommon',20,'bold'),fg='lawngreen',bg=bg_color)
rice.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Rice)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cr)
cr_txt.grid(row=3,column=2,padx=20,pady=15)


milk=Label(F1,text='Milk',font=('times of rommon',20,'bold'),fg='lawngreen',bg=bg_color)
milk.grid(row=4,column=0,padx=20,pady=15)
m_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Milk)
m_txt.grid(row=4,column=1,padx=20,pady=15)
cm_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cm)
cm_txt.grid(row=4,column=2,padx=20,pady=15)

Total=Label(F1,text='Total Price',font=('times of rommon',20,'bold'),fg='lawngreen',bg=bg_color)
Total.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
t_txt.grid(row=5,column=1,padx=20,pady=15)
ct_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
ct_txt.grid(row=5,column=2,padx=20,pady=15)


#========================Bill area========================

F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_tilte=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 ',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)


#=======================Button=============================

F3=Frame(root,relief=GROOVE,bd=10,bg=bg_color)
F3.place(x=5,y=590,width=1270,height=120)

btn1=Button(F3,text='Total',font='arial 25 bold',bg='yellow',fg='crimson',padx=4,pady=5,width=10,command=calculate_total)
btn1.grid(row=0,column=0,padx=10,pady=10)

btn2=Button(F3,text='Receipt',font='arial 25 bold',bg='yellow',fg='crimson',padx=4,pady=5,width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3=Button(F3,text='Print',font='arial 25 bold',bg='yellow',fg='crimson',padx=4,pady=5,width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4=Button(F3,text='Reset',font='arial 25 bold',bg='yellow',fg='crimson',padx=4,pady=5,width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5=Button(F3,text='Exit',font='arial 25 bold',bg='yellow',fg='crimson',padx=4,pady=5,width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)

root.mainloop()
