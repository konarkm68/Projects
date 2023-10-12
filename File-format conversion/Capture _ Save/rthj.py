import numpy as np
from tkinter import Tk,filedialog
from PIL import Image, ImageSequence, TiffImagePlugin

images = []
img_listing=filedialog.askopenfilenames()
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
