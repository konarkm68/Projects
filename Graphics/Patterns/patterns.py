import time

'''
    MENU FOR PATTERNS

    Pyramid Patterns
        1. Pyramid 
        2. Hollow Pyramid
        3. Inverted Pyramid
        4. Hollow Inverted Pyramid
    Arrow Patterns
        5. Left to Right Arrow
            6. Hollow Left to Right Arrow
            7. Left to Right Arrow 1
            8. Hollow Left to Right Arrow 1
            9. Left to Right Arrow 2
            10. Hollow Left to Right Arrow 2
        11. Right to Left Arrow
            12. Hollow Right to Left Arrow
            13. Right to Left Arrow 1
            14. Hollow Right to Left Arrow 1
            15. Right to Left Arrow 2
            16. Hollow Right to Left Arrow 2
    Shapes Patterns
        17. Square
            18. Hollow Square
            19. Hollow Square with Diagonal
        20. Diamond
            21. Hollow Diamond
            22. Hollow Diamond with Diagonal
        23. Parallelogram
            24. Hollow Parallelogram
            25. Hollow Parallelogram with Diagonal
        26. Heart
            27. Hollow Heart
            28. Hollow Heart with Diagonal Arrow
'''

num = int(input("Enter no. of lines to draw (>=5): ")) ## print instruction to input no. of lines
print() ## print new line

