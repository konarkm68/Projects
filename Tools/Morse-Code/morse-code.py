from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class morse_code:
    def __init__(self):
        colorama_init(autoreset=True)
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
            print(f"{Fore.BLUE}{self.codec[i]}", end='   ')
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
            print(f"{Fore.BLUE}{key[val.index(j)]}", end='')
        print()
        print()

    def menu(self):
        print("1. Message to Morse Code")
        print("2. Morse Code to Message")
        print("3. Exit \n")
        choice=int(input(f"Enter your choice: {Fore.YELLOW}"))
        if choice == 1:
            msg_code = input(f"\nEnter the message: {Fore.YELLOW}")
            self.msg2code(msg_code)
        elif choice == 2:
            msg_code = input(f"\nEnter the Morse Code: {Fore.YELLOW}")
            self.code2msg(msg_code)
        elif choice == 3:
            exit()
        else:
            print("Invalid Choice!")

    def main(self):
        while True:
            self.menu()

if __name__=="__main__":
    morse_code().main()