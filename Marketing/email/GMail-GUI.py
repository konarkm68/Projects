from tkinter import *#Toplevel,Button,Label
from gmail import Message
import time,gmail

mail_app=Tk()
mail_app.title('NUVISTA e- SOLUTIONS | GMAIL...')
mail_app.config(background='blue')
mail_app.geometry('595x213')

def send_bill():
    current_date=time.strftime(' %d-%m-%Y ') 
    mail_text=f'''<h2>Hello, With reference to your shopping at ASK BILLING S/W on {current_date},
    we have sent you the BILL attached with this mail to confirm your BILL and the payment against it...</h2>

    <h3>Thanks,
    Team Nuvista e-Solutions</h3>'''
    attachment='GMail-GUI.py'##invoice_file_path+'.pdf'
    gmail_entry= gmail.GMail(f'ASK BILLING S/W <{from_mail.get()}>',from_password.get())
    msg = Message(f'Re: e-Bill for your shopping with ASK BILLING S/W dated {current_date}',to=to_mail.get(),html=mail_text,attachments=[attachment])
    gmail_entry.send(msg)

def reset_entries():
    from_mail.delete(0,'end')
    from_password.delete(0,'end')
    to_mail.delete(0,'end')

Label(mail_app, text="Sender's email",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=0)
from_mail= Entry(mail_app,width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
from_mail.place(x=253,y=0,height=36)

Label(mail_app, text="Sender's email password: ",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=41)
from_password= Entry(mail_app,show="*",width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
from_password.place(x=253,y=41,height=36)

Label(mail_app, text="Receiver's email",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=90)
to_mail= Entry(mail_app,width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
to_mail.place(x=253,y=90,height=36)

Button(mail_app, text="SEND e- BILL", command=send_bill,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE).place(x=0, y=150,width=295)
Button(mail_app, text="RESET ENTRIES", command=reset_entries,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE).place(x=299,y=150,width=297)

mail_app.mainloop()
