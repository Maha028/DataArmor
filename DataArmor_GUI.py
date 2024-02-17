from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import k_Anonymity as md
import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd
import os
color1='#020f12'
color2='#BDE0FE'
color3='#65e7ff'
color4='pink'
class Page1:
    def __init__(self,root):
        self.root=root
        self.root.geometry('800x500+500+100')
        self.root.title('DataArmor')
        self.root.config(background='#BDE0FE')
        self.root.resizable(False,False)
        self.title= Label(self.root , 
                     foreground="black",
                     text='DataArmor',
                     bg="#BDE0FE",
                     highlightcolor='pink',
                     font=('century',28),
                     )
        self.title.place(x=320, y=150)
        self.btn = Button(root, 
             text ="Start", 
             command = self.load_new,
             background=color4,
             foreground=color2,
             activebackground=color2,
             activeforeground=color4,
             highlightthickness=2,
             highlightbackground=color2,
             highlightcolor='white',
             font=('Times New Roman',20, 'bold'),
             fg='white',
             cursor='hand2',
             )
        self.btn.place(x=375, y=230)
    def load_new(self):
        self.title.destroy()
        self.btn.destroy()
        self.another=Page2(self.root)


#--------------------Page2---------------------------
class Page2:
     def __init__(self,root):
        self.root=root
        self.root.geometry('800x600+500+100')
        self.root.title('DataArmor')
        self.root.config(background=color2)
        self.root.resizable(True,True)
        self.f1 = Frame(self.root,bg=color2)
        self.f1.pack()
        self.title= Label(self.f1 , 
                     text='DataArmor',
                     bg=color2,
                     font=('monospace',22),
                     )
        self.title.pack(padx=20, pady=20)
        v = IntVar()
        
        self.radio1=Radiobutton(self.f1, 
               text="DataBase connection",
               padx = 20, 
               variable=v, 
               value=1,
               bg=color2,
               font=('Times New Roman',18),
               command=self.addEntry)
        self.radio1.pack(padx=5, pady=5)

        self.radio2=Radiobutton(self.f1, 
               text="flat file",
               padx = 20, 
               variable=v, 
               bg=color2,
               value=2,
               font=('Times New Roman',18),
               command=self.Entry_destroy)
        self.radio2.pack(padx=5, pady=5)
        self.up_bt=Button(self.f1,text='Open a File',command=self.file_uploading)
        self.f = Frame(self.root,bg=color2)
        self.f.pack()
        
#------------------variables--------------------------
        self.host=StringVar()
        self.user=StringVar()
        self.passw=StringVar()
        self.port=StringVar()
        self.database=StringVar()
        self.table=StringVar()
#------------------------------------------------------------------
#check button
     def check_btn(self):
        self.check_bt= Button(self.f1,text = 'Next', command = self.load_new, 
            background=color4,
             foreground="black",
             activebackground=color2,
             activeforeground=color4,
             highlightthickness=2,
             highlightbackground=color2,
             highlightcolor='white',
             font=('monospace',14),
             cursor='hand2')
        self.up_bt.destroy()
        self.check_bt.pack(padx=10,pady=20)  
        button = Button(self.f1, text="Re upload dataset",
                           command=self.back, 
                          background=color4,
                           foreground=color2,
                           activebackground=color2,
                           activeforeground=color4,
                           highlightthickness=2,
                           highlightbackground=color2,
                           highlightcolor='white',
                           font=('monospace',8),
                           fg='black',
                           cursor='hand2')
        button.pack()

