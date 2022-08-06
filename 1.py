from tkinter import *
from tkinter.font import BOLD, ITALIC
from pymysql import *
from tkinter import messagebox

con=connect(user='root',host='localhost',password='',database='vehicle')
cur=con.cursor()

class veh(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('500x600')
        self.title('Registration')
        self.vehi=Label(text='VEHICLE',fg='black',font=('times',28,BOLD))
        self.vehi.grid(row=0,column=0,sticky=W,pady=10)
        self.c1=Label(text='reg no',fg='grey',font=('times',18,BOLD))
        self.c1.grid(row=1,column=0,sticky=W)
        self.c11=Entry(fg='black',font=('times',18,ITALIC))
        self.c11.grid(row=1,column=1)
        self.c2=Label(text='vehicle number',fg='grey',font=('times',18,BOLD))
        self.c2.grid(row=2,column=0,sticky=W)
        self.c22=Entry(fg='black',font=('times',18,ITALIC))
        self.c22.grid(row=2,column=1)
        self.c3=Label(text='entry date',fg='grey',font=('times',18,BOLD))
        self.c3.grid(row=3,column=0,sticky=W)
        self.c33=Entry(fg='black',font=('times',18,ITALIC))
        self.c33.grid(row=3,column=1)
        self.c4=Label(text="owner's name",fg='grey',font=('times',18,BOLD))
        self.c4.grid(row=4,column=0,sticky=W)
        self.c44=Entry(fg='black',font=('times',18,ITALIC))
        self.c44.grid(row=4,column=1)
        self.c5=Label(text='contact number',fg='grey',font=('times',18,BOLD))
        self.c5.grid(row=5,column=0,sticky=W)
        self.c55=Entry(fg='black',font=('times',18,ITALIC))
        self.c55.grid(row=5,column=1)
        self.c6=Label(text='vehicle issue',fg='grey',font=('times',18,BOLD))
        self.c6.grid(row=6,column=0,sticky=W)
        self.c66=Entry(fg='black',font=('times',18,ITALIC))
        self.c66.grid(row=6,column=1)
        self.c7=Label(text='delivery date',fg='grey',font=('times',18,BOLD))
        self.c7.grid(row=7,column=0,sticky=W)
        self.c77=Entry(fg='black',font=('times',18,ITALIC))
        self.c77.grid(row=7,column=1)
        self.c8=Label(text='charge',fg='grey',font=('times',18,BOLD))
        self.c8.grid(row=8,column=0,sticky=W)
        self.c88=Entry(fg='black',font=('times',18,ITALIC))
        self.c88.grid(row=8,column=1)
        self.b1=Button(text='ADD',fg='black',bg='grey',font=('times',14,BOLD),command=self.ins)
        self.b1.grid(row=9,column=1,sticky=E)
        self.b1=Button(text='VIEW ALL',fg='black',bg='grey',font=('times',14,BOLD))
        self.b1.grid(row=9,column=2,sticky=E)
        self.b1=Button(text='VIEW ONE',fg='black',bg='grey',font=('times',14,BOLD))
        self.b1.grid(row=9,column=3)
        self.b1=Button(text='UPDATE',fg='black',bg='grey',font=('times',14,BOLD),command=self.upd)
        self.b1.grid(row=9,column=4)
        self.b1=Button(text='DELETE',fg='black',bg='grey',font=('times',14,BOLD),command=self.dele)
        self.b1.grid(row=9,column=5)
        self.b1=Button(text='CLEAR',fg='black',bg='grey',font=('times',14,BOLD),command=self.clear)
        self.b1.grid(row=9,column=6)

    def ins(self):
        qry="""insert into reg(reg_no,vehicle_number,entry_date,owners_name,contact_number,vehicle_issue,delivery_date,charge) values(%d,'%s','%s','%s',%d,'%s','%s',%f)""" % \
            (int(self.c11.get()),self.c22.get(),self.c33.get(),self.c44.get(),int(self.c55.get()),self.c66.get(),self.c77.get(),float(self.c88.get()))
            
        ack=cur.execute(qry)
        con.autocommit(True)
        print(cur.rowcount,'record(s) added')
        if ack !=0:
            messagebox.showinfo('ack','added successfully')

        else:
            messagebox.showerror('ack','error')

    def upd(self):
        qry1=""" update reg set vehicle_number='%s',entry_date='%s',owners_name='%s',contact_number=%d,vehicle_issue='%s',delivery_date='%s',charge=%f where reg_no =%d """ %\
            (self.c22.get(),self.c33.get(),self.c44.get(),int(self.c55.get()),self.c66.get(),self.c77.get(),float(self.c88.get()),int(self.c11.get()))
        acc=cur.execute(qry1)
        con.autocommit(True)
        print(cur.rowcount,'updated')
        if acc!=0:
            messagebox.showinfo('message','updated')
        else:
            messagebox.showerror('message','not updated')
        
    def dele(self):
        qry='delete from reg where '+self.c11.get()
        ackk=cur.execute(qry)
        con.autocommit(True)
        if ackk!=0:
            messagebox.showinfo('message','deleted')
        else:
            messagebox.showerror('message','not deleted')

    


    def clear(self):
        self.c11.delete(0,'end')
        self.c22.delete(0,'end')
        self.c33.delete(0,'end')
        self.c44.delete(0,'end')
        self.c55.delete(0,'end')
        self.c66.delete(0,'end')
        self.c77.delete(0,'end')
        self.c88.delete(0,'end')
        print('cleared')
    
v=veh()
v.mainloop()