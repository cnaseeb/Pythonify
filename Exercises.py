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
