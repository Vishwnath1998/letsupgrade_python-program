from pytube import YouTube
  
from tkinter import *

import os

root = Tk()
    
root.geometry("300x400")
root.title("you tube video download")
L1 = Label(root,text = "YouTube Video",fg="BLACK",font=("bold",20))
L1.place(x=200,y=70)

mylink=StringVar()


pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=200, y=120)
def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('E:/letsupgrade'):
        os.makedirs('E:/Letsupgrade')
    ytvideo.download('E:/Letsupgrade') 

Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=200, y=180)


root.mainloop()