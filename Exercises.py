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

