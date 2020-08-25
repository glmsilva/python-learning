#Write a program to prompt the user for hours and rate per hour using input to
#compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
#hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
#10.50 per hour to test the program (the pay should be 498.75). 

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
a = 1.5

if hrs <= 40:
    pay = hrs * rate
    print(pay)
elif hrs > 40:
    whr = hrs - 40
    hrs = 40
    pay = hrs * rate + whr * (rate*1.5)
    print(pay)
