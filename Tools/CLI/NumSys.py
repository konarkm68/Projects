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

    def BinaryOperations():
        print("""\n\t    2. Binary Operations
\t        a. Binary Addition
\t        b. Binary Subtraction
\t        c. EXIT!""")

        choice = input(f"Enter your choice: {Fore.YELLOW}")
        print(f"{Style.RESET_ALL}", end="")

        def BinaryAdd():
            print("\n\t    2. a. Binary Addition\n")

            num = int(input(f"{Fore.YELLOW}Enter the number of binary-numbers to add: "))
            
            for i in range(num):
                bin_num = input(f"{Style.RESET_ALL}Enter Binary-Number #{i+1}: {Fore.YELLOW}")
                if i == 0:
                    bin_sum = int(bin_num, 2)
                else:
                    bin_sum += int(bin_num, 2)

            print(f"{Style.RESET_ALL}\n{Fore.BLUE}The Binary-Sum is:  {bin(bin_sum)[2:]}")
            print(f"{Fore.BLUE}The Decimal-Sum is: {bin_sum:d}")

        def BinarySub():
            print("\n\t    2. b. Binary Subtraction\n")

            bin_num1 = input(f"Enter Binary-Number #1: {Fore.YELLOW}")
            bin_num2 = input(f"{Style.RESET_ALL}Enter Binary-Number #2: {Fore.YELLOW}")

            bin_sum = int(bin_num1, 2) - int(bin_num2, 2)

            print(f"{Style.RESET_ALL}\n{Fore.BLUE}The Binary-Difference is:  {bin(bin_sum)[2:]}")
            print(f"{Fore.BLUE}The Decimal-Difference is: {bin_sum:d}")
        
        match choice:
            case 'a' | 'A':
                BinaryAdd()
            case 'b' | 'B':
                BinarySub()
            case 'c' | 'C':
                exit()
            case _:
                print(f"\n\t{Fore.RED}Invalid Choice")

    def complement():
        print("\n\t    3. Complement\n")

        bits = int(input(f"Enter the number of bits (including signed-bit): {Fore.YELLOW}"))
        bits_mask = int(bin(2**bits - 1)[2:], 2)

        num = int(input(f"{Style.RESET_ALL}Enter the ({bits}-bit-Binary-Number) = (1-signed-bit + {bits-1}-Binary-Number-bits): {Fore.YELLOW}"), 2)

        def ones_complement(num, bits):
            return bin(num ^ bits_mask)[2:]

        def twos_complement(num, bits):
            ones_comp = ones_complement(num, bits)
            return bin(int(ones_comp, 2) + 0b1)[2:]
        
        sign = '+'
        bin_ss = 2

        ones_comp = ones_complement(num, bits)
        ones_comp1 = -int(bin(num)[bin_ss:], 2)-1
        ones_comp2 = ~int(bin(num)[bin_ss:], 2) 
        
        twos_comp = twos_complement(num, bits) 
        twos_comp1 = -int(bin(num)[bin_ss:], 2)  
        twos_comp2 = ~int(bin(num)[bin_ss:], 2)+1  

        print(f"\n{Fore.BLUE}The Decimal-Number is: ({sign}){int(bin(num)[bin_ss:], 2):d}")
        print(f"""{Fore.BLUE}The 1's Complement is: 
\tBinary : {ones_comp} 
\tDecimal: Actual: {int(ones_comp, 2):d} Considered as: {ones_comp1:d} OR {ones_comp2:d}""")
        print(f"""{Fore.BLUE}The 2's Complement is: 
\tBinary : {twos_comp} 
\tDecimal: Actual: {int(twos_comp, 2):d} Considered as: {twos_comp1:d} OR {twos_comp2:d}""")

    def main():
        try:
            print("""
            Welcome to the Number-System Calculator!\n
    1. Number-System Conversion
    2. Operations on Binary-Numbers
    3. Find Complements - 1's & 2's
    4. EXIT!    """)

            operation_choice = int(input(f"Enter your choice: {Fore.YELLOW}"))
            print(f"{Style.RESET_ALL}", end="")

            match operation_choice:
                case 1:
                    NumSys.NumSys_converter()
                case 2:
                    NumSys.BinaryOperations()
                case 3:
                    NumSys.complement()
                case 4:
                    exit()
                case _:
                    print(f"\n\t{Fore.RED}Invalid Choice")
        except Exception as e:
            print(f"""\n\t{Fore.RED}Exception: {e}\n\tPress <Control> + <C> to exit !!{Style.RESET_ALL}""") 

    def __init__(self):
        colorama_init(autoreset=True)
        while True:
            NumSys.main()

if __name__=="__main__":
    NumSys()
#   NumSys.NumSys() ## usage when importing this module