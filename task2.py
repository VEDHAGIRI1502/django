from cgitb import text
from msilib.schema import ComboBox
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
from turtle import width
from pymysql import *


con=connect(user='root',host='localhost',password="",database='hotel')
cur=con.cursor()

class hotel(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('600x600')
        self.title('hotel')
        self.ord=Label(text='Orders',fg='red',font=('arial',25,ITALIC,BOLD))
        self.ord.grid(row=0,column=0,sticky=W,pady=20)
        self.r1=Label(text='no of tables to book',fg='black',font=('times',18,BOLD))
        self.r1.grid(row=1,column=0,sticky=W,pady=10)
        self.rr1=Entry(fg='black',font=('times',18))
        self.rr1.grid(row=1,column=1,pady=10)
        self.r2=Label(text="type of meal(veg or non-veg)",fg='black',font=('times',18,BOLD))
        self.r2.grid(row=2,column=0,sticky=W,pady=10)
        self.rr2=Entry(fg='black',font=('times',18))
        self.rr2.grid(row=2,column=1,pady=10)
        self.r3=Label(text='items to order',fg='black',font=('times',18,BOLD))
        self.r3.grid(row=3,column=0,sticky=W,pady=10)
        self.rr3=Entry(fg='black',font=('times',18))
        self.rr3.grid(row=3,column=1,pady=10)
        self.r4=Label(text='snacks(if required)',fg='black',font=('times',18,BOLD))
        self.r4.grid(row=4,column=0,sticky=W,pady=10)
        self.rr4=Entry(fg='black',font=('times',18))
        self.rr4.grid(row=4,column=1,pady=10)
        self.b1=Button(text='Enter',bg='white',fg='black',font=('times',18,BOLD),command=self.ins)
        self.b1.grid(row=5,column=1,sticky=W,pady=10)
        self.b2=Button(text='Clear',bg='white',fg='black',font=('times',18,BOLD))
        self.b2.grid(row=5,column=1,sticky=E,pady=10)
        self.co=Label(text='rating',fg='black',font=('times',18,BOLD))
        self.co.grid(row=1,column=3,padx=10)
        self.coo=ttk.Combobox(state='read only',width=50)
        self.coo['values']=('Excellent','Good','Average','Bad')
        self.coo.grid(row=1,column=4)
        self.bu2=Button(text='Enter',bg='white',font=('times',18,BOLD))
        self.bu2.grid(row=2,column=4,sticky=E) 
        self.b3=Button(text='update',bg='white',fg='black',font=('times',18,BOLD),command=self.upd)
        self.b3.grid(row=6,column=1,sticky=W)

    def ins(self):
        qry='''insert into orders(no_of_tabels,type_of_meal,items_to_order,snacks) values(%d,'%s','%s','%s')''' % \
            (int(self.rr1.get()),self.rr2.get(),self.rr3.get(),self.rr4.get())
        ack=cur.execute(qry)
        con.autocommit(True)
        print(cur.rowcount,'data added')
        if ack!=0:
            messagebox.showinfo('message','booked successfully')
        else:
            messagebox.showerror('message',"coudn't booked")
    def upd(self):
        qry1="""update orders set no_of_tabels=%d,snacks='%s',items_to_order='%s' where type_of_meal='%s'"""\
            %(int(self.rr1.get()),self.rr4.get(),self.rr3.get(),self.rr2.get())
        aaz=cur.execute(qry1)
        con.autocommit(True)
        print(cur.rowcount,'updated')
        if aaz!=0:
            messagebox.showinfo('message','updated')
        else:
            messagebox.showerror('message','not updated')

        
h=hotel()
h.mainloop()
