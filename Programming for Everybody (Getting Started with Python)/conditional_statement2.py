# type of hrs and rate is string
hrs = input("Enter Hours: ") 
rate = input("Enter Rate: ")
print(type(hrs)) 

# so we need to convert it it float to calculate the gross pay
gross_pay = float(hrs) * float(rate)
print(type(gross_pay))
print("Pay:", gross_pay)