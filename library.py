
from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
import mysql.connector

class LibrarymanagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library management System")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="#27252b")
        icon = PhotoImage(file ='lm.png')
        self.root.iconphoto(False, icon)

        # ========== Variables ==============

        self.member_var=StringVar()
        self.ref_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()

        # ================= TitleLabel ==================

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="#D3D3D3",fg="#27252b",bd=20,relief=FLAT,font=("Agency FB",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        def time(): 
            string = strftime('%I:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(lbltitle, font = ('times new roman',15, 'bold'),background = 'purple',foreground = 'white') 
        #lbl.place(x=0,y=0,width=150) 
        time() 
        
        # ============== Dataframe ==================

        DataFrame=Frame(self.root,bd=20,padx=20,relief=FLAT,bg="#27252b")
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=12,padx=20,relief=FLAT,bg="#D3D3D3",fg="#27252b",
                                                font=("Agency FB",20,"bold"),text="Library Membership Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=400)

        DataFrameRight=LabelFrame(DataFrame,bd=12,padx=20,relief=FLAT,bg="#D3D3D3",fg="#27252b",
                                            font=("Agency FB",20,"bold"),text="Book Details")
        DataFrameRight.place(x=910,y=5,width=540,height=400)

        # =========== Buttonframe ==================

        ButtonFrame=Frame(self.root,bd=20,padx=8,relief=FLAT,bg="#27252b")
        ButtonFrame.place(x=15,y=530,width=1530,height=90)

        # ============== ButtonFrame ======================

        btnAddData=Button(ButtonFrame,command=self.add_data,text="REGISTER",font=("arial",17,"bold"),width=17,bg="#D3D3D3",fg="#27252b")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(ButtonFrame,command=self.showData,text="SHOW DATA",font=("arial",17,"bold"),width=17,bg="#D3D3D3",fg="#27252b")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",17,"bold"),width=16,bg="#D3D3D3",fg="#27252b")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,command=self.mDelete,text="DELETE",font=("arial",17,"bold"),width=16,bg="#D3D3D3",fg="#27252b")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",17,"bold"),width=16,bg="#D3D3D3",fg="#27252b")
        btnReset.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.iExit,text="EXIT",font=("arial",17,"bold"),width=17,bg="#D3D3D3",fg="#27252b")
        btnExit.grid(row=0,column=5)

        # ======= Framedetails ===============

        FrameDetails=Frame(self.root,bd=20,padx=20,relief=FLAT,bg="#27252b")
        FrameDetails.place(x=0,y=600,width=1920,height=200)

        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6,bg="#D3D3D3")
        lblMember.grid(row=0,column=0,sticky=W)

        comMenber=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",
                                                        font=("arial",12,"bold"),width=27)
        comMenber['value']=("Admin Staff","Lecturer","Student")
        comMenber.current(0)
        comMenber.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,bg="#D3D3D3")
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref_var,width=29)
        txtref.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="#D3D3D3")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.title_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,pady=6,bg="#D3D3D3")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Surname:",padx=2,pady=6,bg="#D3D3D3")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6,bg="#D3D3D3")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6,bg="#D3D3D3")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Post Code:",padx=2,pady=4,bg="#D3D3D3")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile Number:",padx=2,pady=6,bg="#D3D3D3")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,bg="#D3D3D3")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="#D3D3D3")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="#D3D3D3")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="#D3D3D3")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="#D3D3D3")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="#D3D3D3")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="#D3D3D3")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
   
        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="#D3D3D3")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdate.grid(row=7,column=3)
   
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="#D3D3D3")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice,width=29)
        txtActualPrice.grid(row=8,column=3)

        # ==============$DataframeRight===============

        # ================textBox================

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        # ============ListBox==============

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        ListOfBooks=['Internet of Things','Web Services','Python Programming',"DBMS vol1 ",'OOP C++','Digital Marketing','Basics of HTML','Data Structures in C++','Communication Skills','Angular JS Sem3','Django begginer','Excel Advance Sheets','3D Rendering CyclesX','Arch Viz','English Grammer','Marathi Poems','Hindi Rashtra Bhasha','GUI in Python','Cyber security','Accounting v3','Android Programming (kotlin)','Rdbms','Advance MYSQL','C# by Microsoft','Spring boot Java','Intro to linux','Wings Of Fire','Believe In Yourself','Fear Not: Be Strong','The World As I See It','Think & Grow Rich','Rich Dad Poor Dad']

        def SelectBook(event=""):
            value=str(bookList.get(bookList.curselection()))
            x=value
            if (x=="Internet of Things"):
                self.bookid_var.set("BKID5487")
                self.booktitle_var.set("Internet Of Things")
                self.author_var.set("Cham berry")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.375")

            elif (x=="Web Services"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Web Services")
                self.author_var.set("R. lincon")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.425")

            
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Intro to python Comp Science")
                self.author_var.set("John Zhelle")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.500")

            
            elif (x=="DBMS vol1 "):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Database management Systems")
                self.author_var.set("Dr Ruchita vadnere")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.289")

            
            elif (x=="OOP C++"):
                self.bookid_var.set("BKID2546")
                self.booktitle_var.set("OOP C++")
                self.author_var.set("Brian Jones")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.354")

            
            elif (x=="Digital Marketing"):
                self.bookid_var.set("BKID8795")
                self.booktitle_var.set("Digital Marketting")
                self.author_var.set("K.P Sharma")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.319")

            
            elif (x=="Basics of HTML"):
                self.bookid_var.set("BKID8789")
                self.booktitle_var.set("Basic Of  HTML")
                self.author_var.set("Marlow Willson")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.15")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.25")

            elif (x=="Data Structures in C++"):
                self.bookid_var.set("BKID6749")
                self.booktitle_var.set("Data Structures in C++")
                self.author_var.set("Dr Archana Karla")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.205")

            elif (x=="Communication Skills"):
                self.bookid_var.set("BKID6750")
                self.booktitle_var.set("Advance Communication Skills")
                self.author_var.set("Mr Sahil D")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.905")

            elif (x=="Angular JS Sem3"):
                self.bookid_var.set("BKID9750")
                self.booktitle_var.set("Angular JS Sem3 BBA CA 2019")
                self.author_var.set("Mr Amit Dixit")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.1005")

            elif (x=="Django begginer"):
                self.bookid_var.set("BKID6056")
                self.booktitle_var.set("Django begginer")
                self.author_var.set("Mr Bipin Baby")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.499")

            elif (x=="Excel Advance Sheets"):
                self.bookid_var.set("BKID6756")
                self.booktitle_var.set("Excel Advance Sheets")
                self.author_var.set("Mrs Pooja .D")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.600")

            elif (x=="3D Rendering CyclesX"):
                self.bookid_var.set("BKID2512")
                self.booktitle_var.set("3D Rendering CyclesX in Blender")
                self.author_var.set("Blender Guru")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.10")

            elif (x=="Arch Viz"):
                self.bookid_var.set("BKID251")
                self.booktitle_var.set("Arch Viz in Blender")
                self.author_var.set("Blender Guru")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.10")

            elif (x=="English Grammer"):
                self.bookid_var.set("BKID2598")
                self.booktitle_var.set("English Grammer")
                self.author_var.set("Prof Indulkar")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.220")   

            elif (x=="Marathi Poems"):
                self.bookid_var.set("BKID225")
                self.booktitle_var.set("Poems in Marathi")
                self.author_var.set("Prof Omkar .C")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.220")

            elif (x=="Hindi Rashtra Bhasha"):
                self.bookid_var.set("BKID267")
                self.booktitle_var.set("Hindi Rashtra Bhashai")
                self.author_var.set("Prof Omkar .C")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.500")   


            elif (x=="GUI in Python"):
                self.bookid_var.set("BKID265")
                self.booktitle_var.set("GUI in Python Tkinter")
                self.author_var.set("mr Dinesh Kumar")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.750")

            elif (x=="Cyber security"):
                self.bookid_var.set("BKID565")
                self.booktitle_var.set("Cyber security")
                self.author_var.set("Mr Atharva salunke")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.850")

            elif (x=="Accounting v3"):
                self.bookid_var.set("BKID865")
                self.booktitle_var.set("Accounting v3")
                self.author_var.set("Mr Atharva bajaj")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.950")

            elif (x=="Android Programming (kotlin)"):
                self.bookid_var.set("BKID1255")
                self.booktitle_var.set("Android Programming in Kotlin")
                self.author_var.set("Mr Sushant bhere")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.1150")

            elif (x=="Rdbms"):
                self.bookid_var.set("BKID8955")
                self.booktitle_var.set("Relational databse in Oracle")
                self.author_var.set("Mr K.l simpson")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.1000")

            elif (x=="Advance MYSQL"):
                self.bookid_var.set("BKID165")
                self.booktitle_var.set("Advance MYSQL")
                self.author_var.set("Mr Ryan Thompson")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.2150")

            elif (x=="C# by Microsoft"):
                self.bookid_var.set("BKID8368")
                self.booktitle_var.set("C# by Microsoft")
                self.author_var.set("Mr J.kilkarni")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.1000")

            elif (x=="Spring boot Java"):
                self.bookid_var.set("BKID364")
                self.booktitle_var.set("Spring boot Java")
                self.author_var.set("Free code camp")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.15")


            elif (x=="Intro to linux"):
                self.bookid_var.set("BKID2687")
                self.booktitle_var.set("Intro to linux")
                self.author_var.set("Free code camp")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.15") 

            elif (x=="Wings Of Fire"):
                self.bookid_var.set("BKID880")
                self.booktitle_var.set("Wings Of Fire")
                self.author_var.set("Dr. APJ Kalam")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("20")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.150") 

            elif (x=="Believe In Yourself"):
                self.bookid_var.set("BKID800")
                self.booktitle_var.set("Believe In Yourself")
                self.author_var.set("Joseph Murphy")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("40")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.450") 
            
            elif (x=="Fear Not: Be Strong"):
                self.bookid_var.set("BKID1900")
                self.booktitle_var.set("Fear Not: Be Strong")
                self.author_var.set("Swami Vivekanand")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("100")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.199") 
            
            elif (x=="The World As I See It"):
                self.bookid_var.set("BKID0003")
                self.booktitle_var.set("The World As I See It")
                self.author_var.set("Albert Einstein")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("8")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.599")
            
            elif (x=="Think & Grow Rich"):
                self.bookid_var.set("BKID793")
                self.booktitle_var.set("Think & Grow Rich")
                self.author_var.set("Nepoleon Hill")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("48")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.349")

            elif (x=="Rich Dad Poor Dad"):
                self.bookid_var.set("BKID623")
                self.booktitle_var.set("Rich Dad Poor Dad")
                self.author_var.set("Robert Kiyosaki")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("10")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.299")

        bookList=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        bookList.bind('<<ListboxSelect>>',SelectBook)
        bookList.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=bookList.yview)

        for item in ListOfBooks:
            bookList.insert(END,item)
        
        # ========== Scrollbar =================

        Table_frame=Frame(FrameDetails,bd=6,relief=FLAT)
        Table_frame.place(x=0,y=1,width=1460,height=150)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("member","ref","title","firtname","lastname","adress1",
                                            "adress2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                            "datedue","days","latereturnfine","dateoverdue","finalprice")
                                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("member",text="Member Type")
        self.library_table.heading("ref",text="PRN No.")
        self.library_table.heading("title",text="ID No.")
        self.library_table.heading("firtname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post Code")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
   
        self.library_table.column("member",width=100)
        self.library_table.column("ref",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firtname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        self.library_table.pack(fill=BOTH,expand=1)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


    # ============== Function Declaration =================

    def add_data(self):
        if self.member_var.get()=="" or self.postcode_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        
        else:
            try:
                conn=mysql.connector.connect(host='localhost',port=3306,username='root',password='',database='library')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.member_var.get(),
                    self.ref_var.get(),
                    self.title_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.author_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get()                                                        
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success","Member has been inserted")
             
            except Exception as es:
                messagebox.showerror("Error",f" Must be enter Integer number,PRN NO&ID NO is Primery Key :{str(es)}",parent=self.root)

    def update_data(self):
        if self.ref_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            conn=mysql.connector.connect(host='localhost',port=3306,username='root',password='',database='library')
            my_cursor=conn.cursor()
            my_cursor.execute("update library set Member_type=%s,ID_No=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,DaysOfBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_No=%s",
            (
                self.member_var.get(),                                                                              
                self.title_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook.get(),
                self.lateratefine_var.get(),
                self.dateoverdue.get(),
                self.finallprice.get(),  
                self.ref_var.get() 
            ))
                                                                                                    
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been updated successfully")


                 
    def fatch_data(self):
        conn=mysql.connector.connect(host='localhost',port=3306,username='root',password='',database='library')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.ref_var.set(row[1]),
        self.title_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17])


    def mDelete(self): 
        if self.ref_var.get()=="":
            messagebox.showinfo("ERROR","First Select the Member!!")
        else:
            conn=mysql.connector.connect(host='localhost',port=3306,username='root',password='',database='library')
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.ref_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            conn.close()
            self.fatch_data()
            self.reset()
            messagebox.showinfo("DELETE","Member has been Deleted successfully")         


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Confirm if you want to exit")
        if iExit>0:
            root.destroy()
            return

    def reset(self):
        self.member_var.set(""),
        self.ref_var.set(""),
        self.title_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue.set(""),
        self.finallprice.set("")
        self.txtBox.delete("1.0",END)   

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.ref_var.get() + "\n") 
        self.txtBox.insert(END,"ID No:\t\t"+ self.title_var.get() + "\n")           
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")   
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")   
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")   
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")   
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")   
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")   
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")   
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")   
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")   
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")   
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")   
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook.get() + "\n")   
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.lateratefine_var.get() + "\n")   
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue.get() + "\n")   
        self.txtBox.insert(END,"FinallPrice:\t\t"+ self.finallprice.get() + "\n")   
        
   
            

if __name__ == "__main__":
    root=Tk()
    obj=LibrarymanagementSystem(root)
    root.mainloop()
