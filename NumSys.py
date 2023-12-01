from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class NumSys():
    def NumSys_converter():
        print("""
            1. Number-System Converter
        1. Decimal      ->  Binary-Number
                            Octal-Number
                            Hexa-Decimal--Number
        2. Binary       ->  Decimal-Number
                            Octal-Number
                            Hexa-Decimal--Number
        3. Octal        ->  Decimal-Number
                            Binary-Number
                            Hexa-Decimal--Number
        4. Hexa-Decimal ->  Decimal-Number
                            Binary-Number
                            Octal-Number
        5. Exit    """)
        choice = int(input(f"Enter your choice: {Fore.YELLOW}"))
        print(f"{Style.RESET_ALL}")
        match choice:
            case 1:
                num = int(input(f"Enter the Decimal-Number{':':>4} {Fore.YELLOW}"), 10)
                print(f"{Fore.BLUE}The Binary-Number is{':':>8} {num:b}")                  # bin(num)[2:]
                print(f"{Fore.BLUE}The Octal-Number is{':':>9} {num:o}")                   # oct(num)[2:]
                print(f"{Fore.BLUE}The Hexa-Decimal--Number is{':':0} {num:x} OR {num:X}") # hex(num)[2:]
            case 2:
                num = int(input(f"Enter the Binary-Number{':':>5} {Fore.YELLOW}"), 2)
                print(f"{Fore.BLUE}The Decimal-Number is{':':>7} {num:d}")
                print(f"{Fore.BLUE}The Octal-Number is{':':>9} {num:o}")
                print(f"{Fore.BLUE}The Hexa-Decimal--Number is{':':0} {num:x} OR {num:X}")
            case 3:
                num = int(input(f"Enter the Octal-Number{':':>6} {Fore.YELLOW}"), 8)
                print(f"{Fore.BLUE}The Decimal-Number is{':':>7} {num:d}")
                print(f"{Fore.BLUE}The Binary-Number is{':':>8} {num:b}")
                print(f"{Fore.BLUE}The Hexa-Decimal--Number is{':':0} {num:x} OR {num:X}")
            case 4:
                num = int(input(f"Enter the Hexa-Decimal--Number{':':0} {Fore.YELLOW}"), 16)
                print(f"{Fore.BLUE}The Decimal-Number is{':':>10} {num:d}")
                print(f"{Fore.BLUE}The Binary-Number is{':':>11} {num:b}")
                print(f"{Fore.BLUE}The Octal-Number is{':':>12} {num:o}")
            case 5:
                exit()
            case _:
                print(f"\t{Fore.RED}Invalid Choice")

    def complement():
        print("\n\t    2. Complement")
        num = int(input(f"\nEnter the Binary-Number: {Fore.YELLOW}"), 2)
        print(f"{Fore.BLUE}The 1's Complement is: \n\tBinary : {(~num):b} \n\tDecimal: {(~num):d}")
        print(f"{Fore.BLUE}The 2's Complement is: \n\tBinary : {(~num + 1):b} \n\tDecimal: {(~num + 1):d}")

    def main():
        try:
            print("""\nWelcome to the Number-System Calculator!

    1. Number-System Conversion
    2. Complement 
    3. Exit    """)
            operation_choice = int(input(f"Enter your choice: {Fore.YELLOW}"))
            print(f"{Style.RESET_ALL}", end="")
            match operation_choice:
                case 1:
                    NumSys.NumSys_converter()
                case 2:
                    NumSys.complement()
                case 3:
                    exit()
                case _:
                    print(f"\n\t{Fore.RED}Invalid Choice")
        except Exception as e:
            print(f"""\n\t{Fore.RED}Exception: {e}
            Press <Control> + <C> to exit !!""") 

    def __init__(self):
        colorama_init(autoreset=True)
        while True:
            NumSys.main()

if __name__=="__main__":
    NumSys()
#   NumSys.NumSys() ## usage when importing this module