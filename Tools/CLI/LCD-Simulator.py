class LCDsimulator():
    ## Making functions for each line of the digit
    ## Matching the digit with the input one-by-one and printing the corresponding digit in LED display format using star(*)

    def Line1(i):
        #print('         '*digit_index,end='')
        match i:
            case '0': print('* * * ') 
            case '1': print('    * ')
            case '2': print('* * * ')
            case '3': print('* * * ')
            case '4': print('*   * ')
            case '5': print('* * * ')
            case '6': print('* * * ')
            case '7': print('* * * ')
            case '8': print('* * * ')
            case '9': print('* * * ')

    def Line2(i):
        #print('         '*digit_index,end='')
        match i:
            case '0': print('*   * ')
            case '1': print('    * ')
            case '2': print('    * ')
            case '3': print('    * ')
            case '4': print('*   * ')
            case '5': print('*     ')
            case '6': print('*     ')
            case '7': print('    * ')
            case '8': print('*   * ')
            case '9': print('*   * ')

    def Line3(i):
        #print('         '*digit_index,end='')
        match i:
            case '0': print('*   * ')
            case '1': print('    * ')
            case '2': print('* * * ')
            case '3': print('* * * ')
            case '4': print('* * * ')
            case '5': print('* * * ')
            case '6': print('* * * ')
            case '7': print('    * ')
            case '8': print('* * * ')
            case '9': print('* * * ')

    def Line4(i):
        #print('         '*digit_index,end='')
        match i:
            case '0': print('*   * ')
            case '1': print('    * ')
            case '2': print('*     ')
            case '3': print('    * ')
            case '4': print('    * ')
            case '5': print('    * ')
            case '6': print('*   * ')
            case '7': print('    * ')
            case '8': print('*   * ')
            case '9': print('    * ')

    def Line5(i):
        #print('         '*digit_index,end='')
        match i:
            case '0': print('* * * ')
            case '1': print('    * ')
            case '2': print('* * * ')
            case '3': print('* * * ')
            case '4': print('    * ')
            case '5': print('* * * ')
            case '6': print('* * * ')
            case '7': print('    * ')
            case '8': print('* * * ')
            case '9': print('* * * ')
        print('\n')

    def main(i):
        ## Calling the functions Line1() to Line5()
        LCDsimulator.Line1(i)
        LCDsimulator.Line2(i)
        LCDsimulator.Line3(i)
        LCDsimulator.Line4(i)
        LCDsimulator.Line5(i)

    def __init__(self):
        digit=input('Enter a digit (0-9): ') ## Taking input from user
        print('\n')
        ## Checking condition for invalid input and calling the function LCDsimulator() if the input is valid
        for i in digit:
            if i not in '0123456789':
                print('Invalid Input...!!')
                break
            else:
                LCDsimulator.main(i)

if __name__ == '__main__':
    LCDsimulator()
