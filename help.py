from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recongnition system")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width="1380",height="45")


        #1st image
        img_top=Image.open(r"college_images\help.jpeg")
        img_top=img_top.resize((1385,665),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1385,height=665)


        dev_lbl=Label(f_lbl,text="Email:gupta.parag6@gmail.com",font=("times new roman",18,"bold"),bg="white")
        dev_lbl.place(x=500,y=250)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()