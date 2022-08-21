from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database or Id is already exists")


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Open Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Umang##20"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#CAD3D1")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=3)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='White', fg='black', font=('Time new Roman',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black',bd=3)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='white', fg='black',font=('Time new Roman',10))
    lb1.place(relx=0.05,rely=0.2, relheight=0.15)
        
    bookInfo1 = Entry(labelFrame,font=('Time new Roman',10))
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.15)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='white', fg='black',font=('Time new Roman',10))
    lb2.place(relx=0.05,rely=0.40, relheight=0.15)
        
    bookInfo2 = Entry(labelFrame,font=('Time new Roman',10))
    bookInfo2.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.15)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ",bg='white', fg='black',font=('Time new Roman',10))
    lb3.place(relx=0.05,rely=0.60, relheight=0.15)
        
    bookInfo3 = Entry(labelFrame,font=('Time new Roman',10))
    bookInfo3.place(relx=0.3,rely=0.60, relwidth=0.62, relheight=0.15)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ",bg='white', fg='black',font=('Time new Roman',10))
    lb4.place(relx=0.045,rely=0.8, relheight=0.15)
        
    bookInfo4 = Entry(labelFrame,font=('Time new Roman',10))
    bookInfo4.place(relx=0.3,rely=0.8, relwidth=0.62, relheight=0.15)
        
    #Submit Button
    SubmitBtn = Button(root,text="ADD",bg='green', fg='white',command=bookRegister,font=('Time new Roman',12))
    SubmitBtn.place(relx=0.28,rely=0.82, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="CLOSE",bg='red', fg='white', command=root.destroy,font=('Time new Roman',12))
    quitBtn.place(relx=0.53,rely=0.82, relwidth=0.18,relheight=0.08)
    
    root.mainloop()