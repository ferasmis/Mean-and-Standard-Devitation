## Author: Feras
## Problem: Implement a program to compute a sumOfNum, mean, 
##  and standard deviation of a series of integer numbers
## Formula: 1) mean = sum/length of the series
##          2) Standard devitation

import math

def standardDeviationCalculator(numbers):
    sumOfNum = 0.0
    length = len(numbers)
    standardDeviation = 0.0

    for i in numbers:
        sumOfNum += i
    
    mean = sumOfNum / length

    for i in numbers:
        standardDeviation += math.pow(i - mean, 2)
        
    result = math.sqrt(standardDeviation / length)

    print("The sumOfNum is " + str(sumOfNum) + ", the mean is " + str(mean)
     + ", and the standard deviation is " + str(round(result,6)) + ".")
    return result
standardDeviationCalculator(list(range(1,11)))