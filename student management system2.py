import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox 
import mysql.connector as sqltor
class lg:
       def __init__(self,root):
              self.root=root
              self.root.title("STUDENT MANAGEMENT SYSTEM")
              self.root.geometry("1350x700+0+0")
              self.root.configure(bg="black")
              #====================================================
              self.bg=ImageTk.PhotoImage(file="E:\Saksham/bg.jpg")
              self.user=ImageTk.PhotoImage(file="E:\Saksham/logo.jpg")
              #====================================================
              self.user_var=StringVar()
              self.pass_var=StringVar()
              #====================================================
              bg_lbl=Label(self.root,image=self.bg).pack()
              title=Label(self.root,text="LOGIN",font=("bahnschrift condensed",40,"bold"),bg="black",fg="blue",relief=GROOVE)
              title.place(x=0,y=0,relwidth=1)

              f1=Frame(self.root,bg="white")
              f1.place(x=400,y=110)

              logolbl=Label(f1,image=self.user,bd=0).grid(row=0,columnspan=2,pady=20)

              user=Label(f1,text="USER ID:",compound=LEFT,font=("bahnschrift condensed",40,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
              txt1=Entry(f1,bd=5,textvariable=self.user_var,relief=RIDGE,font=("bahnschrift condensed",25)).grid(row=1,column=1,padx=20,pady=10)

              passwrd=Label(f1,text="PASSWORD:",compound=LEFT,font=("bahnschrift condensed",40,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)              
              txt1=Entry(f1,bd=5,textvariable=self.pass_var,show='*',relief=RIDGE,font=("bahnschrift condensed",25)).grid(row=2,column=1,padx=20,pady=10)

              loginbtn=Button(f1,text="LOGIN",width=15,font=("bahnschrift condensed",20,"bold"),bg="white",fg="black").grid(row=3,column=1,pady=10,padx=20)

       def login(self):
             if self.user_var.get()=="Saksham" and self.pass_var.get()=="8961455191":
                     messagebox.showinfo("Successful","Welcome {self.user_var.get()}")
             else:
                     messagebox.showerror("Error","Invalid User ID or Password")
                     


root=Tk()
ob1=lg(root)
root.mainloop()
#================================================================================              
class student:
       def __init__(self,root):
              self.root=root
              self.root.title("STUDENT MANAGEMENT SYSTEM")
              self.root.geometry("1350x700+0+0")
              self.root.configure(bg='black')

              title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("bahnschrift condensed",30,"bold"),bg='black',fg="red",relief=GROOVE)
              title.pack(side=TOP,fill=X)
#===============================================================================
              self.Roll_no_var=StringVar()
              self.name_var=StringVar()
              self.class_var=StringVar()
              self.phone_var=StringVar()
              self.gender_var=StringVar()
              self.subject_var=StringVar()
              self.search_by=StringVar()
              self.search_txt=StringVar()
              
              
#==================Student's Details=====================================================================
              f1=Frame(self.root,bd=4,relief=GROOVE,bg='black')
              f1.place(x=18,y=72,width=480,height=600)

              f1_title=Label(f1,text="STUDENT'S DETAILS",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              f1_title.grid(row=0,columnspan=2,pady=20)

              l1=Label(f1,text="ROLL NUMBER:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l1.grid(row=1,column=0,pady=10,padx=20,sticky='w')

              e1=Entry(f1,textvariable=self.Roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
              e1.grid(row=1,column=1,pady=10,padx=20,sticky="w")

              l2=Label(f1,text="NAME:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l2.grid(row=2,column=0,pady=10,padx=20,sticky='w')
              
              e2=Entry(f1,textvariable=self.name_var,font=("bahnschrift condensed",15,"bold"),bd=5,relief=GROOVE)
              e2.grid(row=2,column=1,pady=10,padx=20,sticky="w")
              
              l3=Label(f1,text="PHONE NUMBER:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l3.grid(row=3,column=0,pady=10,padx=20,sticky='w')
              
              e3=Entry(f1,textvariable=self.phone_var,font=("bahnschrift condensed",15,"bold"),bd=5,relief=GROOVE)
              e3.grid(row=3,column=1,pady=10,padx=20,sticky="w")
                     
              l4=Label(f1,text="CLASS:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l4.grid(row=4,column=0,pady=10,padx=20,sticky='w')

              e4=ttk.Combobox(f1,textvariable=self.class_var,font=("bahnschrift condensed",20,"bold"))
              e4['values']=("I - A","I - B","I - C","II - A",'II - B',"II - C",'III - A','III - B','III - C','IV - A','IV - B','IV - C','V - A','V - B','V - C','VI - A','VI - B','VI - C','VII - A','VII - B','VII - C','VIII - A','VIII - B','VIII - C','IX - A','IX - B','IX - C','X - A','X - B','X - C','X- D','XI - A','XI - B','XI - C','XI - D','XII - A','XII - B','XII - C','XII - D')
              e4.grid(row=4,column=1,pady=10,padx=20,sticky='w')

              l5=Label(f1,text="GENDER:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l5.grid(row=5,column=0,pady=10,padx=20,sticky='w')

              e5=ttk.Combobox(f1,textvariable=self.gender_var,font=("bahnschrift condensed",20,"bold"))
              e5['values']=("MALE","FEMALE","OTHERS")
              e5.grid(row=5,column=1,pady=10,padx=20,sticky='w')

              l6=Label(f1,text="SUBJECTS:",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              l6.grid(row=6,column=0,pady=10,padx=20,sticky='w')

              e6=ttk.Combobox(f1,textvariable=self.subject_var,font=("bahnschrift condensed",20,"bold"))
              e6['values']=("ENGLISH, HINDI, MATHS, ENIVRONMENTAL STUDIES (FOR CLASSES I - V)","ENGLISH, HINDI, MATHS, SCIENCE, SOCIAL STUDIES, SANSKRIT (FOR CLASSES VI - VIII WITH SANSKRIT AS A SUBJECT)","ENGLISH, HINDI, MATHS, SCIENCE, SOCIAL STUDIES, GERMAN (FOR CLASSES VI - VIII WITH GERMAN AS A SUBJECT)","ENGLISH, MATHS, HINDI, SCIENCE, SOCIAL STUDIES (FOR CLASSES IX AND X)","ENGLISH, MATHS, PHYSICS, CHEMISTRY, COMPUTER SCIENCE (FOR CLASSES XI - A AND XII - A)","ENGLISH, MATHS, BIOLOGY, PHYSICS, CHEMISTRY (FOR CLASSES XI - B AND XII - B WITH MATHS AS A SUBJECT)","ENGLISH, HINDI, BIOLOGY, PHYSICS, CHEMISTRY (FOR CLASSES XI - B AND XII - B WITH HINDI AS A SUBJECT)","ENGLISH, HINDI, ACCOUNTANCY, BUSINESS STUDIES, ECONOMICS (FOR CLASSES XI - C AND XII - C WITH HINDI AS A SUBJECT)","ENGLISH, MATHS, ACCOUNTANCY, BUSINESS STUDIES, ECONOMICS (FOR CLASSES XI - C AND XII - C WITH MATHS AS A SUBJECT","ENGLISH, IP, ACCOUNTANCY, BUSINESS STUDIES, ECONOMICS (FOR CLASSES XI - C AND XII - C WITH IP AS A SUBJECT","ENGLISH, HINDI, POLITICAL SCIENCE/ ECONOMICS/ MATHS,HISTORY, GEOGRAPHY (FOR CLASSES XI - D AND XII - D ")
              e6.grid(row=6,column=1,pady=10,padx=20,sticky='w')
#============================Buttons=======================================================================

              btn_frame=Frame(f1,bd=4,relief=GROOVE,bg='black')
              btn_frame.place(x=30,y=500,width=410,height=50)
              Addbtn=Button(btn_frame,text="ADD",width=10,command=self.addstudent).grid(row=0,column=0,padx=10,pady=10)
              updatebtn=Button(btn_frame,text="UPDATE",width=10,command=self.udata).grid(row=0,column=1,padx=10,pady=10)
              delbtn=Button(btn_frame,text="DELETE",width=10,command=self.ddata).grid(row=0,column=2,padx=10,pady=10)
              clbtn=Button(btn_frame,text="CLEAR",width=10,command=self.clr).grid(row=0,column=3,padx=10,pady=10)

              


#==================================DETAILS================================================================
              f2=Frame(self.root,bd=4,relief=GROOVE,bg='black')
              f2.place(x=500,y=72,width=840,height=600)

              lbl_Search=Label(f2,text="SEARCH BY",bg='black',fg='white',font=("bahnschrift condensed",20,"bold"))
              lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

              combo_search=ttk.Combobox(f2,textvariable=self.search_by,width=12,font=("bahnschrift condensed",20,"bold"),state='readonly')
              combo_search['values']=("roll_no","name","phone_no")
              combo_search.grid(row=0,column=1,pady=10,padx=20)

              txt_search=Entry(f2,textvariable=self.search_txt,font=("bahnschrift condensed",17,"bold"),bd=5,relief=GROOVE)
              txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

              searchbtn=Button(f2,text="SEARCH",width=10,pady=8,command=self.sdata).grid(row=0,column=3,padx=10,pady=10)
              showallbtn=Button(f2,text="SHOW ALL",width=10,pady=8,command=self.fdata).grid(row=0,column=4,padx=10,pady=10)

#=============================TABLE DETAILS====================================================================

              Table_frame=Frame(f2,bd=4,relief=GROOVE,bg='black')
              Table_frame.place(x=10,y=70,width=810,height=510)

              scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
              scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
              self.Student_table=ttk.Treeview(Table_frame,columns=("Roll Number","Name","Phone Number","Class","Gender","Subjects"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
              scroll_x.pack(side=BOTTOM,fill=X)
              scroll_y.pack(side=RIGHT,fill=Y)
              scroll_x.config(command=self.Student_table.xview)
              scroll_y.config(command=self.Student_table.yview)
              self.Student_table.heading("Roll Number",text="Roll Number")
              self.Student_table.heading("Name",text="Name")
              self.Student_table.heading("Phone Number",text="Phone Number")
              self.Student_table.heading("Class",text="Class")
              self.Student_table.heading("Gender",text="Gender")
              self.Student_table.heading("Subjects",text="Subjects")
              self.Student_table['show']='headings'
              self.Student_table.column("Roll Number",width=50)
              self.Student_table.column("Name",width=150)
              self.Student_table.column("Phone Number",width=150)
              self.Student_table.column("Class",width=200)
              self.Student_table.column("Gender",width=100)
              self.Student_table.column("Subjects",width=200)
              self.Student_table.pack(fill=BOTH,expand=1)
              self.Student_table.bind("<ButtonRelease-1>",self.gcursor)
              self.fdata()
              #self.root.mainloop()

#==================================FUNCTIONS================================================================
       def addstudent(self):
                            con=sqltor.connect(host='localhost',user='root',passwd='8961455191',database='saksham')
                            cur=con.cursor()
                            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),self.name_var.get(),self.phone_var.get(),self.class_var.get(),self.gender_var.get(),self.subject_var.get()))
                            con.commit()
                            self.fdata()
                            self.clr()
                            con.close()

       def fdata(self):
              con=sqltor.connect(host='localhost',user='root',passwd='8961455191',database='saksham')
              cur=con.cursor()
              cur.execute("select * from students")
              rows=cur.fetchall()
              if len(rows)!=0:
                     self.Student_table.delete(*self.Student_table.get_children())
                     for row in rows:
                            self.Student_table.insert('',END,values=row)
                     con.commit()
              con.close()

       def clr(self):
              self.Roll_no_var.set("")
              self.name_var.set("")
              self.class_var.set("")
              self.phone_var.set("")
              self.gender_var.set("")
              self.subject_var.set("")
              

       def gcursor(self,ev):
              cursor_row=self.Student_table.focus()
              contents=self.Student_table.item(cursor_row)
              row=contents['values']
              self.Roll_no_var.set(row[0])
              self.name_var.set(row[1])
              self.class_var.set(row[2])
              self.phone_var.set(row[3])
              self.gender_var.set(row[4])
              self.subject_var.set(row[5])
              

       def udata(self):
              con=sqltor.connect(host='localhost',user='root',passwd='8961455191',database='saksham')
              cur=con.cursor()
              cur.execute("update students set name=%s,class=%s,phone_no=%s,gender=%s,address=%s where roll_no=%s",(self.name_var.get(),self.class_var.get(),self.phone_var.get(),self.gender_var.get(),self.subject_var.get(),self.Roll_no_var.get()))
              con.commit()
              self.fdata()
              self.clr()
              con.close()

       def ddata(self):
              con=sqltor.connect(host='localhost',user='root',passwd='8961455191',database='saksham')
              cur=con.cursor()
              cur.execute("delete from students where roll_no=%s",self.Roll_no_var.get())
              con.commit()
              con.close()
              self.fdata()
              self.clr()

       def sdata(self):
              con=sqltor.connect(host='localhost',user='root',passwd='8961455191',database='saksham')
              cur=con.cursor()
              cur.execute("select * from students where "+"self.search_by.get()"+"LIKE '%"+"self.search_txt.get()"+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                     self.Student_table.delete(*self.Student_table.get_children())
                     for row in rows:
                            self.Student_table.insert('',END,values=row)
                     con.commit()
              con.close()
              
root=Tk()
ob2=student(root)
root.mainloop()
              
              

