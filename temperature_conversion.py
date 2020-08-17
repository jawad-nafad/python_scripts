
user_input = input("What is the temparature in fahrenheit? ")
if(user_input.isnumeric()==False):
    print("Value is not a number")
    exit()
celsius = (int(user_input) -32) * 5/9
celsius = int(celsius)

print('Temperature in celsius is '+ str(celsius))
