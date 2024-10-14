def computepay(h, r):
    if h <= 40:
        return h * r
    overtime = h - 40
    return (r * 40) + (1.5 * r * overtime)

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)