def C_2_F(number):
    # Celsius to Fahrenheit

    # Reading temperature in Celsius
    celsius = number

    # Converting
    fahrenheit = 1.8 * celsius + 32
    print(fahrenheit)

    # Displaying output
    return fahrenheit
    
def C_2_K(number):
    # Celsius to Kelvin

    # Reading temperature in Celsius
    celsius = number

    # Converting
    kelvin = 273.15 + celsius
    print(kelvin)

    # Displaying output
    return kelvin

def F_2_C(number):
    # Fahrenheit to Celsius

    # Reading temperature in Fahrenheit
    fahrenheit = number

    # Converting
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)

    # Displaying output
    return celsius
    
def F_2_K(number):
    # Fahrenheit to Kelvin

    # Reading temperature in Fahrenheit
    fahrenheit = number

    # Converting
    kelvin = 5 * (fahrenheit - 32)/9 + 273.15
    print(kelvin)

    # Displaying output
    return kelvin

def K_2_F(number):
    # Kelvin to Fahrenheit

    # Reading temperature in Fahrenheit
    kelvin = number

    # Converting
    fahrenheit = kelvin * 1.8 - 459.67
    print(fahrenheit)

    # Displaying output
    return fahrenheit

def K_2_C(number):
    # Kelvin to Celsius

    # Reading temperature in Kelvin
    kelvin = number

    # Converting
    celsius = kelvin - 273.15
    print(celsius)

    # Displaying output
    return celsius

if __name__ == "__main__":
    number = float(input("Enter the degree you want to convert from C to F: "))
    print("The value in Fahrenheit is:", end = " ")
    C_2_F(float(number))
    number = float(input("Enter the degree you want to convert from C to K: "))
    print("The value in Kelvin is:", end = " ")
    C_2_K(float(number))
    number = float(input("Enter the degree you want to convert from F to C: "))
    print("The value in Celsius is:", end = " ")
    F_2_C(float(number))
    number = float(input("Enter the degree you want to convert from F to K: "))
    print("The value in Kelvin is:", end = " ")
    F_2_K(float(number))
    number = float(input("Enter the degree you want to convert from K to F: "))
    print("The value in Fahrenheit is:", end = " ")
    K_2_F(float(number))
    number = float(input("Enter the degree you want to convert from K to C: "))
    print("The value in Celsius is:", end = " ")
    K_2_C(float(number))