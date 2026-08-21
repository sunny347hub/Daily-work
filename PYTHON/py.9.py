unit = input("what is the temperature unite you want to convert from (C for Celsius and F for Fahrenheit): ")
temperature = float(input("what is the temperature you want to convert?: "))
if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {round(converted_temperature, 2)}°F")
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {round(converted_temperature, 2)}°C")
else:
    print("invalid unit, only  Celsius or Fahrenheit is available")   
