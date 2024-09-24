from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title('billing slip')
root.geometry('1278x720')
bg_color="#2377fc"
#========================varaible==============#
c_name=StringVar()
c_phone=StringVar()
Item=StringVar()
Quantity=IntVar()
Rate=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))
global l
l=[]

#========================Function==================#

def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome BSC Retails")
    textarea.insert(END,f"\n\n Bill Number :\t\t{bill_no.get()}")
    textarea.insert(END,f"\n Customer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\n  Phone Number:\t\t{c_phone.get()}")
    textarea.insert(END,"\n======================================\n")
    textarea.insert(END,f"\n Product\t\t QTY\t\tPrice")
    textarea.insert(END,"\n======================================\n")
    textarea.config(font="arial 15 bold")

#====================add item=======================

def additm():
    n=Rate.get()
    m=Quantity.get()*n 
    l.append(m)
    if Item.get()=='':
        messagebox.showerror('Error','Please Enter the item')
    else:
        textarea.insert((10.0+float(len(l)-1)),f'{Item.get()}\t\t{Quantity.get()}\t\t{m}\n')



#====================gbill=======================#
def gbill():
    if c_name.get()==''or c_phone.get()=='':
        messagebox.showerror('Error','Customer Details are must')
    else:
        tex=textarea.get(10.0,(10.0+float(len(l))))

        welcome()
        textarea.insert(END,tex)
        textarea.insert(END,f"\n====================================\n")
        textarea.insert(END,f"Total Paybill Amount : \t\t\t{sum(l)}")
        textarea.insert(END,f"\n====================================\n")
        savebill()

def savebill():
    op=messagebox.askyesno('Save bill','Do you want to save the bill')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("bills/"+str(bill_no.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f'Bill no:{bill_no.get()} saved successfully')

    else:
        return
def clear():
    c_name.set('')
    c_phone.set('')
    Item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    op=messagebox.askyesno('Exit','Do you really want to exit')
    if op>0:
        root.destroy()
    

title=Label(root,text='Billing Software',bg=bg_color,fg="red",font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

F1=LabelFrame(root,text="Customer Details",font=('times new roman',18,'bold'),relief=GROOVE,bg=bg_color,fg='gold')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name ',font=('times new roman',18,'bold'),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)

cname_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)


cphn_lbl=Label(F1,text='Phone NO.',font=('times new roman',18,'bold'),bg=bg_color,fg='white')
cphn_lbl.grid(row=0,column=2,padx=10,pady=5)
cphn_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_phone)
cphn_txt.grid(row=0,column=3,padx=10,pady=5)


#=====================Product Details================#
F2=LabelFrame(root,text="Products Details",font=('times new roman',18,'bold'),relief=GROOVE,bg=bg_color,fg='gold')
F2.place(x=20,y=180,width=630,height=500)


item=Label(F2,text='Product Name',font=('times new roman',18,'bold'),bg=bg_color,fg='lightgreen')
item.grid(row=0,column=0,padx=30,pady=20)
itm_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)



rate=Label(F2,text='Product Rate',font=('times new roman',18,'bold'),bg=bg_color,fg='lightgreen')
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)



quantity=Label(F2,text='Product Quantity',font=('times new roman',18,'bold'),bg=bg_color,fg='lightgreen')
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)

#======================button========================#

btn1=Button(F2,text='Add item',font='arial 15 bold',padx=5,pady=10,bg='blue',width=15,command=additm)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text='Generate Bill item',font='arial 15 bold',padx=5,pady=10,bg='blue',width=15,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)


btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,bg='blue',width=15,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,bg='blue',width=15,command=exit)
btn4.grid(row=4,column=1,padx=10,pady=30)



#===================bill area ========#
F3=Frame(root,relief=GROOVE,bd=10,bg="#010f05")
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text="Bill Area",font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()

welcome()


root.mainloop()

