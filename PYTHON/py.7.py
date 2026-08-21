age = input("Enter your age :")

if int(age) >= 18 and int(age) < 100:

    print("you are eligible  to vote")

elif int (age) >= 100:

    print("you are not eligible to vote because you are too old")

elif int(age) < 0:

    print(" you are not born yet")

else:

    print("you are not eligible to vote")
    
print("thank you for using our voting eligibility checker")