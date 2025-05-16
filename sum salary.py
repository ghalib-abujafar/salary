li=[]
while True:
    x, y = map(int, input("enter the hour and minutes: ").split())
    if x == -1 or y == -1:
        break
    li.append([x,y])
minutes=sum(int(row[1]) for row in li)
hour=sum(int(row[0]) for row in li)+ int(minutes/60)

salary = (hour + ((minutes%60) / 60 ))*1.7

has_double=input("do you have hour on double pay Yes or No: ")
if has_double.lower() == "yes":
    d_hour = 0
    d_minutes = 0
    while True:
        h, m=map(int, input("enter the hour and minutes: ").split())
        if h == -1 or m == -1:
            break
        d_hour = d_hour + h
        d_minutes = d_minutes + m
        
    double_pay=((d_hour/2)+((d_minutes%60) / 60 ))*1.7
    salary = salary + double_pay

print(f"your hours is {hour}h and {minutes%60}m")
print(f"your salary without Daman is : {salary:.2f}")
print(f"your salary with Daman is : {salary-22.75:.2f}")
