import random,pywhatkit,datetime,phonenumbers

x=datetime.datetime.now()

def random_phone_num_generator():
    first = str(91)
    second = str(random.randint(66666, 99998)).zfill(5)
    last = (str(random.randint(1, 99998)).zfill(5))

    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)

n = int(input("How much mobile numbers do you want to generate: "))

whats_app_message='''We are looking for freshers for computer-related jobs & 10th-pass students who are interested to get admission into ITI...If anybody is interested, please call or WhatsApp @ +91-89201-88073 or visit https://cc.mmeduport.com or write a mail at info@mmeduport.com'''

for i in range(0, n):
    print('+'+random_phone_num_generator())
    pywhatkit.sendwhatmsg('+'+random_phone_num_generator(),whats_app_message,x.hour,x.minute+2)
