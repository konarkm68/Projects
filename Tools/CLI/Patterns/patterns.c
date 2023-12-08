# include <stdio.h> // for printf and scanf functions
# include <iostream> // for cout and cin functions
# include <windows.h> // for Sleep function

using namespace std; // using standard namespace

int main(void) // main function
{
    /*
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
    */

    unsigned short int num; // 0 to 65535

    printf("Enter no. of lines to draw (>=5): "); // print instruction to input no. of lines
    scanf("%u",&num); // input no. of lines
    printf("\n"); // print new line

    // 1. Pyramid
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int pyramid(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 2. Hollow Pyramid
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int pyramid_hollow(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if (j==0 || j==2*i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 3. Inverted Pyramid
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int pyramid_inverted(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }
    
    // 4. Hollow Inverted Pyramid
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int pyramid_inverted_hollow(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if (j==0 || j==2*i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }
    
    // 5. Left to Right Arrow
    // Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int L2R_arrow(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }  
        printf("\n");
    }

    // 6. Hollow Left to Right Arrow
    // Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int L2R_arrow_hollow(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }  
        printf("\n");
    }
    
    // 7. Left to Right Arrow 1
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars
    //           3. Print new line
    
    int L2R_arrow_1(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 8. Hollow Left to Right Arrow 1
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int L2R_arrow_1_hollow(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 9. Left to Right Arrow 2
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars 
    //           3. Print new line

    int L2R_arrow_2(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }  
        printf("\n");
    }

    // 10. Hollow Left to Right Arrow 2
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int L2R_arrow_2_hollow(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }  
        printf("\n");
    }
    
    // 11. Right to Left Arrow
    // Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int R2L_arrow(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 12. Hollow Right to Left Arrow
    // Logic? -- 1. Outer loop for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int R2L_arrow_hollow(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }
    
    // 13. Right to Left Arrow 1
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int R2L_arrow_1(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }
    
    // 14. Hollow Right to Left Arrow 1
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int R2L_arrow_1_hollow(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 15. Right to Left Arrow 2
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int R2L_arrow_2(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++)
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 16. Hollow Right to Left Arrow 2
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int R2L_arrow_2_hollow(num); 
    {
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++)
                printf("  ");
            for (unsigned short int j = 0; j <= i; j++) 
            {
                if(j==0 || j==i || i==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }
    
    // 17. Square
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars 
    //           3. Print new line

    int square(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num; j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 18. Hollow Square
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int square_hollow(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num; j++) 
            {
                if(i==0 || i==num-1 || j==0 || j==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        } 
        printf("\n");
    }

    // 19. Hollow Square with Diagonal
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int square_hollow_diagonal(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num; j++) 
            {
                if(i==0 || i==num-1 || j==0 || j==num-1 || i==j || i+j==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 20. Diamond
    // Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int diamond(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
                printf("* ");
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 21. Hollow Diamond
    // Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int diamond_hollow(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if(j==0 || j==2*i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if(j==0 || j==2*i)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 22. Hollow Diamond with Diagonal
    // Logic? -- 1. Outer loops for no. of lines - 1. Upper half, 2. Lower half
    //           2. Inner loops for no. of stars and spaces - 1. Upper half, 2. Lower half
    //           3. Print new line

    int diamond_hollow_diagonal(num); 
    {
        for (unsigned short int i = 0; i < num-1; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if(i==0 || j==0 || j==2*i || i==num-1 || i==j)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        for (short int i = num-1; i > -1; i--) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j <= (2*i); j++) 
            {
                if(i==0 || j==0 || j==2*i || i==num-1 || i==j)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    } 
    
    // 23. Parallelogram
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int parallelogram(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j < num; j++) 
                printf("* ");
            cout<<endl;
        }
        printf("\n");
    }

    // 24. Hollow Parallelogram
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int parallelogram_hollow(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j < num; j++) 
            {
                if(i==0 || i==num-1 || j==0 || j==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 25. Hollow Parallelogram with Diagonal
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loops for no. of stars and spaces
    //           3. Print new line

    int parallelogram_hollow_diagonal(num); 
    {
        for (unsigned short int i = 0; i < num; i++) 
        {
            for (unsigned short int j = 0; j < num-i; j++) 
                printf("  ");
            for (unsigned short int j = 0; j < num; j++) 
            {
                if(i==0 || i==num-1 || j==0 || j==num-1 || i==j || i+j==num-1)
                    printf("* ");
                else
                    printf("  ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 26. Heart
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int heart(void); 
    {
        
        unsigned short int num = 5;

        for (unsigned short int i = 0; i <= num; i++) 
        {
            for (unsigned short int j = 0; j <= num+1; j++) 
            {
                if ( (i==0 & j==0) || (i==0 & j==num+1) || (i==0 & j==(num+1)/2) )
                    printf("  ");
                else if ( i==num-2 & j<((num+1)/2)-2 || i==num-2 & j>((num+1)/2)+2 )
                    printf("  ");
                else if ( i==num-1 & j<((num+1)/2)-1 || i==num-1 & j>((num+1)/2)+1 )
                    printf("  ");
                else if ( i==num & j!=((num+1)/2) )
                    printf("  ");
                else
                    printf("* ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 27. Hollow Heart
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int heart_hollow(void); 
    {
       
        unsigned short int num = 5;

        for (unsigned short int i = 0; i <= num; i++) 
        {
            for (unsigned short int j = 0; j <= num+1; j++) 
            {
                if ( (i==0 & j==0) || (i==0 & j==num+1) || (i==0 & j==(num+1)/2) )
                    printf("  ");
                else if ( i==1 & j==(num+1)/2 )
                    printf("* ");
                else if ( i==1 & j!=0 && i==1 & j!=num+1 || i==2 & j!=0 && i==2 & j!=num+1 )
                    printf("  ");
                else if ( i==num-2 & j!=3-2 && i==num-2 & j!=3+2 )
                    printf("  ");
                else if ( i==num-1 & j!=3-1 && i==num-1 & j!=3+1 )
                    printf("  ");
                else if ( i==num & j!=((num+1)/2) )
                    printf("  ");
                else
                    printf("* ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    // 28. Hollow Heart with Diagonal Arrow
    // Logic? -- 1. Outer loop for no. of lines
    //           2. Inner loop for no. of stars and spaces
    //           3. Print new line

    int heart_hollow_diagonal_arrow(void); 
    {
       
        unsigned short int num = 5;

        for (unsigned short int i = 0; i <= num; i++) 
        {
            for (unsigned short int j = 0; j <= num+1; j++) 
            {
                if ( (i==0 & j==0) || (i==0 & j==(num+1)/2) )
                    printf("  ");
                else if ( i+j==num+1 )
                    printf("* ");
                else if ( i==1 & j==(num+1)/2 )
                    printf("* ");
                else if ( i==1 & j!=0 && i==1 & j!=num+1 || i==2 & j!=0 && i==2 & j!=num+1 )
                    printf("  ");
                else if ( i==num-2 & j!=3-2 && i==num-2 & j!=3+2 )
                    printf("  ");
                else if ( i==num-1 & j!=3-1 && i==num-1 & j!=3+1 )
                    printf("  ");
                else if ( i==num & j!=((num+1)/2) )
                    printf("  ");
                else
                    printf("* ");
            }
            cout<<endl;
        }
        printf("\n");
    }

    //Sleep(60000); // wait for 60 seconds

    return 0; // return 0 to operating system to indicate that program has successfully executed

} // end of main function