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



root.mainloop()



