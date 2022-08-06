
from tkinter import*
from tkinter import messagebox

win=Tk()
win.geometry('500x500')
win.title('PROJECT X')

def myfun():
    if (gender.get()==1):
        data=malebutton.cget('text')
        messagebox.showinfo('message',data)
    if (gender.get()==2):
        data=femalebutton.cget('text')
        messagebox.showinfo('message',data)
    if (gender.get()==3):
        data=Transgender.cget('text')
        messagebox.showinfo('message','submitted successfully')

vedha=Label(win,text='verification',bg='grey',fg='white',padx=20,pady=30,font=('times',25,'bold'))
vedha.pack(fill=X)
gender=IntVar()
malebutton=Radiobutton(win,text='Male',variable=gender,value=1,font=('times',15,'bold'),state='active')
malebutton.pack()
femalebutton=Radiobutton(win,text='Female',variable=gender,value=2,font=('times',15,'bold'),state='active')
femalebutton.pack()
Transgender=Radiobutton(win,text='Transgender',variable=gender,value=3,font=('times',15,'bold'),state='active')
Transgender.pack()
sub=Button(win,text='Submit',bg='grey',fg='black',padx=40,pady=7,font=('times',16,'bold'),command=myfun)
sub.pack()

win.mainloop()

