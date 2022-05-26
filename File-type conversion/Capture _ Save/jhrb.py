import time
from psutil import *
from plyer import notification
from pyautogui import *
from tkinter import *
from tkinter import filedialog

capture_screen=Tk()
capture_screen.title('Capture your screen')
capture_screen.geometry('376x83')
capture_screen.attributes('-topmost', True)
capture_screen.resizable(False,False)

img_save_file_types=[('Portable Network Graphics (.PNG) FILES','.png'),('Joint Photographic Experts Group (.JPG) FILES','.jpg'),('Bitmap Image (.BMP) FILES','.bmp'),
                     ('Joint Photographic Experts Group (.JPEG) FILES','.jpeg'),('Portable Document Format (.PDF) FILES','.pdf'),('All Files','.*')]

def take_scrshot():
    capture_screen.state('iconic')
    time.sleep(1)
    scrshot=screenshot()
    with open('scrshot_no_file.txt','r') as scrshot_no_file:
        scrshot_no=scrshot_no_file.read()
    file_name='Screenshot_'+scrshot_no
    file_path=filedialog.asksaveasfilename(initialfile=file_name,defaultextension='.png',filetypes=img_save_file_types)
    scrshot.save(file_path)
    capture_screen.state('normal')
    notification.notify(title='Screenshot Saved',message='Screenshot saved at '+file_path,timeout=100,toast=True)
    with open('scrshot_no_file.txt','w') as scrshot_no_file:
        scrshot_no_file.write(str(int(scrshot_no)+1))

scrshot_button=Button(capture_screen,text='Full-Screen Screenshot !!', command=take_scrshot,bg='blue',fg='yellow',relief='groove',font=('Comic Sans MS',20,'bold'),bd=10)
scrshot_button.place(x=0,y=0)
capture_screen.bind('<Alt-X>',take_scrshot)
capture_screen.mainloop()
