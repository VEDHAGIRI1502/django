from tkinter import*

'''from tkinter import *
from tkinter import ttk
from pymysql import *
from tkinter import messagebox
mydb=connect(host="localhost",user="root",password='',database="frame")
cur=mydb.cursor()



winn=Tk()
winn.geometry('600x700')
winn.title('regg')
def f():
    qry="""insert into records(name,email)values('%s','%s')""" %\
        (e2.get(),e3.get())

    sasi=cur.execute(qry)
    mydb.commit()
    if sasi!=0:
        messagebox.showinfo("message","inserted")
    else:
        messagebox.showerror("error","record not inserted")
        
            
    

f1=Frame(winn,highlightthickness=20,highlightbackground='red')
f1.grid(padx=20,pady=20)
l1=Label(f1,text='registration',fg='brown',font=('times',20,'bold'))
l1.grid(row=0,columnspan=2)
l2=Label(f1,text='name',fg='black',font=('times',18,'bold'))
l2.grid(row=1,column=0)
e2=Entry(f1,font=('times',18,'bold'))
e2.grid(row=1,column=1)
l3=Label(f1,text='email',fg='black',font=('times',18,'bold'))
l3.grid(row=2,column=0)
e3=Entry(f1,font=('times',18,'bold'))
e3.grid(row=2,column=1)


cb=ttk.Combobox(f1,state='readonly')
cb['values']=('c','c+','python','java')
cb.grid(row=2,column=2)

bu=Button(f1,text='submit',fg='black',bg='white',font=('times',18,'bold'),command=f)
bu.grid(row=3,column=1)
winn.mainloop()
'''