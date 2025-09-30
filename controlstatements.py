'''#if statement example
#checking positive of a number
num=int(input("Enter a number:"))
if num<0:
    print(f"{num} is a negative ")
if num>0:
    print(f"{num} is a positive ")
#converting fahrenheit to celsius and vice vera
ch=input("Enter your choice Fahrenheit as f and celsius as c :")
if ch=='f' or ch=='F':
    f=int(input("Enter the fahrenheit value :"))
    c=5/9*(f-32)
if ch=='c' or ch=='C':
    c=int(input("Enter celsius value:"))
    f=(9/5*c)+32
print(f"fahrenheit {f} is equal to celsius {c} value..")
#if else statemenmt
#coverting temperature c to f or f to c
val=input("Enter fahrenheit as F or Celsius as C:")
if val=='c' or 'C':
    cel=float(input("Enter celsius to convert f :"))
    f=(9/5*c)+32
else:
    f=int(input("Enter the fahrenheit value :"))
    c=5/9*(f-32)
print(f"fahrenheit {f} is equal to celsius {c} value..")
#odd or even
n=int(input("Enter a number:"))
if n%2==0:
    print(n, "is a even")
else:
    print("number is odd")

#nested if 
#leap or not
year=int(input("Enter year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is leap year")
        else: 
            print(f"{year} is not leap year")
else:
    print(f"{year} is not leap year")
 #leap or not
 #  using if else   
year=int(input("Enter year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not a leap year")

#if elif else
m1=int(input("Enter subject1:"))
m2=int(input("Enter subject2:"))
m3=int(input("Enter subject3:"))
m4=int(input("Enter subject4:"))
m5=int(input("Enter subject5:"))
tot=m1+m2+m3+m4+m5
avg=tot/5
print(avg)
if avg>=90:
    print("O")
elif avg>=80 and avg<90:
    print("A+")
elif avg>=70 and avg<80:
    print("A")
elif avg>=60 and avg<70:
    print("b+")
elif avg>=50 and avg<60:
    print("B")
else:
    print("fail")
    
#--------------------------------iterative control statements----------------------
#for loop
#sum of n numbers
n=int(input("Enter no of numbers to sum:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
'''
#while loop
#factorial
n=int(input("Enter n no factorial:"))
if n<0:
    print("factorial not for negqtive numbers")
elif n==0:
    print("factorial of 0 is 1")
else:
    fact=1
    i=1
    while(i<=n):
        fact*=i
        i+=1
print(fact)
