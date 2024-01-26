from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui import *

class LoginClass():
    def __init__(self , master):
        self.master = master
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        master.configure(background='mediumpurple')
        master.geometry("%dx%d+0+0" % (w, h))
        #==============================VARIABLES======================================
        PRODUCT_ID = StringVar()
        PASSWORD = StringVar()
        res = StringVar()
        #==============================FRAMES=========================================

        Form = Frame(master, height=200)
        Form.pack(side=TOP, pady=10)
        
        lbl_id = Label(Form,fg="red", text = "Login Window", font=('arial', 20), bd=15)
        lbl_id.grid(row=0)

        lbl_id = Label(Form, text = "Enter User Name :", font=('arial', 14), bd=15)
        lbl_id.grid(row=1)

        lbl_res = Label(Form, textvariable=res,text = "start", font=('arial', 14), bd=15)
        lbl_res.grid(pady=20, row=2, columnspan=2)
        lbl_password = Label(Form, text = "Enter Password:", font=('arial', 14), bd=15)
        lbl_password.grid(row=2)
        lbl_text = Label(Form)
        lbl_text.grid(row=3, columnspan=2)

        #==============================ENTRY WIDGETS==================================
        self.input_id = Entry(Form, textvariable=PRODUCT_ID, font=('arial', 14))
        self.input_id.grid(row=1, column=1,padx=20)
        self.password = Entry(Form, textvariable=PASSWORD, show="*", font=('arial', 14))
        self.password.grid(row=2, column=1)

        #==============================BUTTON WIDGETS=================================
        btn_login = Button(Form,bg="indigo",fg="white", text="Login", width=25, command=self.Login)
        btn_login.grid(row=3,column=0,pady=40)
        btn_clear = Button(Form,bg="indigo",fg="white", text="Reset", width=25, command=self.Reset)
        btn_clear.grid(row=3, column=1,pady=40)
 
    #Fucntion to clear text
    def Reset(self):
        self.input_id.delete(0,END)
        self.input_id.insert(0,'')
        self.password.delete(0,END)
        self.password.insert(0,'')
     
    #Fucntion to check Login 
    def Login(self):
        if self.password.get()=='' or self.input_id.get()=='':
            messagebox.showinfo('', 'All Fields Mandatory')
        elif self.password.get()=='p' and self.input_id.get()=='p':
                messagebox.showinfo('Response', 'Login Successful')
                self.newWindow = Toplevel(self.master)
                self.app = RealEstate(self.newWindow)
                
        else: 
            messagebox.showinfo('Response', 'Invalid Credentials')

