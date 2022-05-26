import time,datetime
from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

open_webinar_window=Tk()
open_webinar_window.title('ICSI WEBINAR')
open_webinar_window.geometry('475x239')
open_webinar_window.resizable(False,False)
date=str(datetime.date.today())
date=date.split('-')
date=date[::-1]
webinar_date=''
for i in date:
    webinar_date+=i
webinar_url='https://ecpl.live/icsi/'
webinar_url_with_date=webinar_url+webinar_date

memb_no_lbl=Label(open_webinar_window,text='Enter membership no.: ',font=('Comic Sans MS',14,'bold'),bg='blue',fg='yellow',bd=5,relief='groove').place(x=0,y=0,width=229,height=39)
memb_no=Entry(open_webinar_window,font=('Comic Sans MS',14,'bold'),bd=2,relief='groove')
memb_no.place(x=229,y=0,height=39)
memb_name_lbl=Label(open_webinar_window,text='Enter your name: ',font=('Comic Sans MS',14,'bold'),bg='blue',fg='yellow',bd=5,relief='groove').place(x=0,y=39,width=229,height=39)
memb_name=Entry(open_webinar_window,font=('Comic Sans MS',14,'bold'),bd=2,relief='groove')
memb_name.place(x=229,y=39,height=39)
memb_mail_lbl=Label(open_webinar_window,text='Enter your e-mail: ',font=('Comic Sans MS',14,'bold'),bg='blue',fg='yellow',bd=5,relief='groove').place(x=0,y=78,width=229,height=39)
memb_mail=Entry(open_webinar_window,font=('Comic Sans MS',14,'bold'),bd=2,relief='groove')
memb_mail.place(x=229,y=78,height=39)
memb_mob_lbl=Label(open_webinar_window,text='Enter your mobile no.: ',font=('Comic Sans MS',14,'bold'),bg='blue',fg='yellow',bd=5,relief='groove').place(x=0,y=117,width=229,height=39)
memb_mob=Entry(open_webinar_window,font=('Comic Sans MS',14,'bold'),bd=2,relief='groove')
memb_mob.place(x=229,y=117,height=39)

memb_no.insert(0,"A13275")
memb_name.insert(0,"RAJESH MITTAL")
memb_mail.insert(0,"OFFICE@CSMRA.COM")
memb_mob.insert(0,"9811262068")

def open_webinar_url():
    try:
        # Using Chrome to access web
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Open the website
        driver.get(webinar_url_with_date)

        membership_no = driver.find_element(by=By.NAME, value="member_ship_no")
        membership_no.clear()
        membership_no.send_keys(memb_no.upper())#"A13275"
        
        member_name = driver.find_element(by=By.NAME, value="name")
        member_name.clear()
        member_name.send_keys(memb_name.upper())#"RAJESH MITTAL"

        member_email = driver.find_element(by=By.NAME, value="email")
        member_email.clear()
        member_email.send_keys(memb_mail.upper())#"OFFICE@CSMRA.COM"

        member_mob_no = driver.find_element(by=By.NAME, value="mobile")
        member_mob_no.clear()
        member_mob_no.send_keys(memb_mob.upper())#"9811262068"

        driver.find_element(by=By.NAME, value="login").click()

        time.sleep(5)
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    except exceptions.NoSuchElementException:
        driver.quit()
        messagebox.showerror('ERROR','No webinar is available today.....!!!')
    except Exception as e:
        err='Exception (ERROR): \n'+str(e)
        messagebox.showerror('ERROR',err)

open_webinar_button=Button(open_webinar_window,text='Click to open ICSI Webinar...!!',command=open_webinar_url,font=('Comic Sans MS',20,'bold'),bg='blue',fg='yellow',bd=10,relief='groove')
open_webinar_button.place(x=0,y=156,width=475)

open_webinar_window.mainloop()
