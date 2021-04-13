"""
A calculator that converts Fahrenheit to Celsius and Celsius to Fahrenheit.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""
while True:
    try:
        conversionDet = input("If you like to convert from Celsius to Fahrenheit input CtoF\nIf you like to convert from Fahrenheit to Celsius input FtoC \nYour Input: ")
        if conversionDet.lower() == "ctof": 
            temp = input("Please input the temperature you would like to convert: ") # gets the temperature input
            convertedTemp = (9/5)*int(temp)+32 # converts celsius to fahrenheit
            print(str(round(convertedTemp, 2))+ " degrees fahrenheit") # prints Result
        elif conversionDet.lower() == "ftoc":
            temp = input("Please input the temperature you would like to convert: ")
            convertedTemp = (int(temp)-32)*(5/9) # converts fahrenheit to celsius
            print(str(round(convertedTemp, 1)) + " degrees celsius")
        else:
            print("That does not look like one of the options. Try again.") # warns user on invalid error
    except ValueError:
        print("That does not look like the input im looking for.")
        continue
    except:
        print("Some Unknown error occured. Try inputting again.") # catches any other potential errors
        continue
                            
