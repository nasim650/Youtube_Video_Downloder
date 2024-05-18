from tkinter import *
from pytube import YouTube
from moviepy.editor import VideoFileClip

from main import y_tube

root = Tk()

root.title('Youtube Video Downloader')
root.geometry('450x550+400+50')
root.configure(bg='#cdc9c8')

root.resizable(False,False)
def download():
    v_link = link.get('1.0','end')

    #download
    Y_tube = YouTube(v_link)
    title = Y_tube.title
    root.title('downloading.....')
    stream = y_tube.streams.filter(progressive="True",res="720p")
    video = stream.first().download()
    clip = VideoFileClip(video)
    clip.close()


    pass

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
link.place(x=95,y=83)

#submit button
Button(frame,width=10,padx=1,pady=3,text='Download',bg='#57a1f8',fg='white',border=1,command=download,font=('Microsoft yahei UI Light',14,'bold')).place(x=140,y=200)


root.mainloop()



