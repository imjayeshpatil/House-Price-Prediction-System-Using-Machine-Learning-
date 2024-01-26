from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import Label



class AreaHighlight():
    def __init__(self , master,areaName):
        self.master = master
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        master.configure(background='mediumpurple')
        master.geometry("%dx%d+0+0" % (w, h))
        
        
        #==============================FRAMES=========================================

        Form = Frame(master, height=200)
        Form.pack(side=TOP, pady=10)      
        
        
        
        print(areaName)
        if areaName=='agra road':
           lbl_area = Label(Form,fg="red", text = "Agra Road Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)
        elif areaName=='sakri road':
           lbl_area = Label(Form,fg="red", text = "Sakri Road Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)
        elif areaName=='wadibhokar road':
           lbl_area = Label(Form,fg="red", text = "Wadibhokar Road Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)
        elif areaName=='agrawal nagar':
           lbl_area = Label(Form,fg="red", text = "Agrawal Nagar Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)  
        elif areaName=='near stadium':
           lbl_area = Label(Form,fg="red", text = "Near Stadium Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)
        elif areaName=='jaihind colny':
           lbl_area = Label(Form,fg="red", text = "Jaihind Colony Area Highlights", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)
        else:
           lbl_area = Label(Form,fg="red", text = "No data found", font=('arial', 14), bd=15)
           lbl_area.grid(row=0)           
        
        label = Label(Form)
        label.grid(row=1)
        image = ImageTk.PhotoImage(Image.open("bus_stand_icon.png"))
        label.config(image = image)
        label.image = image
        
        if areaName=='agra road':
           lbl_distance_bus_stand = Label(Form,fg="lightcoral", text = "Bus Stand 1.3 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)           
        elif areaName=='sakri road':
           lbl_distance_bus_stand = Label(Form,fg="red", text = "Bus Stand 2.1 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)
        elif areaName=='wadibhokar road':
           lbl_distance_bus_stand = Label(Form,fg="red", text = "Bus Stand 3.0 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)
        elif areaName=='agrawal nagar':
           lbl_distance_bus_stand = Label(Form,fg="red", text = "Bus Stand 2.8 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)  
        elif areaName=='near stadium':
           lbl_distance_bus_stand = Label(Form,fg="red", text = "Bus Stand 3.7 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)
        elif areaName=='jaihind colny':
           lbl_distance_bus_stand = Label(Form,fg="red", text = "Bus Stand 1.9 KM", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)
        else:
           lbl_distance_bus_stand = Label(Form,fg="red", text = "No data found", font=('arial', 14), bd=15)
           lbl_distance_bus_stand.grid(row=3)
           
        label_railway_icon = Label(Form)
        label_railway_icon.grid(row=4)
        image = ImageTk.PhotoImage(Image.open("railway_station_icon.png"))
        label_railway_icon.config(image = image)
        label_railway_icon.image = image 

        if areaName=='agra road':           
           lbl_distance_railway_station = Label(Form,fg="lightcoral", text = "Railway Station 2.5 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)
        elif areaName=='sakri road':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Railway Station 3.4 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)
        elif areaName=='wadibhokar road':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Railway Station 4.2 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)
        elif areaName=='agrawal nagar':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Railway Station 1.3 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)  
        elif areaName=='near stadium':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Railway Station 4.9 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)
        elif areaName=='jaihind colny':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Railway Station 3.1 KM", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)
        else:
           lbl_distance_railway_station = Label(Form,fg="red", text = "No data found", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=5)        

        label_hospital_icon = Label(Form)
        label_hospital_icon.grid(row=6)
        image = ImageTk.PhotoImage(Image.open("hospital_icon.png"))
        label_hospital_icon.config(image = image)
        label_hospital_icon.image = image
        
        if areaName=='agra road':           
           lbl_hospital = Label(Form,fg="lightcoral", text = "Maher Hospital, Tuljai hospital, Manjushree hospital, Shree samarth Hospital", font=('arial', 14), bd=15)
           lbl_hospital.grid(row=7)
        elif areaName=='sakri road':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Siddhivinay Hospital, Sai Hospital, Shegdane Hospital, District Hospital", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)
        elif areaName=='wadibhokar road':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Jamnaabai Hospital, Spandan Hospital, Chudaman Patil Hospital, okar Hospital", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)
        elif areaName=='agrawal nagar':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Shaha Hospital, Bhatwal Hospital, Sharada Hospital, Yash Kidney care Hospial", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)  
        elif areaName=='near stadium':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Bipin Hospital, Shidhakal Hospital, Siddhivinayak Hospital, Morya Surgical Hospital", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)
        elif areaName=='jaihind colny':
           lbl_distance_railway_station = Label(Form,fg="red", text = "Ziddha Hospital, Kale Hospital, Gokul Hospital, Sushrut Hospital", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)
        else:
           lbl_distance_railway_station = Label(Form,fg="red", text = "No data found", font=('arial', 14), bd=15)
           lbl_distance_railway_station.grid(row=7)

        
       
 
   
     
    