## 1. Pyramid
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def pyramid(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            print("* ", end='')
        print()
    print()
pyramid(num)

## 2. Hollow Pyramid
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def pyramid_hollow(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if j==0 or j==2*i or i==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
pyramid_hollow(num)

## 3. Inverted Pyramid
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def pyramid_inverted(num):
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            print("* ", end='')
        print()
    print()
pyramid_inverted(num)

## 4. Hollow Inverted Pyramid
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def pyramid_inverted_hollow(num):
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if j==0 or j==2*i or i==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
pyramid_inverted_hollow(num)

## 5. Left to Right Arrow
## Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def L2R_arrow(num):
    for i in range(num-1):
        for j in range(i+1):
            print("* ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(i+1):
            print("* ", end='')
        print()
    print()
L2R_arrow(num)

## 6. Hollow Left to Right Arrow
## Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def L2R_arrow_hollow(num):
    for i in range(num-1):
        for j in range(i+1):
            if j==0 or j==i:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(i+1):
            if j==0 or j==i:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
L2R_arrow_hollow(num)

## 7. Left to Right Arrow 1
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars
##           3. Prdef new line

def L2R_arrow_1(num):
    for i in range(num):
        for j in range(i+1):
            print("* ", end='')
        print()
    print()
L2R_arrow_1(num)

## 8. Hollow Left to Right Arrow 1
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def L2R_arrow_1_hollow(num):
    for i in range(num):
        for j in range(i+1):
            if j==0 or j==i or i==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
L2R_arrow_1_hollow(num)

## 9. Left to Right Arrow 2
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars 
##           3. Prdef new line

def L2R_arrow_2(num):
    for i in range(num-1,-1,-1):
        for j in range(i+1):
            print("* ", end='')
        print() 
    print()
L2R_arrow_2(num)

## 10. Hollow Left to Right Arrow 2
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def L2R_arrow_2_hollow(num):
    for i in range(num-1,-1,-1):
        for j in range(i+1):
            if j==0 or j==i or i==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
L2R_arrow_2_hollow(num) 

## 11. Right to Left Arrow
## Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def R2L_arrow(num):
    for  i in range(num-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            print("* ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            print("* ", end='')
        print()
    print()
R2L_arrow(num)  

## 12. Hollow Right to Left Arrow
## Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def R2L_arrow_hollow(num):
    for i in range(num-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            if(j==0 or j==i):
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            if(j==0 or j==i):
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
R2L_arrow_hollow(num)

## 13. Right to Left Arrow 1
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def R2L_arrow_1(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            print("* ", end='')
        print()
    print()
R2L_arrow_1(num)

## 14. Hollow Right to Left Arrow 1
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def R2L_arrow_1_hollow(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            if(j==0 or j==i or i==num-1):
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
R2L_arrow_1_hollow(num)

## 15. Right to Left Arrow 2
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def R2L_arrow_2(num):
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            print("* ", end='')
        print()
    print()
R2L_arrow_2(num)

## 16. Hollow Right to Left Arrow 2
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def R2L_arrow_2_hollow(num):
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(i+1):
            if j==0 or j==i or i==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
R2L_arrow_2_hollow(num)

## 17. Square
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars 
##           3. Prdef new line

def square(num):
    for i in range(num):
        for j in range(num):
            print("* ", end='')
        print()
    print()
square(num)

## 18. Hollow Square
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def square_hollow(num):
    for i in range(num):
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
square_hollow(num)

## 19. Hollow Square with Diagonal
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def square_hollow_diagonal(num):
    for i in range(num):
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 or i==j or i+j==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
square_hollow_diagonal(num)

## 20. Diamond
## Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def diamond(num):
    for i in range(num-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            print("* ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            print("* ", end='')
        print()
    print()
diamond(num)

## 21. Hollow Diamond
## Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def diamond_hollow(num):
    for i in range(num-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if j==0 or j==2*i:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if j==0 or j==2*i:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
diamond_hollow(num)

## 22. Hollow Diamond with Diagonal
## Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
##           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
##           3. Prdef new line

def diamond_hollow_diagonal(num):
    for i in range(num-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if i==0 or j==0 or j==2*i or i==num-1 or i==j:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    for i in range(num-1,-1,-1):
        for j in range(num-i):
            print("  ", end='')
        for j in range(2*i+1):
            if i==0 or j==0 or j==2*i or i==num-1 or i==j:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
diamond_hollow_diagonal(num)

## 23. Parallelogram
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def parallelogram(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(num):
            print("* ", end='')
        print()
    print()
parallelogram(num)

## 24. Hollow Parallelogram
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def parallelogram_hollow(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
parallelogram_hollow(num)

## 25. Hollow Parallelogram with Diagonal
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loops for no. of stars and spaces
##           3. Prdef new line

def parallelogram_hollow_diagonal(num):
    for i in range(num):
        for j in range(num-i):
            print("  ", end='')
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 or i==j or i+j==num-1:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
    print()
parallelogram_hollow_diagonal(num)  

## 26. Heart
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def heart():
    
    num = 5

    for i in range(num+1):
        for j in range(num+2):
            if (i==0 and j==0) or (i==0 and j==num+1) or (i==0 and j==(num+1)/2):
                print("  ", end='')
            elif i==num-2 and j<((num+1)/2)-2 or i==num-2 and j>((num+1)/2)+2:
                print("  ", end='')
            elif i==num-1 and j<((num+1)/2)-1 or i==num-1 and j>((num+1)/2)+1:
                print("  ", end='')
            elif i==num and j!=((num+1)/2):
                print("  ", end='')
            else:
                print("* ", end='')
        print()
    print()
heart()

## 27. Hollow Heart
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def heart_hollow():
    
    num = 5

    for i in range(num+1):
        for j in range(num+2):
            if (i==0 and j==0) or (i==0 and j==num+1) or (i==0 and j==(num+1)/2):
                print("  ", end='')
            elif i==1 and j==(num+1)/2:
                print("* ", end='')
            elif i==1 and j!=0 and i==1 and j!=num+1 or i==2 and j!=0 and i==2 and j!=num+1:
                print("  ", end='')
            elif i==num-2 and j!=3-2 and i==num-2 and j!=3+2:
                print("  ", end='')
            elif i==num-1 and j!=3-1 and i==num-1 and j!=3+1:
                print("  ", end='')
            elif i==num and j!=((num+1)/2):
                print("  ", end='')
            else:
                print("* ", end='')
        print()
    print()
heart_hollow()

## 28. Hollow Heart with Diagonal Arrow
## Logic? -- 1. Outer loop for no. of lines
##           2. Inner loop for no. of stars and spaces
##           3. Prdef new line

def heart_hollow_diagonal_arrow():
    
    num = 5

    for i in range(num+1):
        for j in range(num+2):
            if (i==0 and j==0) or (i==0 and j==(num+1)/2):
                print("  ", end='')
            elif i+j==num+1:
                print("* ", end='')
            elif i==1 and j==(num+1)/2:
                print("* ", end='')
            elif i==1 and j!=0 and i==1 and j!=num+1 or i==2 and j!=0 and i==2 and j!=num+1:
                print("  ", end='')
            elif i==num-2 and j!=3-2 and i==num-2 and j!=3+2:
                print("  ", end='')
            elif i==num-1 and j!=3-1 and i==num-1 and j!=3+1:
                print("  ", end='')
            elif i==num and j!=((num+1)/2):
                print("  ", end='')
            else:
                print("* ", end='')
        print()
    print()
heart_hollow_diagonal_arrow()

#time.sleep(100) ## wait for 100 seconds