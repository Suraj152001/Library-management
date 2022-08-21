from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    id = userInfo1.get()
    name = userInfo2.get()
    gmail = userInfo3.get()
    password = userInfo4.get()
    
    insertUser = "insert into "+userTable+" values('"+id+"','"+name+"','"+gmail+"','"+password+"')"
    try:
        cur.execute(insertUser)
        con.commit()
        messagebox.showinfo('Success',"registered successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database or Id is already exists")
 

    root.destroy()
    
def register(): 
    
    global userInfo1,userInfo2,userInfo3,userInfo4,Canvas1,con,cur,userTable,root
    
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
    userTable = "user" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#CAD3D1")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=3)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Register Your account", bg='White', fg='black', font=('Time new Roman',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black',bd=3)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="User ID : ", bg='white', fg='black',font=('Time new Roman',10))
    lb1.place(relx=0.05,rely=0.2,relwidth=0.20, relheight=0.15)
        
    userInfo1 = Entry(labelFrame,font=('Time new Roman',10))
    userInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.15)
        
    # Title
    lb2 = Label(labelFrame,text="User name ", bg='white', fg='black',font=('Time new Roman',10))
    lb2.place(relx=0.05,rely=0.40,relwidth=0.20, relheight=0.15)
        
    userInfo2 = Entry(labelFrame,font=('Time new Roman',10))
    userInfo2.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.15)
        
    # Book Author
    lb3 = Label(labelFrame,text="gmail : ",bg='white', fg='black',font=('Time new Roman',10))
    lb3.place(relx=0.05,rely=0.60,relwidth=0.20, relheight=0.15)
        
    userInfo3 = Entry(labelFrame,font=('Time new Roman',10))
    userInfo3.place(relx=0.3,rely=0.60, relwidth=0.62, relheight=0.15)
        
    # Book Status
    lb4 = Label(labelFrame,text="password : ",bg='white', fg='black',font=('Time new Roman',10))
    lb4.place(relx=0.05,rely=0.8,relwidth=0.20, relheight=0.15)
        
    userInfo4 = Entry(labelFrame,font=('Time new Roman',10))
    userInfo4.place(relx=0.3,rely=0.8, relwidth=0.62, relheight=0.15)
        
    #Submit Button
    SubmitBtn = Button(root,text="Register",bg='green', fg='white',command=bookRegister,font=('Time new Roman',12))
    SubmitBtn.place(relx=0.28,rely=0.82, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Close",bg='red', fg='white', command=root.destroy,font=('Time new Roman',12))
    quitBtn.place(relx=0.53,rely=0.82, relwidth=0.18,relheight=0.08)
    
    root.mainloop()