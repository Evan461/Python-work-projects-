print("Welcome to Evan's Weight and Height converter! ")#This prints out the intro statement when the code is ran.
weight = input("Please enter your weight: ") #This tells the user to input their weight 
print("Your weight is" + " " + weight + " in pounds. ") #This prints out the print statement but puts the number the user inputted into the statement
ask = input("Do you want to convert your weight into kilograms?: ")#This ask the user if they want to convert their into kilograms

if ask == "Yes" or ask == "yes": #This says if the user says "Yes" or "yes" run this code 
    kilo = int(weight) /2.205 #This is the equation to get kilograms it changes the users number into a intger so that after it can get divied by 2.205
    print("Your weight in kilograms is " + str(kilo))#This prints out the statement while converting the intger into a string 
else: #This is our else statement 
    print(f"Your weight is {weight} pounds.")#This is a f string that prints out with the rest of the statement 

height = input("Please enter your height: ") #This tells the user to input their height 
print("Your height is " + height + " in inches. " )#This prints out this statement but with the height that the user inputted 
question = input("Do you want to convert your height into centimeters: ") #This ask the user if they want to convert their height to centimeters 

if question == "Yes" or question == "yes": #This says if the user inputs yes or Yes to keep the code going keeps going 
    centi = int(height) * 2.54 #This changes the number the user input into a integer then multiplys it by 2.54
    print("Your height in centimeters is " + str(centi)) #This takes the product of the equation and puts it in the print statemnt 
else: #This is our else statement 
    print(f"Your height is {height} inches.") #This is a f string that prints with the print statement 

print("Thanks for using Evan's Weight and Height converter!")#This is the outro statement for the converter 