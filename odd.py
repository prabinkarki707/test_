# less gooooo
#learning git commit

#lets print some intro for the program
print("Welcome to the inbuild calculater app!!")
print("Here you can perform calculation like addition, subtraction, multification and division!!")

#using while loop to iterate the programs till it's true.
while(True):
    try:
       #using split function to treat euqation into diffrent list of variables
        a,x,b = input("Enter the equation you want to perform seperated by space: ").split()
        a = int(a)
        b = int(b)
        break
    except:
       #this try and except helps us to prevent user from entering any equation that are not not valid
       #since this is inside a loop the program will ask user to input only supported type of equation again and again 
        print("Please enter a valid number or with spaces as shown in below example")
        print("55 + 10 or 55 / 5, 75 * 5, 231 - 123")



x = x.lower()
while True: 
       #if user inputs '+' or "addition"   
     if x == str("addition") or x == "+":
            Result = a + b
            print("Result:", Result)
            break
       #if user assign '-' operator
     elif x == str("subtraction") or x == "-":
            Result = a - b
            print("Result: ", Result)
            break
       #if user assign '*' operator
     elif x == str("multiplication") or x == "*":
            Result = a * b
            print("Result: ", Result)
            break 
       #if user assign '/' operator
     elif x == str("division") or x == "/":
            try:
              Result = 0
              Result = a / b
              print("Result: ", Result)
              break
            except ZeroDivisionError:
              print("Cannot divide by zero")
              break
     else:  
            print("Please enter two number and arthimetic character like '+,-,*,/'")
            print("Enter a valid arithemetic equation, below ar some examples:")      

#adding "=" string in result and treating it as string to write in new text file
Result = " = " + str(Result)             
#using with statement to write a new text file and using "a" to append every new data so that it doesn't replace over previous
# Writing the result to the text file

#updates from old code and correction
#I am really sorry I missunderstood the question I thought I only needed to perform certain things
#but this time I have allowed user to add the calculation in a new file OR/AND
#view any files where previous calculations has been stored
#please update me if I am missing anything, thank you!!


filename = input("Enter the name of the text file to store the calculation: ")
with open(filename, 'a') as file:
   file.write(f"{a} {x} {b} {Result}\n")
print(f"{a} {x} {b} {Result}")
file_name = input("Enter the name of the text file to view: ")
try:
       with open(file_name, 'r') as file:
              contents = file.read()
              print(contents)
except FileNotFoundError:
            print("File not found. Please make sure the file exists.")



#to ask user if they wanna perform any other calculation and repeating the same process as above and 
# using try and except statement to catch if user put any other value      
while True:
    try: 
       cont = input("Do you want to perform another task? (y/n): ")
       if cont.lower() == "y":
              print("Welcome to the inbuild calculater app!!")
              print("Here you can perform calculations like addition, subtraction, multiplication, and division!!")
              while True:
                     try:
                            a, x, b = input("Enter the equation you want to perform separated by space: ").split()
                            a = int(a)
                            b = int(b)
                            break
                     except:
                            print("Please enter a valid number or with spaces as shown in the below example")
                            print("55 + 10 or 55 / 5, 75 * 5, 231 - 123")
                     
              x = x.lower()
              while True:    
                     if x == str("addition") or x == "+":
                            Result = a + b
                            print("Result:", Result)
                            break
                     elif x == str("subtraction") or x == "-":
                            Result = a - b
                            print("Result: ", Result)
                            break
                     elif x == str("multiplication") or x == "*":
                            Result = a * b
                            print("Result: ", Result)
                            break 
                     elif x == str("division") or x == "/":
                         try:
                             Result = 0
                             Result = a / b
                             print("Result: ", Result)
                             break
                         except ZeroDivisionError:
                             print("Cannot divide by zero")
                             break
                     else:  
                            print("Please enter two numbers and an arithmetic character like '+,-,*,/'")
                            print("Enter a valid arithmetic equation. Below are some examples:")

              Result = " = " + str(Result)
              filename = input("Enter the name of the text file to store the calculation: ")
              with open(filename, 'a') as file:
                      file.write(f"{a} {x} {b} {Result}\n")
                      print(f"{a} {x} {b} {Result}")
              file_name = input("Enter the name of the text file to view: ")
              try:
                     with open(file_name, 'r') as file:
                            contents = file.read()
                            print(contents)
              except FileNotFoundError:
                     print("File not found. Please make sure the file exists.")

       elif cont.lower() == "n":
              print("Thank you for using our calculator!!")
              break

       else:
          print("Please just type y for yes or n for no")
          cont = input("Do you want to perform another task? (y/n): ")  
          

    except ValueError:
          print("Please just type y for yes or n for no")
          cont = input("Do you want to perform another task? (y/n): ")  