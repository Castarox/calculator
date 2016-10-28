import sys #add sys library

def ask(): #define ask function
    print('Enter first number(or letter to exit): ', end='') #ask user for first argument
    number = input() #pass argument to number
    if number.isdigit(): # check what type of argument was passed
        return number           
    elif number.isalpha():               
        print('Goodbay')
        sys.exit(0)      #close program if argument is alpha
    else:
        print('You must choose somthing :-)')
        ask()

def operator(firstNumber):  #define ask function witch check operator passed by user
    print('Which operator you want to use')
    print('You can choose from: \'+\', \'-\', \'*\', \'/\',')
    operation = input()  
    
    if operation == '+':            #check which operator was selected
        return add(firstNumber)
    elif operation == '-':
        return subtraction(firstNumber)
    elif operation == '*':
        return multiplication(firstNumber)
    elif operation == '/':
        return division(firstNumber)
    else:
        print('You entered the wrong parameter', end='\n\n')
        operator(firstNumber)

def add(firstNumber): #function add 2 parameters
    print('Enter the second number: ', end='')
    secondNumber = input()
    if secondNumber.isdigit():
        return int(firstNumber) + int(secondNumber)
    else:
        print('You must enter number', end='\n\n')
        add(firstNumber)

def subtraction(firstNumber):   #function subtraction 2 parameters
    print('Enter the second number: ', end='')
    secondNumber = input()
    if secondNumber.isdigit():
        return int(firstNumber) - int(secondNumber)
    else:
        print('You must enter number', end='\n\n')
        subtraction(firstNumber)

def multiplication(firstNumber): #function multiplication 2 parameters
    print('Enter the second number: ', end='')
    secondNumber = input()
    if secondNumber.isdigit():
        return int(firstNumber) * int(secondNumber)
    else:
        print('You must enter number', end='\n\n')
        multiplication(firstNumber)

def division(firstNumber): #function division 2 parameters
    print('Enter the second number: ', end='')
    secondNumber = input()
    if secondNumber.isdigit():
        score = int(firstNumber) / int(secondNumber)
        return score
    else:
        print('You must enter number', end='\n\n')
        division(firstNumber)

def main(): #main function
    result = 0
    number = ask() #call ask function
    result = operator(number) #call operator function
    print('Your result is equal to: ', result, end='\n\n')
    main() #call main function again

if __name__ == '__main__': 
    main() #first run main function    
