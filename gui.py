from tkinter import *
from pytube import YouTube
from moviepy.editor import VideoFileClip
root = Tk()

root.title('Youtube Video Downloader')
root.geometry('450x550+400+50')
root.configure(bg='#cdc9c8')

root.resizable(False,False)

#for image
img = PhotoImage(file='logo.png')
Label(image =img,bd=1,bg='#cdc9c8').place(x=70,y=20)

#creating frame where we provide fields
frame = Frame(root,width=400,height=370,bg='#fff') #frame size,bg color
frame.place(x=25,y=170) #passing location

#passing text with in a frame
heading = Label(frame,text='Youtube Video Downloader',fg='#57a1f8',bg='#F8EBE7',font=('Microsoft yahei UI Light',22,'bold'))
heading.place(x=10,y=10)

Label(frame,text="Link :",fg='#019f90',bg='#F8EBE7',font=('Microsoft yahei UI Light',14,'bold')).place(x=10,y=80)

#taking link
link = Text(frame,fg='black',bd=1,height=1,width=30,bg="light yellow",font=('Microsoft yahei UI Light',13))
link.place(x=95,y=83 )

root.mainloop()



