from fpdf import FPDF
import os,time,shutil,numpy as np,PyPDF2
from tkinter import Tk,Button,filedialog
from PIL import Image, ImageGrab, ImageSequence, TiffImagePlugin

tiff_file_tk=Tk()
tiff_file_tk.geometry('695x53')
tiff_file_tk.title('MULTIPLE IMAGES -----> ONE FILE')
tiff_file_tk.config(background='blue')
tiff_file_tk.attributes('-topmost', True)
tiff_file_tk.resizable(False,False)

def shot():
    if os.path.exists('tiff_file_scrshots'):
        with open('img_no_file.txt','r') as img_no_file:
            img_no=img_no_file.read()
        tiff_file_tk.state('iconic')
        time.sleep(1)
        scrshot=ImageGrab.grab()
        file_path='.//tiff_file_scrshots//Screenshot_'+str(img_no)+'.png'
        scrshot.save(file_path)
        with open('img_no_file.txt','w') as img_no_file:
            img_no=img_no_file.write(str(int(img_no)+1))
        tiff_file_tk.state('normal')
    else:
        os.mkdir('tiff_file_scrshots')
        shot()
        
def add_files():
    images = []
    img_listing=[os.path.join(r,file) for r,d,f in os.walk('tiff_file_scrshots') for file in f]
    def add_to_tiff_file():
        for img in list(img_listing):
            images.append(np.asarray(Image.open(img)))
        image_list = []	
        for image in images:
            image_list.append(Image.fromarray(image))

        frames = []
        for i, frame in enumerate(image_list):
            info = TiffImagePlugin.ImageFileDirectory()
            frame.encoderinfo = {'tiffinfo': info}
            frames.append(frame)

        multi_img_one_file=filedialog.asksaveasfilename(defaultextension='.tiff',filetypes=[('Tag Image File Format (TIFF) Files','.tiff')])   
        with open(multi_img_one_file, "w+b") as fp:
            with TiffImagePlugin.AppendingTiffWriter(fp) as tf:
                for frame in frames:
                    frame.encoderconfig = ()
                    TiffImagePlugin._save(frame, tf,multi_img_one_file)
                    tf.newFrame()
        shutil.rmtree('tiff_file_scrshots')
        with open('img_no_file.txt','w') as img_no_file:
            img_no_file.write('1')
            
    def add_to_pdf_file():
        pdf_list=[]
        multi_img_one_file=filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[('Portale Document Format (PDF) Files','.pdf')])   
        for fname in img_listing:
            w=int((Image.open(fname).width)*2.54); h=int((Image.open(fname).height)*2.54)
            pdf=FPDF('P','mm',np.array([w,h]))
            pdf.add_page()
            pdf.image(fname,0,0,w,h)
            with open('pdf_no_file.txt','r') as pdf_no_file:
                pdf_no=pdf_no_file.read()
                pdf_file_no='PDF_'+pdf_no+'.pdf'
            pdf.output(pdf_file_no)
            pdf_list.append(pdf_file_no)
            with open('pdf_no_file.txt','w') as pdf_no_file:
                pdf_no_file.write(str(int(pdf_no)+1))
        pdfMerger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list: 
            pdfMerger.append(pdf)
        with open(multi_img_one_file, 'wb') as f: 
            pdfMerger.write(f)        

    shot_button=Button(tiff_file_tk,text='screenshot...',command=shot,bd=5,font=('Comic Sans MS',18,'bold'),bg='blue',fg='white')
    shot_button.place(x=0,y=0,height=51)

    add_files_button=Button(tiff_file_tk,text='Convert multiple scrshots ---> one file',command=add_to_pdf_file,bd=5,font=('Comic Sans MS',18,'bold'),bg='blue',fg='white')
    add_files_button.place(x=200,y=0,height=51)
add_files()
tiff_file_tk.mainloop()
