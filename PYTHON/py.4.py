item = input("what is the name of the item?:")

price = float(input("what is the price of the item?: "))

quantity = int(input("how many would you like to buy?: "))

total_price = price * quantity

print(f"the item you like to buy is {item} and you are buying {quantity} of them so total price is ${round(total_price, 1)}")

feedback = input("give your feedback about the item you bought:")

not_good = False

if feedback == "not good":

    not_good = True

    print("we are sorry to hear that you did not like the item")

else:

    print("we are glad to hear that you like the item")

print (f"thank you for your feedback about {item}") 

print("thank you for visiting our food court ")

print("we hope to see you again soon")
