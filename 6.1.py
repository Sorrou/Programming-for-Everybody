def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        h1 = (h // 40) * 40 * r
        h2 = (h % 40) * (r * 1.5)
        pay = h1 + h2
        return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print(p)