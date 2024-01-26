# Author: company name
# Version: 0.1

try:
    from Tkinter import *
    from ttk import Scrollbar
    from Tkconstants import *
except ImportError:
    from tkinter import Frame, Label, Message, StringVar, Entry, Button, messagebox, Canvas
    from tkinter.ttk import Scrollbar
    from tkinter.constants import *

import json
from table import *
from tkinter import *  
import csv
from dt import *
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from areahighlights import *


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="pass",
  database="realEstateDb"
)
input_year=0 

if __name__ == "__main__":
    try:
       from Tkinter import Tk
       
    except ImportError:
        from tkinter import Tk
        
class RealEstate():
      
    def __init__(self , master):
        self.master = master
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (w, h))
        master.configure(background='mediumpurple')         
        root = Frame(master, height=h, width=w)
        root.configure(background='mediumpurple')
        root.pack(side=TOP, pady=20)
       
          

        lbl_id_1 = Label(root,bg="mediumpurple", fg="yellow", text = "House Prediction System", font=('arial', 20))
        lbl_id_1.grid(row=0, column=2,pady=10)      

        lbl_id_2 = Label(root,bg="mediumpurple",fg="white", text = "Enter Area(Sq.Feet)", font=('arial', 10))
        lbl_id_2.place(x=0, y=100)  

        self.input_area = Entry(root, font=('arial', 10))
        self.input_area.place(x=150, y=100)  

          

        lbl_id_3 = Label(root,bg="mediumpurple",fg="white", text = "Quality(Range 1-10)", font=('arial', 10))
        lbl_id_3.place(x=0, y=150)  

        self.input_ovrquality = Entry(root, font=('arial', 10))
        self.input_ovrquality.place(x=150, y=150)  

        lbl_id_4 = Label(root,bg="mediumpurple",fg="white", text = "Condition(Range 1-10)", font=('arial', 10))
        lbl_id_4.place(x=0, y=200)    

        self.input_ovrcondition = Entry(root, font=('arial', 10))
        self.input_ovrcondition.place(x=150, y=200)     

        lbl_id_5 = Label(root,bg="mediumpurple",fg="white", text = "Year Built", font=('arial', 10))
        lbl_id_5.place(x=0, y=250) 

        self.input_YearBuilt = Entry(root, font=('arial', 10))
        self.input_YearBuilt.place(x=150, y=250)       
              
        lbl_id_6 = Label(root,bg="mediumpurple",fg="white", text = "Total Basment(Sq.Feet)", font=('arial', 10))
        lbl_id_6.place(x=0, y=300)

        self.input_totalBasment = Entry(root, font=('arial', 10))
        self.input_totalBasment.place(x=150, y=300)    
        
          

        lbl_id_7 = Label(root,bg="mediumpurple",fg="white", text = "Area Name", font=('arial', 10))
        lbl_id_7.place(x=0, y=350) 

        self.input_AreaName = Entry(root, font=('arial', 10))
        self.input_AreaName.place(x=150, y=350)       


        btn_Predict = Button(root,bg="indigo",fg="white", text="Apply Prediction", width=20, command=self.applyprediction)
        btn_Predict.place(x=0, y=380) 
        
        btn_Load_Data = Button(root,bg="indigo",fg="white", text="Show Property", width=20, command=self.showPropertyAreaWise)
        btn_Load_Data.place(x=150, y=380)         
        
        self.lbl_Op = Label(root,bg="mediumpurple", fg="orange", text = "Predicted Cost Range: ", font=('arial', 12))
        self.lbl_Op.grid(row=6, column=2)
        
        
        
        
        
        btn_Graph_avg_salePrice = Button(root,bg="indigo",fg="white", text="Avg Sale Price Graph", width=25, command=self.showgraphAvgSalesPrice)
        btn_Graph_avg_salePrice.grid(row=5,column=3,padx=10,pady=10)
        
        btn_Graph_avg_quality = Button(root,bg="indigo",fg="white", text="Avg Quality Graph", width=25, command=self.showgraphAvgQuality)
        btn_Graph_avg_quality.grid(row=6,column=3,padx=10,pady=10)
        
        btn_Graph_avg_condition = Button(root,bg="indigo",fg="white", text="Avg Condition Graph", width=25, command=self.showgraphAvgCondition)
        btn_Graph_avg_condition.grid(row=7,column=3,padx=10,pady=10)
        
        btn_Graph_area_year = Button(root,bg="indigo",fg="white", text="Area vs Year", width=25, command=self.showgraphAreaYear)
        btn_Graph_area_year.grid(row=8,column=3,padx=10,pady=10)
        
        btn_Area_Highlight = Button(root,bg="tomato",fg="white", text="Area Highlights", width=25, command=self.AreaHighlightPage)
        btn_Area_Highlight.grid(row=9,column=3,padx=10,pady=10)
        
        
        
        self.table_Data = Table(root, ["Sr.No","Area(Sq.Feet)", "Quality","Condition"," Year Built "," Basment(Sq.Feet) ","Price"], column_minwidths=[None, None, None, None])        
        self.table_Data.grid(row=3, column=3)

        
        
    def applyprediction(self):
        
        isBlank=0
        
        if self.input_area.get()=='':
           isBlank=1
        elif self.input_ovrquality.get()=='':
           isBlank=1 
        elif self.input_ovrcondition.get()=='':
           isBlank=1
        elif self.input_totalBasment.get()=='':
           isBlank=1 
        elif self.input_YearBuilt.get()=='':
           isBlank=1
           
        if isBlank==0:   
           mycursor = mydb.cursor()
           mysql_query="""SELECT * FROM propertydetails where LocationName=%s"""
           mycursor.execute(mysql_query, (self.input_AreaName.get().lower(),))
           myresult = mycursor.fetchall()
           dataset= [[]]        
           i=0     
           n_folds = 5
           max_depth = 5
           min_size = 10
           op=1
           inp_quality_value=-1 
           inp_condition_value=-1
           inp_basment_value=-1
           inp_year_value=-1
           inp_area_value=-1
           salepriceLowRange=0
           salepriceMediumRange=0  
           if (self.input_AreaName.get().lower()=='jaihind colny'):
               salepriceLowRange=100000
               salepriceMediumRange=150000
           elif (self.input_AreaName.get().lower()=='agra road'):   
               salepriceLowRange=262347
               salepriceMediumRange=275741
           elif (self.input_AreaName.get().lower()=='near stadium'):   
               salepriceLowRange=212410
               salepriceMediumRange=229224
           elif (self.input_AreaName.get().lower()=='agrawal nagar'):   
               salepriceLowRange=35311
               salepriceMediumRange=353184
           elif (self.input_AreaName.get().lower()=='sakri road'):   
               salepriceLowRange=198956
               salepriceMediumRange=166703
           elif (self.input_AreaName.get().lower()=='wadibhokar road'):   
               salepriceLowRange=118544
               salepriceMediumRange=134537           

           
           for row in myresult:                         
                   
                if row[6]>0 and row[6]<=salepriceLowRange:
                   op=0
                elif row[6]>salepriceLowRange and row[6]<=salepriceMediumRange:
                   op=1
                elif row[6]>salepriceMediumRange:
                   op=2      
                dataset.insert(i,[row[1],row[2],row[3],row[4],row[5],op])     
                i=i+1
            
        
           dataset.pop()
        
        
           
               
           for x in range(len(dataset[0])):
                str_column_to_float(dataset, x)
        
           input_area=int(self.input_area.get())
           input_quality=int(self.input_ovrquality.get())
           input_condition=int(self.input_ovrcondition.get())
           input_basment=int(self.input_totalBasment.get())  
           input_builtYear=int(self.input_YearBuilt.get())          
            #predictions = decision_tree(dataset, [[13682.0, 10, 5, 2006, 1410.0, -1]], max_depth, min_size)
           predictions = decision_tree(dataset, [[input_area, input_quality, input_condition, input_builtYear, input_basment, -1]], max_depth, min_size)
          # print (str(predictions))
           strop=str(predictions)
        
           if strop=='[0]':
              if (self.input_AreaName.get().lower()=='jaihind colny'):
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.800000)' 
              elif (self.input_AreaName.get().lower()=='agra road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.5250000)' 
              elif (self.input_AreaName.get().lower()=='near stadium'):   
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.4390000)'     
              elif (self.input_AreaName.get().lower()=='agrawal nagar'):   
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.6300000)'     
              elif (self.input_AreaName.get().lower()=='sakri road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.3020000)'         
              elif (self.input_AreaName.get().lower()=='wadibhokar road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Low (Rs.2200000)'             
           elif strop=='[1]':
                if (self.input_AreaName.get().lower()=='jaihind colny'):
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.1370000)' 
                elif (self.input_AreaName.get().lower()=='agra road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.4560000)' 
                elif (self.input_AreaName.get().lower()=='near stadium'):   
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.4793800)'     
                elif (self.input_AreaName.get().lower()=='agrawal nagar'):   
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.8600000)'     
                elif (self.input_AreaName.get().lower()=='sakri road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.3540000)'         
                elif (self.input_AreaName.get().lower()=='wadibhokar road'):   
                  self.lbl_Op['text']='Predicted Cost Range: Medium (Rs.2600000)' 
           elif strop=='[2]':
                if (self.input_AreaName.get().lower()=='jaihind colny'):
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.2020000)' 
                elif (self.input_AreaName.get().lower()=='agra road'):   
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.600000)' 
                elif (self.input_AreaName.get().lower()=='near stadium'):   
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.5053560)'     
                elif (self.input_AreaName.get().lower()=='agrawal nagar'):   
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.11100000)'     
                elif (self.input_AreaName.get().lower()=='sakri road'):   
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.5050000)'         
                elif (self.input_AreaName.get().lower()=='wadibhokar road'):   
                  self.lbl_Op['text']='Predicted Cost Range: High (Rs.3180000)' 
    
    def showPropertyAreaWise(self):
        mycursor = mydb.cursor()
        mysql_query="""SELECT * FROM propertydetails where LocationName=%s"""
        mycursor.execute(mysql_query, (self.input_AreaName.get().lower(),))
        myresult = mycursor.fetchall()
        
        T = [[]]
        i=0     
        
        for row in myresult: 
            T.insert(i,[i,row[1],row[2],row[3],'   '+str(row[4])+'   ','        '+str(row[5])+'        ',str(row[6]*20)]) 
            i=i+1
            
        if i>0:    
           self.table_Data.set_data(T)
        
    
    
    def showgraphAreaYear(self):
        mycursor = mydb.cursor()
        mysql_query="""SELECT COUNT(*) FROM propertydetails where LocationName=%s AND yearBuilt=%s"""
        mycursor.execute(mysql_query, (self.input_AreaName.get().lower(),self.input_YearBuilt.get(),))
        myresult = mycursor.fetchall() 
        
        count=0
        for row in myresult:         
            count=int(row[0])
        
        # Make fake dataset
            height = [0,count,0]
            str=self.input_AreaName.get().lower()+" vs "+self.input_YearBuilt.get()
            bars = ('',str,'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Area vs Year Built')
            plt.xlabel('Property Count')
            plt.ylabel('Property Count')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()
    
    
    def showgraphAvgCondition(self):
        mycursor = mydb.cursor()
        mysql_query="""SELECT AVG(overallCondition) FROM propertydetails where LocationName=%s"""
        mycursor.execute(mysql_query, (self.input_AreaName.get().lower(),))
        myresult = mycursor.fetchall() 
        
        avgCondition=0
        for row in myresult:         
            avgCondition=int(row[0])
        
        # Make fake dataset
            height = [0,avgCondition,0]
            bars = ('',self.input_AreaName.get().lower(),'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Average Condition')
            plt.xlabel('Avg Condition')
            plt.ylabel('Condition')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()        
            
            
    def showgraphAvgQuality(self):
        mycursor = mydb.cursor()
        mysql_query="""SELECT AVG(overallQuality) FROM propertydetails where LocationName=%s"""
        mycursor.execute(mysql_query, (self.input_AreaName.get().lower(),))
        myresult = mycursor.fetchall() 
        
        avgQuality=0
        for row in myresult:         
            avgQuality=int(row[0])
        
        # Make fake dataset
            height = [0,avgQuality,0]
            bars = ('',self.input_AreaName.get().lower(),'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Average Quality')
            plt.xlabel('Avg Quality')
            plt.ylabel('Quality')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()        
            
            
    def showgraphAvgSalesPrice(self):
        mycursor = mydb.cursor()
        mysql_query="""SELECT AVG(salesPrice) FROM propertydetails where LocationName=%s"""
        mycursor.execute(mysql_query, (self.input_AreaName.get(),))
        myresult = mycursor.fetchall() 
        
        avgsalesprice=0
        for row in myresult:         
            avgsalesprice=int(row[0])
        
        # Make fake dataset
            height = [0,avgsalesprice,0]
            bars = ('',self.input_AreaName.get().lower(),'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Average Sales price')
            plt.xlabel('Avg Sales Price')
            plt.ylabel('Sale Price')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()        
            
    #Fucntion to navigate AreaHighlightPage 
    def AreaHighlightPage(self):        
                self.newWindow = Toplevel(self.master)
                self.app = AreaHighlight(self.newWindow,self.input_AreaName.get().lower()) 
    
    def showgraphSalesPrice(self,salesPrice1,salesPrice2):
    
         
         mycursor = mydb.cursor()
         mysql_query="""SELECT COUNT(propertyID) FROM propertydetails where salesPrice > %s AND salesPrice < %s"""
         mycursor.execute(mysql_query, (salesPrice1,salesPrice2,))
         myresult = mycursor.fetchall()
         
         count_property=0;
         for row in myresult: 
            count_property=row[0]
            #print(count_property)    

            string="Sale Price Range Rs."
            string+=salesPrice1+' - Rs.'
            string+=salesPrice2
            #print(string)
         # Make fake dataset
            height = [0,count_property,0]
            bars = ('',string,'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Sales price wise Property Analysis')
            plt.xlabel('Sales Price')
            plt.ylabel('Property Count')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()    
        
        

    def showgraph(self,yearbuilt,yearsold):
    
         
         mycursor = mydb.cursor()
         mysql_query="""SELECT COUNT(propertyID) FROM propertydetails where yearBuilt=%s"""
         mycursor.execute(mysql_query, (yearbuilt,))
         myresult = mycursor.fetchall()
         
         count_year_built=0;
         for row in myresult: 
            count_year_built=row[0]
            #print(count_year_built)    

         mycursor = mydb.cursor()
         mysql_query="""SELECT COUNT(propertyID) FROM propertydetails where yearSold=%s"""
         mycursor.execute(mysql_query, (yearsold,))
         myresult = mycursor.fetchall()
         
         count_year_sold=0;
         for row in myresult: 
            count_year_sold=row[0]
            #print(count_year_sold)            
            
            yearbuilt='Built in '+yearbuilt
            yearsold='Sold in ' + yearsold
         # Make fake dataset
            height = [count_year_built,count_year_sold,0]
            bars = (yearbuilt,yearsold,'')
         
        # Choose the position of each barplots on the x-axis (space=1,4,3,1)
            y_pos = np.arange(len(bars))
            
            plt.title('Year Wise Property Built and Sold Analysis')
            plt.xlabel('Year')
            plt.ylabel('Property Count')
         
        # Create bars
            plt.bar(y_pos, height)
         
        # Create names on the x-axis
            plt.xticks(y_pos, bars)
         
        # Show graphic
            plt.show()

    
            
            
    