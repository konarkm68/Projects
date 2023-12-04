import ttg #ttg = truth-table-generator (Terminal: py -m pip install truth-table-generator)
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
#TT = Truth Table

class TT():
    def get_inputs(): 
        num = int(input(f"Enter number of inputs: {Fore.YELLOW}"))
        inputs = []
        for i in range(num):
            inputs.append(input(f"Enter input #{i+1}: {Fore.YELLOW}"))

        return inputs

    def get_LE(): #logical_expressions = Truth Table Logical Expressions
        print(f"\n{Style.RESET_ALL}Enter 'n' or 'N' to stop entering logical expressions. ")
        logical_expressions = []    
        while True:
            exp = input(f"{Fore.YELLOW}Enter logical expression: ")
            if exp == 'n' or exp == 'N':
                break
            else:
                logical_expressions.append(exp)  

        return logical_expressions
        
    def generator(inputs, logical_expressions):
        """ 
        ## Sample Truth Table Truths
        truths = ttg.Truths(['P', 'Q'], 
        #                          ['(~P)', '(~Q)', '(P and Q)', '(P or Q)', '(P xor Q)', '(P nor Q)', 
        #                           '(P nand Q)', '(P => Q)', '(P = Q)'], ints=True, ascending=True)
        """
        """
        ## Ascending or Descending
        AorDEsc = input("Ascending or Descending? (A/D): ")
        if AorDEsc == 'A' or AorDEsc == 'a':
            AorDEsc = True
        elif AorDEsc == 'D' or AorDEsc == 'd':
            AorDEsc = False
        else:
            print("Invalid input. Ascending is chosen by default.")
            AorDEsc = True
        """
        truths = ttg.Truths(inputs, logical_expressions, ints=True, ascending=True) #AorDEsc

        ## Print to console
        print(f"\n{Fore.BLUE}{truths.as_tabulate()}", '\n')
        TT_Val_index = len(inputs + logical_expressions) + 1 ## len(inputs + logical_expressions) = len(inputs) + len(logical_expressions)
        for i in range(1, TT_Val_index): 
            print(f"{Fore.BLUE}Valuation for Column #{i}: {truths.valuation(i)}")

        ## Write to file truth-table.txt
        data = truths.as_tabulate()
        with open('truth-table.txt', 'w') as file:
            file.write(data)
            file.write('\n')
            for i in range(1, TT_Val_index):
                file.write(f"\nValuation for Column #{i}: {truths.valuation(i)}")
            
    def main():
        print(f"\n\tWelcome to the Truth-Table Generator!\n")
        print("""        Operators and their representations

Negation              : 'not', '-', '~'
Logical Disjunction   : 'or'
Logical NOR           : 'nor'
Exclusive Disjunction : 'xor', '!='
Logical Conjunction   : 'and'
Logical NAND          : 'nand'
Material Implication  : '=>', 'implies'
Logical Bi-Conditional: '='

Note: 
1. Use parentheses! (Especially with the negation operator.)
2. Use the table above as reference. 
3. Although precedence rules are used, sometimes precedence between conjunction and disjunction is unspecified 
requiring to provide it explicitly in given formula with parentheses.        \n""")

        try:
            TT.generator(TT.get_inputs(), TT.get_LE())
        except Exception as e:
            print(f"""\n\t{Fore.RED}Exception: {e}\n\tPress <Control> + <C> to exit !!{Style.RESET_ALL}""") 

    def __init__(self):
        colorama_init(autoreset=True)
        while True:
            TT.main()

if __name__ == '__main__':
    TT()