tot = 0
count = 0
while True:

    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    count = count + 1
    tot = tot + fnum

print(tot, count, tot/count)



