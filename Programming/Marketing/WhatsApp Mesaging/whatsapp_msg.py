import datetime
import pywhatkit

mob_no=input('Enter Mobile No. of the person you want to WhatsApp: ')
message=input('Enter message to send to the above person: ')

x = datetime.datetime.now()

print('\nYour message',message,'to',mob_no,'will be sent at',x.hour,':',x.minute+2)
pywhatkit.sendwhatmsg(mob_no,message,x.hour,x.minute+2)
