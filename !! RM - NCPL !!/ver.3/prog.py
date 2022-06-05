import os,csv,time
from os import path
from tkinter.ttk import Treeview
from tkinter import simpledialog,filedialog,messagebox
from tkinter import Tk,ttk,Label,Entry,Button,YES,GROOVE,BOTH,FLAT,SUNKEN,RIGHT,VERTICAL,Toplevel,Scrollbar

try:
    create_dir_app=Tk()
    create_dir_app.config(bg='blue')
    create_dir_app.geometry('400x100')
    create_dir_app.resizable(False,False)
    create_dir_app.title('RECORDS MAINTENANCE APPLICATION')
    try:
        create_dir_app.iconbitmap('.//RECORDS MAINTENANCE APP FILES//icon.ico')
    except Exception as e:
        err='Exception (ERROR): \n'+str(e)
        messagebox.showwarning('ERROR',err)
            
    rec_for_label=Label(create_dir_app,text='INVOICING:',bd=5,bg='blue',fg="white",font=("Comic Sans MS",14,"bold"),relief=GROOVE)
    rec_for_label.place(x=0,y=0,width=200)
    rec_for=ttk.Combobox(create_dir_app,font=('Comic Sans MS',14,'bold'),justify='center')
    rec_for['values']=('Not-Selected','CSC','DSC','PAN')
    rec_for.current(0)
    rec_for.place(x=200,y=0,width=200,height=39)
    rec_for.config(state='readonly')

    def get_master():
        try:
            file_location='.//RECORDS MAINTENANCE APP FILES//'+'LOCATION//'+rec_for.get()+'_location.txt'
        except Exception as e:
            err='Exception (ERROR): \n'+str(e)
            messagebox.showerror('ERROR',err)

        if rec_for.get()=='Not-Selected':
            messagebox.showwarning('ERROR...!!','Select invoicing first...!!')
        else:
            if path.exists('.//RECORDS MAINTENANCE APP FILES//serial.txt'):
                create_dir_app.geometry('400x310')
                
                dir_suffix_label=Label(create_dir_app,text='REFERENCE:',bd=5,bg='blue',fg="white",font=("Comic Sans MS",14,"bold"),relief=GROOVE)
                dir_suffix_label.place(x=0,y=100,width=200)

                def read_ref():
                    with open('.//RECORDS MAINTENANCE APP FILES//REFERENCES.csv','r') as ref_file:
                        global ref_list
                        ref_list=[]
                        read_ref_file=csv.reader(ref_file)
                        for ref_name in read_ref_file:
                            ref_list.append(ref_name)
                        ref_list=tuple(ref_list)
                    global source
                    source=ttk.Combobox(create_dir_app,font=('Comic Sans MS',14,'bold'),justify='center')
                    source['values']=ref_list
                    source.current(0)
                    source.place(x=200,y=100,width=200,height=39)
                    source.config(state='readonly')
                try:
                    read_ref()
                except Exception as e:
                    err='Exception (ERROR): \n'+str(e)
                    messagebox.showerror('ERROR',err)
                
                dir_suffix_label=Label(create_dir_app,text='Enter client-name:',bd=5,bg='blue',fg="white",font=("Comic Sans MS",14,"bold"),relief=GROOVE)
                dir_suffix_label.place(x=0,y=150,width=200)
                
                dir_suffix_name=Entry(create_dir_app,width=10,font=('Comic Sans MS',14,'bold'),justify='center',bd=2,relief=SUNKEN)
                dir_suffix_name.place(x=200,y=150,width=199,height=39)

                def add_ref():
                    try:
                        ref_name=simpledialog.askstring('INPUT','Please enter the new reference name: ',parent=create_dir_app)
                        ref_name=ref_name.upper()
                        if ref_name==None:
                            messagebox.showwarning('ERROR...!!',"Don't leave reference name blank...!!")
                        else:
                            ref_name_without_space=''
                            for i in ref_name:
                                if i==' ':
                                    ref_name_without_space+='.'
                                else:
                                    ref_name_without_space+=i
                            ref_name=ref_name_without_space
                            with open('.//RECORDS MAINTENANCE APP FILES//REFERENCES.csv','a',newline='') as ref_file:
                                append_ref=csv.writer(ref_file)
                                append_ref.writerow([ref_name])
                            read_ref()
                    except Exception as e:
                        err='Exception (ERROR): \n'+str(e)
                        messagebox.showerror('ERROR',err)
                add_ref_name=Button(create_dir_app,text='Add reference...',command=add_ref,bd=5,font=('Comic Sans MS',16,'bold'),bg='blue',fg='white')
                add_ref_name.place(x=10,y=50,width=199,height=39)
                
                def create_dir():
                    try:
                        if source.get()=='Not-Selected':
                            messagebox.showwarning('ERROR...!!','Select the reference first...!!')
                        else:
                            if dir_suffix_name.get()=='':
                                messagebox.showwarning('ERROR...!!',"Don't leave client-name blank...")
                            elif dir_suffix_name.get()!='' and dir_suffix_name.get()!=' ':
                                def create_dir():
                                    def create_dir_universal_method():
                                        with open('.//RECORDS MAINTENANCE APP FILES//serial.txt','r') as serial_file:
                                            serial=int(serial_file.read())
                                        
                                        dir_name=str(parent_dir)+'/'+rec_for.get()+'_'+str(serial)+' '+source.get()+' '+dir_suffix_name.get().upper()
                                        os.mkdir(dir_name)
                                        dir_create_msg=dir_name+' has been created.....'
                                        messagebox.showinfo('Folder created successfully !!',dir_create_msg)
                                        
                                        with open('.//RECORDS MAINTENANCE APP FILES//RECORDS-CONSOLIDATED.csv','a',newline='') as master_rec_file:
                                            master_file_writer=csv.writer(master_rec_file)
                                            record=serial,\
                                                    str(time.strftime(' %d-%m-%Y ')),\
                                                    source.get(),\
                                                    dir_suffix_name.get().upper(),\
                                                    rec_for.get()+'_'+str(serial),\
                                                    serial
                                            master_file_writer.writerow(record)
                                        
                                        with open('.//RECORDS MAINTENANCE APP FILES//serial.txt','w') as serial_file:
                                            serial_file.write(str((int(serial)+1)))
                                            
                                    if rec_for.get()=='PAN':
                                        try:
                                            create_dir_universal_method()
                                        except Exception as e:
                                            err='Exception (ERROR): \n'+str(e)
                                            messagebox.showerror('ERROR',err)
                                            
                                    else:
                                        try:
                                            create_dir_universal_method()                                  
                                        except Exception as e:
                                            err='Exception (ERROR): \n'+str(e)
                                            messagebox.showerror('ERROR',err)

                                if path.exists(file_location):
                                    dir_location_file=open(file_location,'r')
                                    parent_dir=str(dir_location_file.read())
                                    dir_location_file.close()
                                    create_dir()
                                else:
                                    parent_dir=filedialog.askdirectory(parent=create_dir_app,title='Select the folder in which you want to create folders: ')
                                    dir_location_file_writer=open(file_location,'w')
                                    parent_dir=dir_location_file_writer.write(str(parent_dir))
                                    dir_location_file_writer.close()
                                    dir_location_file_reader=open(file_location,'r')
                                    parent_dir=str(dir_location_file_reader.read())
                                    dir_location_file_reader.close()
                                    create_dir()        
                            else:
                                messagebox.showwarning('ERROR...!!','Please try again.....')
                    except Exception as e:
                        err='Exception (ERROR): \n'+str(e)
                        messagebox.showerror('ERROR',err)
                create_folder_button=Button(create_dir_app,text='Create Folder !!',command=create_dir,bd=5,font=('Comic Sans MS',16,'bold'),bg='blue',fg='white')
                create_folder_button.place(x=10,y=200,width=383,height=50)
                                    
                def master_tree_listing():
                    master_treelist=Toplevel()
                    master_treelist.geometry('1000x400')
                    master_treelist.resizable(False,False)
                    master_tree=Treeview(master_treelist,columns=('#0','#1','#2','#3','#4','#5'))
                    master_tree.heading('#0',text='S.NO.')
                    master_tree.heading('#1',text='DATE')
                    master_tree.heading('#2',text='REFERENCE')
                    master_tree.heading('#3',text='CLIENT-NAME')
                    master_tree.heading('#4',text='JOB-NO.')
                    master_tree.heading('#5',text='BILL-NO.')
                    master_tree.heading('#6',text='BALANCE')
                    master_tree.column('#0',anchor='center',width=60)
                    master_tree.column('#1',anchor='center',width=130)
                    master_tree.column('#2',anchor='center')
                    master_tree.column('#3',anchor='center')
                    master_tree.column('#4',anchor='center',width=80)
                    master_tree.column('#5',anchor='center',width=80)
                    master_tree.column('#6',anchor='center',width=130)
                    
                    master_tree.place(x=0,y=0,width=1000,height=400)

                    ttk.Style().configure('Treeview',font=('Courier New',14,'bold'),background='blue',foreground='white')
                    ttk.Style().configure('Treeview.Heading',font=('Courier New',14,'bold'))
                    
                    master_treelist_scrollbar=Scrollbar(master_tree,orient=VERTICAL,width=15,command=master_tree.yview)
                    master_treelist_scrollbar.pack(side=RIGHT,fill=BOTH)
                    master_tree.configure(yscrollcommand=master_treelist_scrollbar.set)

                    def master_update_tree():
                        try:
                            with open('.//RECORDS MAINTENANCE APP FILES//RECORDS-CONSOLIDATED.csv','r') as master_records_file:
                                master_records_reader=list(csv.DictReader(master_records_file))
                                for master_rec_row in master_records_reader[::-1]:
                                    master_sno_csv=master_rec_row['S.NO.']
                                    master_date_csv=master_rec_row['DATE']
                                    master_ref_csv=master_rec_row['REF.']
                                    master_name_csv=master_rec_row['NAME']
                                    master_job_no_csv=master_rec_row['JOB-NO.']
                                    master_bill_no_csv=master_rec_row['BILL-NO.']
                                    master_balance=master_rec_row['BALANCE']
                                    master_tree.insert('',0,text=master_sno_csv,values=(master_date_csv,master_ref_csv,master_name_csv,master_job_no_csv,master_bill_no_csv,master_balance))
                        except Exception as e:
                            master_treelist.destroy()
                            err='Exception (ERROR): \n'+str(e)
                            messagebox.showerror('ERROR',err)
                    master_update_tree()
                master_tree_list_button=Button(create_dir_app,text='VIEW CONSOLIDATED RECORDS',command=master_tree_listing,bd=5,font=('Comic Sans MS',16,'bold'),bg='blue',fg='white')
                master_tree_list_button.place(x=10,y=255,width=383,height=50)

            else:
                try:
                    file=open('.//RECORDS MAINTENANCE APP FILES//job_no.txt','w')
                    file.write('1')
                    file.close()
                except Exception as e:
                    err='Exception (ERROR): \n'+str(e)
                    messagebox.showerror('ERROR',err)
            
    get_master_button=Button(create_dir_app,text='Get Invoicing..',command=get_master,bd=5,font=('Comic Sans MS',16,'bold'),bg='blue',fg='white')
    get_master_button.place(x=220,y=50,height=39)
    
    create_dir_app.mainloop()

except Exception as e:
    err='RUNTIME ERROR: \n'+str(e)
    messagebox.showerror('ERROR',err)