#-----------------------------------------------------------------
#inputs
     def addEntry(self):
        self.f.destroy()
        self.f = Frame(self.root)
        self.f.pack()
        self.root.geometry('800x700+500+50')
        self.pers= Label(self.f , 
                     text='Connection info: ',
                     bg=color2,
                     font=('monospace',14)
                     )
        self.pers.pack(padx=10,pady=10)
        self.host_label=Label(self.f, text='Host:')
        self.host_label.pack(padx=5,pady=5)
        self.host_entry=Entry(self.f, textvariable=self.host, bg='#598AB0', justify='center')
        self.host_entry.pack(padx=5,pady=5)

        self.user_label=Label(self.f, text='User Name:')
        self.user_label.pack(padx=5,pady=5)
        self.user_entry=Entry(self.f, textvariable=self.user, bg='#598AB0', justify='center')
        self.user_entry.pack(padx=5,pady=5)

        self.passw_label=Label(self.f, text='Password:')
        self.passw_label.pack(padx=5,pady=5)
        self.passw_entry=Entry(self.f, textvariable=self.passw, bg='#598AB0', justify='center')
        self.passw_entry.pack(padx=5,pady=5)
        
        self.port_label=Label(self.f, text='Port Number:')
        self.port_label.pack(padx=5,pady=5)
        self.port_entry=Entry(self.f, textvariable=self.port, bg='#598AB0', justify='center')
        self.port_entry.pack(padx=5,pady=5)

        self.database_label=Label(self.f, text='Database Name:')
        self.database_label.pack(padx=5,pady=5)
        self.database_entry=Entry(self.f, textvariable=self.database, bg='#598AB0', justify='center')
        self.database_entry.pack(padx=5,pady=5)

        self.table_label=Label(self.f, text='Database Name::')
        self.table_label.pack(padx=5,pady=5)
        self.table_entry=Entry(self.f, textvariable=self.table, bg='#598AB0', justify='center')
        self.table_entry.pack(padx=5,pady=5)

        self.check_btn()
#----------------------------------------------------------------------
#file upload:
      
     def Entry_destroy(self):
         self.f.destroy()
         self.f = Frame(self.root)
         self.f.pack()
         self.up_bt=Button(self.f,text='Open a File',command=self.file_uploading,
                           bg=color4,
                           activebackground=color2,
                           activeforeground="black",
         font=('Times New Roman',10),)
         self.up_bt.pack()
         
     def file_uploading(self):
        
        filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*'))

        self.filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

        showinfo(title='Selected File',
        message=self.filename)
        self.check_btn()
     def back(self):
         self.f1.destroy()
         self.f.destroy()
         self.another=Page2(self.root)
     def load_new(self):
        self.f1.destroy()
        self.f.destroy()
        self.another=Page3(self.root,self.filename)
