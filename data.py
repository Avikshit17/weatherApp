from tkinter import *
import request 
from PIL import Image,ImageTk

root=Tk()
root.geometry("700x450")
bg=ImageTk.PhotoImage(file="background.jpg")
canvas=Canvas(win,width=700,height=3500)
canvas.pack(fill=BOTH,expand=True)
canvas.create_image(0,0,image=bg,anchor='nw')


root.mainloop()