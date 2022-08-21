# from logging import root
from tkinter import*
from tkinter import font
from tkinter import messagebox
from turtle import bgcolor, title
from tkinter import messagebox
from pip import main

from setuptools import Command
import pymysql
from main import*
from registration import*

# Add your own database name and password here to reflect in the code
mypass ="Umang##20"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
usertable="user"
    
class login:
    def __init__(self,root):


        self.root=root
        self.root.title("login system")
        self.root.geometry("900x600+100+50")
        self.root.configure(bg="#A6F1DF")
        self.root.resizable(False,False)


        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("impact",30,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Account Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)


        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)


        regis_btn=Button(Frame_login,text="new registration",command=register,bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=300,y=500,width=180,height=40)


    

    def login_function(self):
        userid=self.txt_user.get()
        userpass=self.txt_pass.get()
        # print(type(userid))
        if userid=="" or userpass=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:

            extractBid = "select id,password from "+usertable
 
            cur.execute(extractBid)
            con.commit()
            c=0

            for i in cur:
    
                if(i[0]==userid and i[1]==userpass):
                    c=1
            # print("c",c)
            if(c==1 ):
                # messagebox.showinfo("Congrats","Login successfully")
                mainfunction()
               
                
            else:
                messagebox.showinfo("Error","Id or password is incoreect")

root=Tk()
obj=login(root)
root.mainloop()