#--------------------Page3---------------------------
class Page3:
     def __init__(self,root,file):
         
   #-----------------variables------------------------
        self.file=str(file)
        self.EID=StringVar()
        self.num_qids=StringVar()
        self.cat_qids=StringVar()
        self.SV=StringVar()
        self.k=StringVar()
        self.l=StringVar() 
   #--------------------------------------------------
        self.root=root
        self.root.geometry('800x500+500+100')
        self.title= Label(self.root , 
                     text='DataArmor',
                     bg=color2,
                     font=('monospace',22),
                     )
        self.title.pack(padx=20, pady=20)
        self.f1=Frame(self.root,bg=color2)
        self.f1.pack()
        
        self.EID_label=Label(self.f1, text='Enter Explicit Attributes:')
        self.EID_label.pack(padx=5,pady=5)
        self.EID_entry=Entry(self.f1, textvariable=self.EID, bg='#598AB0', justify='center')
        self.EID_entry.pack(padx=5,pady=5)
        
        
        self.QN_label=Label(self.f1, text='Enter Numeric Quasi Identifiers:')
        self.QN_label.pack(padx=5,pady=5)
        self.QN_entry=Entry(self.f1, textvariable=self.num_qids, bg='#598AB0', justify='center')
        self.QN_entry.pack(padx=5,pady=5)
        
        
        self.QC_label=Label(self.f1, text='Enter Non-numeric Quasi Identifiers:')
        self.QC_label.pack(padx=5,pady=5)
        self.QC_entry=Entry(self.f1, textvariable=self.cat_qids, bg='#598AB0', justify='center')
        self.QC_entry.pack(padx=5,pady=5)

        '''self.SV_label=Label(self.root, text='Enter Senstive Atributes:')
        self.SV_label.pack(padx=5,pady=5)
        self.SV_entry=Entry(self.root, textvariable=self.SV, bg='#598AB0', justify='center')
        self.SV_entry.pack(padx=5,pady=5)'''
        Label(self.f1,text="caution!!! separate it with ,",bg=color2,font=('13')).pack()

        self.k_label=Label(self.f1, text='Enter value of K:')
        self.k_label.pack(padx=5,pady=5)
        self.k_entry=Entry(self.f1, textvariable=self.k, bg='#598AB0', justify='center')
        self.k_entry.pack(padx=5,pady=5)
        '''
        self.l_label=Label(self.root, text='Enter value of l:')
        self.l_label.pack(padx=5,pady=5)
        self.l_entry=Entry(self.root, textvariable=self.l, bg='#598AB0', justify='center')
        self.l_entry.pack(padx=5,pady=5)
        '''
        self.anon_btn()
        self.button = tk.Button(self.root, text="Restart",
                           command=self.Restart, 
                           background=color4,
                            foreground=color2,
                            activebackground=color2,
                            activeforeground=color4,
                            highlightthickness=2,
                            highlightbackground=color2,
                            highlightcolor='white',
                            font=('monospace',8),
                            fg='black',
                            cursor='hand2')
        self.button.pack()
        
     def anon_btn(self):
        self.anon_bt= Button(self.f1,text = 'Anonymize',
            command=self.get_input_and_call_mondrian,  
            background=color4,
             foreground=color2,
             activebackground=color2,
             activeforeground=color4,
             highlightthickness=2,
             highlightbackground=color2,
             highlightcolor='white',
             font=('monospace',14),
             fg='white',
             cursor='hand2')
        self.anon_bt.pack(padx=10,pady=10)  

     def get_input_and_call_mondrian(self):
        if self.EID:
            self.EID=str(self.EID.get())
            self.EID=self.EID.replace(" ", "")
            self.EID=self.EID.split(",")
        self.num_qids=str(self.num_qids.get())
        self.num_qids=self.num_qids.replace(" ", "")
        self.cat_qids=str(self.cat_qids.get())
        self.cat_qids=self.cat_qids.replace(" ", "")
        self.num_qids=self.num_qids.split(",")
        self.cat_qids= self.cat_qids.split(",")
        #self.SV=str(self.SV.get())
        self.k=int(self.k.get())
        #self.l=int(self.l.get()) 
        
        m=md.mondrian(self.file, self.EID ,self.cat_qids, self.num_qids, self.k )
        self.result_partitions=m.result_partitions
        self.load_new()
        
     def Restart(self):
            self.root.destroy()
            root=Tk()
            Page1(root)
     def load_new(self):
       self.anon_bt.destroy()
       self.button.destroy()
       self.f1.destroy()
       self.another=page4(self.root,self.result_partitions)

