import os
message=input('Enter text to convert to speech: ')
file=open('TTS.vbs','w')
with file as source:
    cmd='CreateObject("SAPI.Spvoice").Speak"'+message+'"'
    file.write(cmd)
os.system('TTS.vbs')
