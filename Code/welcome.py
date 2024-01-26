from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from login import *
from PIL import ImageTk,Image
from tkinter import Label

class Welcome():
    def __init__(self,master):
        self.master = master
        #==============================VARIABLES======================================
        PRODUCT_ID = StringVar()
        PASSWORD = StringVar()
        res = StringVar()
        #==============================FRAMES=========================================

        Form = Frame(master, height=200)
        Form.pack(side=TOP, pady=10)
         
        lbl_id = Label(Form,fg="red", text = "House Price Prediction System", font=('arial', 20), bd=15)
        lbl_id.grid(row=0)
        label = Label(Form)
        label.grid(row=1)
        image = ImageTk.PhotoImage(Image.open("realestate.png"))
        label.config(image = image)
        label.image = image


        #==============================BUTTON WIDGETS=================================
        btn_login = Button(Form,bg="indigo",fg="white", text="Start Application", width=25, command=self.onLoginButtonClick)
        btn_login.grid(row=3,column=0,pady=50)

    def onLoginButtonClick(self):
        self.newWindow = Toplevel(self.master)
        self.app = LoginClass(self.newWindow)


mainFrame = Tk()
mainFrame.configure(background='mediumpurple')
w = mainFrame.winfo_screenwidth()
h = mainFrame.winfo_screenheight()
mainFrame.geometry("%dx%d+0+0" % (w, h))
mainFrame.resizable(0, 0)


mainFrame.title("Login Window")
cls = Welcome(mainFrame)

mainFrame.mainloop()