class page4:
    def __init__(self,root,result_partitions):
        self.root=root
        self.root.geometry('800x500+500+100')
        self.f1=Frame(self.root)
        self.result_partitions=result_partitions
            
        self.open_button = tk.Button(root, text="View anonymized data", command=self.load_new, 
            background=color4,
             foreground=color2,
             activebackground=color2,
             activeforeground=color4,
             highlightthickness=2,
             highlightbackground=color2,
             highlightcolor='black',
             font=('monospace',10),
             fg='black',
             cursor='hand2')
        self.open_button.pack(padx=20, pady=10)
        
        self.down_button = Button(self.root, text="Download anonymized data", command=self.save_in_csv_file,
                                  background=color4,
                                   foreground=color2,
                                   activebackground=color2,
                                   activeforeground=color4,
                                   highlightthickness=2,
                                   highlightbackground=color2,
                                   highlightcolor='white',
                                   font=('monospace',10),
                                   fg='black',
                                   cursor='hand2')
        self.down_button.pack(padx=20, pady=10)

        self.status_label = tk.Label(root, text="", padx=20, pady=10,bg=color2)
        self.status_label.pack()
        
        button = tk.Button(self.root, text="Restart",
                           command=self.Restart, 
                          background=color4,
                           foreground=color2,
                           activebackground=color2,
                           activeforeground=color4,
                           highlightthickness=2,
                           highlightbackground=color2,
                           highlightcolor='white',
                           font=('monospace',8),
                           fg='black',
                           cursor='hand2')
        button.pack()
        
    def open_csv_file(self):
        file_path = "anonymized_data.csv"
        if file_path:
            self.display_csv_data(file_path)
    def save_in_csv_file(self):
            #-----------save result to csv file--------------------------------
            anonymization_data=pd.concat(self.result_partitions,ignore_index=True)
            anonymization_data=anonymization_data.sort_index()
            anonymization_data.to_csv('anonymized_data.csv',index=False)
            
   
        
    def Restart(self):
           self.root.destroy()
           root=Tk()
           Page1(root)
    def load_new(self):
      self.root.destroy()
      root=Tk()
      page5(root,self.result_partitions)
      
class page5:
    def __init__(self,root,result_partitions):
        self.root=root
        self.root.geometry('800x500+500+100')
        self.root.title('DataArmor')
        self.root.config(background='#BDE0FE')
        self.root.resizable(True,True)
        self.f1=Frame(self.root,background=color2)
        self.f1.pack()
        self.result_partitions=result_partitions
        button = tk.Button(self.f1, text="back",
                           command=self.load_new, 
                          background=color2,
                           foreground=color2,
                           activebackground=color2,
                           activeforeground=color4,
                           highlightthickness=2,
                           highlightbackground=color2,
                           highlightcolor='white',
                           font=('monospace',8),
                           fg='black',
                           cursor='hand2')
        button.pack()
        
        button = tk.Button(self.f1, text="Restart",
                           command=self.Restart, 
                          background=color2,
                           foreground=color2,
                           activebackground=color2,
                           activeforeground=color4,
                           highlightthickness=2,
                           highlightbackground=color2,
                           highlightcolor='white',
                           font=('monospace',8),
                           fg='black',
                           cursor='hand2')
        button.pack()
        self.status_label = tk.Label(self.root, text="", padx=20, pady=10,bg=color2)
        self.status_label.pack()
        self.status_label.config(text=f"Anonymized Data")
        self.vieew()
        
    
    def vieew(self):
            anonymization_data=pd.concat(self.result_partitions,ignore_index=True)
            anonymization_data=anonymization_data.sort_index()
            anonymization_data.to_csv('anonymiz_data.csv',index=False)
            self.f2=Frame(self.root,background=color2)
            self.f2.pack()
            file_path='anonymiz_data.csv'
            self.tree = ttk.Treeview(self.f2, show="headings", height=300)
            self.tree.pack(padx=2, pady=2, fill="both", expand=True)

            self.status_label = tk.Label(self.f2, text="", padx=20, pady=10,bg=color2)
            self.status_label.pack()
            tree=self.tree
            with open(file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                tree.delete(*tree.get_children())  # Clear the current data

                tree["columns"] = header
                for col in header:
                    tree.heading(col, text=col)
                    tree.column(col, width=100)

                for row in csv_reader:
                    tree.insert("", "end", values=row)
            
            os.remove('anonymiz_data.csv')
    
    def Restart(self):
           self.root.destroy()
           root=Tk()
           Page1(root)
    def load_new(self):
      self.f2.destroy()
      self.f1.destroy()
      page4(self.root,self.result_partitions)
#----------------------------------------------------
root=Tk()
ob=Page1(root)
root.mainloop()
