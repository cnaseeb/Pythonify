# The code below almost works

name = input("Enter your name")
print("Hello", name)


##2
# This first line is provided for you

hrs = input("Enter Hours:")
# hrs = float(hrs) #use the one in line 9 instead
ratePerHour = input("Enter rate per hour:")
# rateperHour = float(ratePerHour) #use the one in line 9 instead
# you will hit the following error, if you don't convert the inputs to float
# TypeError: can't multiply sequence by non-int of type 'str' on line 5
grossPay = float(hrs) * float(ratePerHour)
print("Pay:", grossPay)


##3.1
hrs = input("Enter Hours:")
ratePerHour = input("Enter rate per hour:")
try:
    fhrs = float(hrs)
    fratePerHour = float(ratePerHour)
except:
	print("Error, please enter numeric input")
	quit()
#print(fhrs, fratePerHour)
#Pay = float(hrs) * float(ratePerHour)
if fhrs > 40:
    PayNormal = fhrs * fratePerHour
    PayExtra = (fhrs - 40) * (fratePerHour * 0.5)
    Pay = PayExtra + PayNormal
else:
    Pay = fhrs * fratePerHour
print(Pay)


### 3.3
"""3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85."""

### done
score = input("Enter Score: ")
score = float(score)
#if score in range(0.0,0.9): #only ints
if 0.0 <= score and score <= 1.0:
    if score >= 0.9 and score <= 1.0:
        print("A")
    elif score >= 0.8 and score < 0.9:
        print("B")
    elif score >= 0.7 and score < 0.8:
        print("C")
    elif score >= 0.6 and score < 0.7:
        print("D")
    elif score < 0.6:
        print("F")
else:
    print("Error, please enter the score in the range of 0.0 and 1.0")
    quit()

### 4.6
"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for 
hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a
function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 
10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a
number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name 
your variable sum or use the sum() function."""

def computepay(hrs,ratePerHour):
    hrs = input("Enter Hours:")
    ratePerHour = input("Enter rate per hour:")
    try:
    	fhrs = float(hrs)
    	fratePerHour = float(ratePerHour)
    except:
		print("Error, please enter numeric input")
		quit()
	#print(fhrs, fratePerHour)
	#Pay = float(hrs) * float(ratePerHour)
    if fhrs > 40:
        PayNormal = fhrs * fratePerHour
        PayExtra = (fhrs - 40) * (fratePerHour * 0.5)
        Pay = PayExtra + PayNormal
    else:
    	Pay = fhrs * fratePerHour
    #print(Pay)
    
    return Pay


p = computepay(10,20)
print("Pay", p)

### 5.1
# print Total, count of numbers, and their average entered by a user
# also do verification
num = 0
total = 0
while True :
  sval = input('Enter a number')
  if sval == 'done' :
   break
  try:
    fval = float(sval)
  except:
    print('Invalid input')
    continue
  num = num + 1
  total = total + fval
  
print(total, num, total/num)

### 5.2
"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the
largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

largest = None
smallest = None
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            ival = int(num)
        except:
    		print('Invalid input')
    		continue
        if count == 0 and smallest is None:
            smallest = ival
        if ival < smallest:
            smallest = ival
        elif largest is None or ival > largest:
            largest = ival
               
        count = count + 1
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)

