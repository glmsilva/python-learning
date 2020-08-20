def computePay(hour, rate) :
    pay = 0
    extra_hour = 0

    if hour < 40 :
        pay = hour * rate
        return pay
    elif hour >= 40 :
        extra_hour = hour - 40
        extra_hour = extra_hour * (rate * 1.5)
        hour = 40
        pay = hour * rate + extra_hour
        return pay

hour = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

print(computePay(hour, rate))
