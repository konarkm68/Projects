codec={'A':'.-',   'B':'-...', 'C':'-.-.', 'D':'-..',  'E':'.',   'F':'..-.',
       'G':'--.',  'H':'....', 'I':'..',   'J':'.---', 'K':'-.-', 'L':'.-..',
       'M':'--',   'N':'-.',   'O':'---',  'P':'.--.', 'Q':'--.-','R':'.-.',
       'S':'...',  'T':'-',    'U':'..-',  'V':'...-', 'W':'.--', 'X':'-..-',
       'Y':'-.--', 'Z':'--..', ' ':'       ',
       '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
       '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
       ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
       '(':'-.--.',  ')':'-.--.-', '':'[', '':']'}

msg2code=input('Enter message to convert into morse-code: ')
msg2code=msg2code.upper()
for i in msg2code:
    print(codec[i],end='   ')
print()
print()
code2msg=input('Enter morse-code to understand: ')
key=list(codec.keys())
val=list(codec.values())
code2msg=code2msg.split('   ')
code2msg_new=''
for morse_code in code2msg:
    code2msg_new+=morse_code
code2msg_new=str(code2msg_new.split('    '))

for j in code2msg:
    print(key[val.index(j)],end='')

