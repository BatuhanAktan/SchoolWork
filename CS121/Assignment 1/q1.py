import math


inputVal = float(input("Please enter the x value: "))

def firstEq(val):

    result = (1-math.cos(val))/(val**2)

    return result

def secondEq(val):

    result = (2(math.sin(val/2)**2))/(val**2)

    return result

def thirdEq(val):

    if val <= 0:
        result = 0 
    elif 0<val<=1:
        result = (3*(val**2))-(2*(val**3))
    else:
        result = 1

    return result

def fourthEq(val):

    result = (1/math.sqrt(2*math.pi))*math.e**(-1*((val^2)/2))

    return result

print(firstEq(inputVal))
print(secondEq(inputVal))
print(thirdEq(inputVal))
print(fourthEq(inputVal))
