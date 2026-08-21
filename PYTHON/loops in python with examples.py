print("-------------------------------------------------------------------------LOOPS IN PYTHON--------------------------------------------------------------------------------")
print("loops = used to repeat a block of code multiple times")

print("while loop = a statement that will execute a block of code as long as a condition is true")

print("for loop = a statement that will execute a block of code a certain number of times")

print("nested loop = a loop inside a loop. The 'inner loop' will be executed one time for each iteration of the 'outer loop'")

print("double nested loop = a loop inside a loop inside a loop. The 'inner loop' will be executed one time for each iteration ofthe 'outer loop' and the 'innermost loop' will be executed one time for each iteration of the 'inner loop'")

print("triple nested loop = a loop inside a loop inside a loop inside a loop. The 'inner loop' will be executed one time for each iteration of the 'outer loop',the 'innermost loop' will be executed one time for each iteration of the'inner loop' and the 'innermost loop' will be executed one time for each iteration of the 'innermost loop'")

print("loop control statements = statements that can change the flow of a loop. These include break, continue and pass")

print("do while loop = a statement that will execute a block of code once, and then repeat the loop as long as a condition is true. This is not available in  Python but can be simulated using a while loop")

print("infinite loop = a loop that never ends. This will crash your program if you run it")

print("break = a statement used to exit a loop")

print("continue = a statement used to skip the current iteration of a loop and continue with the next one")

print("pass = a statement used to skip a block of code. This is useful when you wantto write a loop but don't want to execute any code yet")

print("_________________________________________________________________________________WHILE LOOPS_________________________________________________________________________________")
#while condition:
    #code to execute

print("Example 1:")
name = input("Enter your name: ")
while name == "":
    print("You did not enter a name. Please try again.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")
#-----------------------------------------------------------------------
print("Example 2:")
age = int(input("Enter your age: "))
while age < 0:
    print("You cannot enter a negative age. Please try again.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")
#---------------------------------------------------------------------
print("Example 3:")
while True:
    name = input("Enter your name: ")
    if name != "":
        break
    print("You did not enter a name. Please try again.")
print(f"Hello, {name}!")
#----------------------------------------------------------------------
print("Example 4:")
age = int(input("Enter your age: "))
while age >= 18:
    print("you are eligible to vote.")
    age = int(input("Enter your age: "))
print(f"you are not eligible to vote because you are {age} years old.")
#----------------------------------------------------------------------
print("Example 5:")
food = input("Enter the food you like to eat or 'quit' to stop: ")
while food != "quit":
    print(f"You like to eat {food}.")
    food = input("Enter the food you like to eat or 'quit' to stop: ")
print("thank you for sharing your favorite food with me!")
print("goodbye!")
#-----------------------------------------------------------------------
print("Example 6:")
num = int(input("enter the # between 1 and 10: "))
while num < 1 or num> 10 :
    print ("you entered in valid number. Please try again.")
    num = int(input("enter the # between 1 and 10: "))
print(f"you entered {num}. thank you for entering a valid number!")
#----------------------------------------------------------------------

print("Example 7:")
print("____________________________ COMPOUND INTEREST CALCULATOR _____________________________")
principle = float(input("Enter the principle amount: "))
while principle < 0:
    print("You cannot enter a negative principle amount. Please try again.")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the interest rate (as a decimal): "))
while rate < 0:
    print("You cannot enter a negative interest rate. Please try again.")
    rate = float(input("Enter the interest rate (as a decimal): "))

time = float(input("Enter the time in years: "))
while time < 0:
    print("You cannot enter a negative time. Please try again.")
    time = float(input("Enter the time in years: "))

print(f"The principle amount is: {principle:,.2f}")
print(f"The interest rate is: {rate}")
print(f"The time is: {time}")

total_amount = principle * pow((1 + rate/100), time)
print(f"The balance after {time} years is: {total_amount:,.2f}")

print("____________________________________________________________________________FOR LOOPS_________________________________________________________________________________")
#for variable in sequence:
    #code to execute

print("Example 1:")
for i in range(5):#[IT WILL PRINT UP TO 4 BECAUSE IT STARTS AT 0 AND INCREMENT BY 1 UNTIL IT REACHES 5 AN HERE 5 IS NOT INCLUDED]
    print(i)
#----------------------------------------------------------------------

print("Example 2:")
for i in reversed(range(1, 11)):#[HERE IT WILL START AT 10 AND DECREMENT BY 1 UNTIL IT REACHES 1 AND HERE 1 IS INCLUDED ]
    print(i)   

print("HAPPY NEW YEAR!")
#----------------------------------------------------------------------

print("Example 3:")
for i in range(0, 11, 2): #[HERE 2 INDICATES THE STEP SIZE. IT WILL START AT 0 AND INCREMENT BY 2 UNTIL IT REACHES 10]
    print(i)
#----------------------------------------------------------------------

print("Example 4:")
for i in range(10, 0, -1): 
    print(i)
#----------------------------------------------------------------------

print("Example 5:")
for i in range(5):
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
#----------------------------------------------------------------------

print("Example 6:")
for i in range(5):
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.") 
#----------------------------------------------------------------------

print("Example 7:")
import time
my_time = 10
for x in range(0, my_time):
    print(f"Time remaining: {my_time - x} seconds")
    time.sleep(1) #[HERE IT WILL PAUSE THE PROGRAM FOR 1 SECOND BEFORE CONTINUING TO THE NEXT ITERATION]
print("HAPPY NEW YEAR!")
#----------------------------------------------------------------------

print("Example 8:")
import time 
my_time = int(input(" enter the time you want to count down from :"))
for x in range(my_time, 0, -1):
    seconds = int(x%60)
    minutes = int((x/60)%60)
    hours = int((x/3600)%24)
    print(f"time remaining : {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0)
print("TIME'S UP!")

print("____________________________________________________________________________NESTED LOOPS_______________________________________________________________________________")
#nestesd loop syntax
#for variable in sequence:
    #for variable in sequence:
        #code to execute
#-----------------------------------------------------------------------

print("Example 1:")
for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")
#-----------------------------------------------------------------------

print("Example 2: ")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
#-----------------------------------------------------------------------

print("Example 3:")
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            print(f"{i} x {j} x {k} = {i * j * k}")
#-----------------------------------------------------------------------

print("Example 4:")
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                print(f"{i} x {j} x {k} x {l} = {i * j * k * l}")
#-----------------------------------------------------------------------

print("Example 5:")
for i in range(3):
    for j in range(1,11):
        print(j,end=" ")#[HERE IT WILL PRINT THE NUMBERS FROM 1 TO 10 ON THE SAME LINE BECAUSE OF THE END PARAMETER]
    print()#[HERE IT WILL PRINT A NEW LINE AFTER EACH ITERATION OF THE OUTER LOOP]
#-----------------------------------------------------------------------

print("Example 6:")
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
symbol = input("Enter the symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()
