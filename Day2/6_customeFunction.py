# Custom function to convert the celsius to fahrenheit 

def convert_to_fahrenheit(celsius_temp):
    calculation = celsius_temp * 1.8 
    return calculation + 32

result = convert_to_fahrenheit(37)
print(result)

convert_to_fahrenheit(celsius_temp=0)



# Custom function to calculate Simple Interest

def Simple_interest(amount,year,rate):
    SI = (amount*rate*year)/100
    return SI

result = Simple_interest(1000,10,2)
print(result)


