print("Welcome to Evan's Calculator") #This will print the introduction statement for the Calculator
first_number = int(input("Please Enter Your First Number: "))#This will allow the user to input the number they want to operate on 
operation = (input("Please choose an operation + - * /: "))#This will allow the user the choose what operation they want to do 
second_number = int(input("Please enter Your second Number: "))#This will allow the user to choose the second number 
#they want to add/subtract/divide/multiply to the first number
if operation == ("+"): #This will choose to add IF thats what the user picks 
    solution = (first_number + second_number)#This will add both the first and second number the user selected 
    print(solution)#This prints out the solution of the first and second number 
elif operation == ("-"):#This will choose to subtract if thats what the user selects
    solution = (first_number - second_number)#This will subtract both the first and the second number they picked
    print(solution)#This will print out the solution to the first and second number 
elif operation == ("*"):#This will choose to multiply if thats what the user is choosing to do 
    solution = (first_number * second_number)#This will multiply the first and second number that the user has picked beforehand
    print(solution)#This will print the solution to the first and second number being multiplyed
elif operation == ("/"):#This will choose the divide if thats what the user picked 
    solution = (first_number / second_number)#This will divide the first and second number that the user has picked giving them the solution 
    print(solution)#This will print out the solution of the two numbers being divided.
print("Thank You for choosing Evan's Calculator")#This is the outro statement for Evan's calculator.
