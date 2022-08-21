from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# from registration import*
# Add your own database name and password here to reflect in the code
mypass = "Umang##20"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def mainfunction():
    root = Tk()
    root.title("Open Library")
    root.minsize(width=400,height=400)
    root.geometry("1500x700")
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to Open Library", bg='white', fg='black', font=('time new roman',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    root.mainloop()
