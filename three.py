from tkinter import*
from tkinter import messagebox

hub=Tk()
hub.geometry('500x500')
hub.title('gender verification')

def myfun():
    if(gender.get()==1):
        data=ppl1.cget("text")
        messagebox.showinfo("message",data)
    if (gender.get()==2):
        data=ppl2.cget('text')
        messagebox.showinfo('message',data)
    if (gender.get()==3):
        data=ppl3.cget('text')
        messagebox.showinfo('message','submitted successfully')



reed=Label(hub,text='GOVT OF INDIA',bg='black',fg='white',pady=30,font=('arial',30,'italic'))
reed.pack(fill=X)
gender=IntVar()
ppl1=Radiobutton(hub,text="male",variable=gender,value=1,font=("times",18,"bold"),state="active")
ppl1.pack()
ppl2=Radiobutton(hub,text='female',variable=gender,value=2,font=('times',18,'bold'),state='active')
ppl2.pack()
ppl3=Radiobutton(hub,text='others',variable=gender,value=3,font=('times',18,'bold'),state='active')
ppl3.pack()
sub=Button(hub,text='submit',bg='black',fg='white',width=20,pady=12,font=('times',15,'bold'),command=myfun)
sub.pack()



hub.mainloop()


'''kit=Tk()
kit.geometry('600x600')
kit.title('project x')


add0=Label(kit,text='GOVT OF INDIA',bg='grey',fg='white',pady='30',font=('times',40,'italic'))
add0.pack(fill=X)
gender=IntVar
add1=Radiobutton(kit,text='male',variable=gender,font=('times',18,'bold'))
add1.pack()
add2=Radiobutton(kit,text='female',variable=gender,font=('times',18,'bold'))
add2.pack()

kit.mainloop()'''