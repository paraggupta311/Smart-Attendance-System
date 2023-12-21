from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recongnition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width="1380",height="45")


        #1st image
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1385,665),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1385,height=665)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=950,y=0,width=400,height=500)

        img_top1=Image.open(r"college_images\Parag.jpeg")
        img_top1=img_top1.resize((300,300),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=200,y=0,width=200,height=265)


        dev_lbl=Label(main_frame,text="Developer name is \n Parag  Gupta",font=("times new roman",18,"bold"),bg="white")
        dev_lbl.place(x=0,y=5)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()