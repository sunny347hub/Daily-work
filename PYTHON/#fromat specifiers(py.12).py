#------------------------------------------------------------------fromat specifiers--------------------------------------------------------------------------------
#format specifiers are used to control the formatting of output in Python. They allow you to specify how values should be displayed, such as the number of decimal places, alignment, and padding. Here are some examples of format specifiers:
#FORMAT SPECIFIERS ARE DENOTED BY A COLON (:) FOLLOWED BY THE SPECIFIER. SOME COMMON FORMAT SPECIFIERS INCLUDE:
#:.2f - formats a floating-point number to 2 decimal places
#:10.2f - formats a floating-point number to 2 decimal places and pads it to a width of 10 characters
#:>10 - right-aligns the value within a width of 10 characters
#:<10 - left-aligns the value within a width of 10 characters
#:^10 - centers the value within a width of 10 characters
#:+10 - right-aligns the value within a width of 10 characters and adds a plus sign for positive numbers
#:10 - right-aligns the value within a width of 10 characters
#=10 - right-aligns the value within a width of 10 characters and pads with zeros
#:, - formats a number with a comma as a thousands separator
#:0 - pads the value with zeros instead of spaces
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#EXAMPLE'S
price = 354565.6019
print(f"The price is {price:.2f}")#formats the price to 2 decimal places
print(f"The price is {price:.3f}")#formats the price to 3 decimal places
print(f"The price is {price:4}")#pads the price to a width of 4 characters
print(f"The price is {price:10.2f}")#formats the price to 2 decimal places and pads it to a width of 10 characters
print(f"The price is {price:<10}")#left-aligns the price within a width of 10 characters
print(f"The price is {price:>10}")#right-aligns the price within a width of 10 characters
print(f"The price is {price:^10}")#centers the price within a width of 10 characters
print(f"The price is {price:+10}")#right-aligns the price within a width of 10 characters and adds a plus sign for positive numbers
print(f"The price is {price:=10}")#right-aligns the price within a width of 10 characters and pads with zeros
print(f"The price is {price:}")#displays the price with the default formatting
print(f"The price is {price:^+,.2f}")#centers the price within a width of 10 characters, adds a plus sign for positive numbers, and formats it with a comma as a thousands separator and 2 decimal places