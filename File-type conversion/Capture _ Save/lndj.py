import keyboard
from PIL import ImageGrab
from tkinter import filedialog

img_save_file_types=[('Portable Network Graphics (.PNG) FILES','.png'),('Joint Photographic Experts Group (.JPG) FILES','.jpg'),('Bitmap Image (.BMP) FILES','.bmp'),
                     ('Joint Photographic Experts Group (.JPEG) FILES','.jpeg'),('Portable Document Format (.PDF) FILES','.pdf'),('All Files','.*')]

while True:
    if keyboard.is_pressed('Ctrl+F5'):
        scrshot=ImageGrab.grab()
        file_path=filedialog.asksaveasfilename(defaultextension='.png',filetypes=img_save_file_types)
        scrshot.save(file_path)
