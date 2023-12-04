class morse_code:
    def __init__(self):
        self.codec={
        'A':'.-',   'B':'-...', 'C':'-.-.', 'D':'-..',  'E':'.',   'F':'..-.',
        'G':'--.',  'H':'....', 'I':'..',   'J':'.---', 'K':'-.-', 'L':'.-..',
        'M':'--',   'N':'-.',   'O':'---',  'P':'.--.', 'Q':'--.-','R':'.-.',
        'S':'...',  'T':'-',    'U':'..-',  'V':'...-', 'W':'.--', 'X':'-..-',
        'Y':'-.--', 'Z':'--..', 
        
        ' ':'       ',

        '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
        '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',

        ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
        '(':'-.--.',  ')':'-.--.-', '':'[', '':']'}

    def msg2code(self, msg_code):
        msg_code = msg_code.upper()
        print()
        for i in msg_code:
            print(self.codec[i], end='   ')
        print()
        print()

    def code2msg(self, msg_code):
        key=list(self.codec.keys())
        val=list(self.codec.values())
        msg_code=msg_code.split("\t")
        msg_code_new=''
        for morse_code in msg_code:
            msg_code_new += morse_code
        msg_code_new=str(msg_code_new.split("\t"))
        print()
        for j in msg_code:
            print(key[val.index(j)], end='')
        print()
        print()

    def menu(self):
        print("1. Message to Morse Code")
        print("2. Morse Code to Message \n")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            msg_code = input("\nEnter the message: ")
            self.msg2code(msg_code)
        elif choice == 2:
            msg_code = input("\nEnter the Morse Code: ")
            self.code2msg(msg_code)
        else:
            print("Invalid Choice!")

    def main(self):
        while True:
            self.menu()
            choice = input("Do you want to continue (Y/y // N/n): ")
            print()
            if choice == 'y' or choice == 'Y':
                continue
            else:
                break

if __name__=="__main__":
    morse_code().main()