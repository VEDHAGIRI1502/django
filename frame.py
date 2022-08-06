from tkinter import *

from numpy import pad


'''from tkinter import *
win=Tk()
win.geometry("2000x2000")
win.title("frame")


frame1=Frame(win,highlightbackground="black",highlightthicknes=2,padx=20,pady=20)
frame1.grid(row=0,column=0,padx=50,pady=50)


lab=Label(frame1,text="REGISTRATION",fg="green",font=("times",20,"bold"))
lab.grid(columnspan=2)


lab1=Label(frame1,text="Name",fg="black",font=("times",20,"bold"))
lab1.grid(row=1,column=0)
labentry=Entry(frame1,font=("times",20,"bold"))
labentry.grid(row=1,column=1)


labmail=Label(frame1,text="Email",fg="black",font=("times",20,"bold"))
labmail.grid(row=2,column=0)
labmail=Entry(frame1,font=("times",20,"bold"))
labmail.grid(row=2,column=1)


labadd=Label(frame1,text="Address",fg="black",font=("times",20,"bold"))
labadd.grid(row=3,column=0)
labentry=Entry(frame1,font=("times",20,"bold"))
labentry.grid(row=3,column=1)

subbtn=Button(frame1,text="SUBMIT",bg="green",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subbtn.grid(row=4,column=1 ,sticky=W)
subclr=Button(frame1,text="CLEAR",bg="red",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subclr.grid(row=4,column=1,sticky=E)

frame2=Frame(win,highlightbackground="black",highlightthicknes=2,width=100,padx=20,pady=20)
frame2.grid(row=0,column=1,padx=20,pady=50)
lab1=Label(frame2,text="LOGIN",fg="green",font=("times",20,"bold"))
lab1.grid(columnspan=2)


lab1=Label(frame2,text="Name",fg="black",font=("times",20,"bold"))
lab1.grid(row=1,column=0)
labentry=Entry(frame2,font=("times",20,"bold"))
labentry.grid(row=1,column=1)


labmail=Label(frame2,text="Email",fg="black",font=("times",20,"bold"))
labmail.grid(row=2,column=0)
labmail=Entry(frame2,font=("times",20,"bold"))
labmail.grid(row=2,column=1)


subbtn=Button(frame2,text="LOGIN",bg="green",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subbtn.grid(row=4,column=1 ,sticky=W)
subclr=Button(frame2,text="CLEAR",bg="red",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subclr.grid(row=4,column=1,sticky=E)

win.mainloop()'''

win=Tk()
win.geometry('500x500')
win.title('content')

frame1=Frame(win,highlightbackground="black",highlightthicknes=2)
frame1.grid(row=0,column=0)

labb=Label(frame1,text='registration',fg='red',font=('times',30,'italic'))
labb.grid(columnspan=2)

labb2=Label(frame1,text='Name',fg='black',font=('arial',18,'bold'))
labb2.grid(row=2,column=0,padx=30)
labbentry=Entry(frame1,font=('times',18,'bold'))
labbentry.grid(row=2,column=1,padx=20,pady=20)

labb3=Label(frame1,text='Email',fg='black',font=('times',18,'bold'))
labb3.grid(row=3,column=0)
labb3entry=Entry(frame1,font=('times',18,'bold'))
labb3entry.grid(row=3,column=1)

buu=Button(frame1,text='clear',bg='red',fg='black',padx=20,pady=2,font=('times',18,'bold'))
buu.grid(row=4,column=1,sticky=W)

buu2=Button(frame1,text='submit',bg='green',fg='black',font=('times',18,'bold'))
buu2.grid(row=4,column=1,sticky=E,pady=20,padx=20)


frame2=Frame(win,highlightbackground="black",highlightthicknes=2)
frame2.grid(row=0,column=5,padx=20,pady=20)
la=Label(frame2,text='login',fg='blue',font=('times',30,'italic'))
la.grid(columnspan=2)


labe1=Label(frame2,text='name',fg='black',font=('times',18,'bold'))
labe1.grid(row=1,column=0)
labe1en=Entry(frame2,font=('times',18,'bold'))
labe1en.grid(row=1,column=1,pady=20)

labe2=Label(frame2,text='passcode',fg='black',font=('times',18,'bold'))
labe2.grid(row=2,column=0)
labe2en=Entry(frame2,font=('times',18,'bold'))
labe2en.grid(row=2,column=1,padx=20)

bu1=Button(frame2,text='login',bg='black',fg='white',font=('times',18,'italic'))
bu1.grid(row=3,column=1,sticky=W,pady=20)

bu1=Button(frame2,text='cancel',bg='black',fg='white',font=('times',18,'italic'))
bu1.grid(row=3,column=1,sticky=E)

win.mainloop()





'''frame1=Frame(win,highlightbackground="black",highlightthicknes=2,padx=20,pady=20)
frame1.grid(row=0,column=0)

frame2=Frame(win,highlightbackground="black",highlightthicknes=2,padx=20,pady=20)
frame2.grid(row=0,column=1)'''