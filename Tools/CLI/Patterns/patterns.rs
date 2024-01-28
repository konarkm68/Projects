// patterns.rs

use std::io; // import io module from standard library to use stdin() method
use std::io::Write; // import Write trait from io module from standard library to use flush() method

// Pyramid Patterns
fn pyramid(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {  
            print!("  ");
        }
        for _j in 0..(2*i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn pyramid_hollow(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn pyramid_inverted(num: u8) {
    for i in (0..num).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(2*i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn pyramid_inverted_hollow(num: u8) {
    for i in (0..num).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}

// Arrow Patterns
// 5. Left to Right Arrow
fn l2r(num: u8) {
    for i in 0..num {
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn l2r_hollow(num: u8) {
    for i in 0..num {
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn l2r1(num: u8) {
    for i in 0..num {
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn l2r2(num: u8) {
    for i in (0..num).rev() {
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn l2r1_hollow(num: u8) {
    for i in 0..num {
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn l2r2_hollow(num: u8) {
    for i in (0..num).rev() {
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
// 11. Right to Left Arrow
fn r2l(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn r2l_hollow(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn r2l1(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn r2l2(num: u8) {
    for i in (0..num).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn r2l1_hollow(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn r2l2_hollow(num: u8) {
    for i in (0..num).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(i+1) {
            if j == 0 || j == i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}

// Shapes Patterns
// 17. Square
fn sq(num: u8) {
    for _i in 0..num {
        for _j in 0..num {
            print!("* ");
        }
        println!();        
    }
}
fn sq_hollow(num: u8) {
    for i in 0..num {
        for j in 0..num {
            if j == 0 || j == num-1 || i == 0 || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn sq_hollow_diag(num: u8) {
    for i in 0..num {
        for j in 0..num {
            if j == 0 || j == num-1 || i == 0 || i == num-1 || i == j || i == num-j-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
// 20. Diamond
fn diamond(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(2*i+1) {
            print!("* ");
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..(2*i+1) {
            print!("* ");
        }
        println!();        
    }
}
fn diamond_hollow(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
fn diamond_hollow_diag(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i || i == num-1 || i == j {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
    for i in (0..num-1).rev() {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..(2*i+1) {
            if j == 0 || j == 2*i || i == num-1 || i == j{   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();        
    }
}
// 23. Parallellogram
fn llgm(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for _j in 0..num {
            print!("* ");
        }
        println!();     
    }
}
fn llgm_hollow(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..num {
            if j == 0 || j == num-1 || i == 0 || i == num-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();     
    }
}
fn llgm_hollow_diag(num: u8) {
    for i in 0..num {
        for _j in 0..(num-i) {
            print!("  ");
        }
        for j in 0..num {
            if j == 0 || j == num-1 || i == 0 || i == num-1 || i == j || i == num-j-1 {   
                print!("* ");
            }
            else {
                print!("  ");
            }
        }
        println!();       
    }
}
// 26. Heart
fn heart() {
    let num = 5;

    for i in 0..num+1 {
        for j in 0..num+2 {
            if (i == 0 && j == 0) || (i == 0 && j == num + 1) || (i == 0 && j == (num + 1) / 2) {
                print!("  ");
            }
            else if i == num - 2 && j < ((num + 1) / 2) - 2 || i == num - 2 && j > ((num + 1) / 2) + 2 {
                print!("  ");
            }
            else if i == num - 1 && j < ((num + 1) / 2) - 1 || i == num - 1 && j > ((num + 1) / 2) + 1 {
                print!("  ");
            }
            else if i == num && j != ((num + 1) / 2) {
                print!("  ");
            }
            else {
                print!("* ");
            }
        } 
        println!();       
    }
}
fn heart_hollow() {
    let num = 5;

    for i in 0..num+1 {
        for j in 0..num+2 {
            if (i == 0 && j == 0) || (i == 0 && j == num + 1) || (i == 0 && j == (num + 1) / 2) {
                print!("  ");
            }
            else if i == 1 && j == (num + 1) / 2 {
                print!("* ");
            }
            else if i == 1 && j != 0 && i == 1 && j != num + 1 || i == 2 && j != 0 && i == 2 && j != num + 1 {
                print!("  ");
            }
            else if i == num - 2 && j != 3 - 2 && i == num - 2 && j != 3 + 2 {
                print!("  ");
            }
            else if i == num - 1 && j != 3 - 1 && i == num - 1 && j != 3 + 1 {
                print!("  ");
            }
            else if i == num && j != ((num + 1) / 2) {
                print!("  ");
            }
            else {
                print!("* ");
            }
        } 
        println!();       
    }
}
fn heart_hollow_diag() {
    let num = 5;

    for i in 0..num+1 {
        for j in 0..num+2 {
            if (i == 0 && j == 0) || (i == 0 && j == (num + 1) / 2) {
                print!("  ");
            }
            else if i + j == num + 1 {
                print!("* ");
            }
            else if i == 1 && j == (num + 1) / 2 {
                print!("* ");
            }
            else if i == 1 && j != 0 && i == 1 && j != num + 1 || i == 2 && j != 0 && i == 2 && j != num + 1 {
                print!("  ");
            }
            else if i == num - 2 && j != 3 - 2 && i == num - 2 && j != 3 + 2 {
                print!("  ");
            }
            else if i == num - 1 && j != 3 - 1 && i == num - 1 && j != 3 + 1 {
                print!("  ");
            }
            else if i == num && j != ((num + 1) / 2) {
                print!("  ");
            }
            else {
                print!("* ");
            }
        } 
        println!();       
    }
}   

// Call Patterns' Functions
fn call_patterns(num: u8) {
    // Pyramid Patterns
    pyramid(num);
    println!();
    pyramid_hollow(num);
    println!();
    pyramid_inverted(num);
    println!();
    pyramid_inverted_hollow(num);
    println!();

    // Arrow Patterns
    // 5. Left to Right Arrow
    l2r(num);
    println!();
    l2r_hollow(num);
    println!();
    l2r1(num);
    println!();
    l2r1_hollow(num);
    println!();
    l2r2(num);
    println!();
    l2r2_hollow(num);
    println!();
    // 11. Right to Left Arrow
    r2l(num);
    println!();
    r2l_hollow(num);
    println!();
    r2l1(num);
    println!();
    r2l1_hollow(num);
    println!();
    r2l2(num);
    println!();
    r2l2_hollow(num);
    println!();

    // Shapes Patterns
    // 17. Square
    sq(num);
    println!();
    sq_hollow(num);
    println!();
    sq_hollow_diag(num);
    println!();
    // 20. Diamond
    diamond(num);
    println!();
    diamond_hollow(num);
    println!();
    diamond_hollow_diag(num);
    println!();
    // 23. Parallellogram
    llgm(num);
    println!();
    llgm_hollow(num);
    println!();
    llgm_hollow_diag(num);
    println!();
    // 26. Heart
    heart();
    println!();
    heart_hollow();
    println!();
    heart_hollow_diag();
    println!();
}

fn main() 
{
    // Prompt for input
    print!("Enter the size: "); // print! is a macro (not a function) to print to stdout without a newline
    io::stdout() // get a handle to stdout
        .flush() // flush buffer to stdout
        .unwrap(); // unwrap the result of flush if Ok, panic if Err
    
    // Get input in the same line
    let mut num = String::new(); // create a mutable string to hold the name
    io::stdin() // get a handle to stdin
        .read_line(&mut num) // read a line from stdin into the mutable string
        .expect("failed to readline"); // handle any errors
    let num: u8 = num.trim() // trim the string to remove the newline
            .parse::<u8>() // parse the string into an unsigned 8-bit integer
            .expect("invalid input");  // handle any errors
    
    // Call Patterns' Functions
    println!(); // print a newline
    call_patterns(num); // call call_patterns function with num as argument

}