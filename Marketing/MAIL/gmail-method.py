import gmail
from gmail import *

gmail = gmail.GMail('Konark Mittal <info.kmittal@gmail.com>','kmittal2068')
msg = Message('Test Message',to='info.kmittal@gmail.com',text="Hello",html="<b>Hello</b>",attachments=['GMail-GUI.py'])
gmail.send(msg)
