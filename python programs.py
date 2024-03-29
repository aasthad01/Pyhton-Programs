#To implement all arithmetic, relational and logical operations
first=input("enter the first number ")
second=input("enter the second number ")
sum=int(first)+int(second)
print("the sum of two number is",sum)

sub=int(first)-int(second)
print("the subtraction of number is",sub)

mul=int(first)*int(second)
print("the product of number is",mul)

div=int(first)/int(second)
print("the difference of number is",div)

print(int(first)<int(second))
print(int(first)>int(second))
print(int(first)!=int(second))
print(int(first)<=int(second))
print(int(first)>=int(second))
print(int(first)==int(second))

#To check number is even or odd
n=input("enter the number to be checked ")
n=int(n)
if n%2==0:
   print("the number is even")
else n%2!=0:
   print("the number is odd")

#To check greater of two numbers
n1=input("enter first number")
n2=input("enter second number")
if n1>n2:
  print("first number is greater")
else:
  print("second number is greater")

#To check greater of three numbers
n1=input("enter first number")
n2=input("enter second number")
n3=input("enter third number")
n1=int(n1)
n2=int(n2)
n3=int(n3)
if n1>n2 and n1>n3:
  l=n1

elif n2>n1 and n2>n3:
  l=n2

elif n3>n1 and n3>n2:
  l=n3

else:
  print("invalid")    

print("the largest number is ",l)

#To find number is prime or composite
n=input("enter the number ")
n=int(n)
count=0
for i in range (2,n):
  if n%i==0:
    count+=1
    break
else:
    print("the number is prime")  

if count!=0:
  print("number is composite")

#To print all even numbers in range
n=int(input("enter the range "))
for i in range(1,n+1):
  if i%2==0:
    print(i)

#To print all odd numbers in range
n=int(input("enter the range "))
for i in range(1,n+1):
  if i%2!=0:
    print(i)

#To print all prime numbers in the range
n=int(input("enter the range "))
for j in range(2,n+1):
   count=0
   for i in range (2,j):
     if j%i==0:
       count+=1
       break
   else:
       print(j)

#To find reverse of a number
n=int(input("enter the number "))
rev=0
while n!=0:
  d=n%10
  rev=rev*10+d
  n//=10

print("reversed number:",rev)

#To find number is palidrome or not
n=int(input("enter the number "))
org=n
rev=0
while n!=0:
  d=n%10
  rev=rev*10+d
  n//=10

if rev==org:
    print ("the number is palidrome")
else:
    print("the number is not palidrome")

#To check number is armstrong number or not
n=int(input("enter the number"))
sum=0
temp=n
while temp>0:
  digit=temp%10
  sum+=digit**3
  temp//=10

if n==sum:
  print("the number is armstrong")   
else:
  print("the number is not armstrong")

#To print all amstrong numbers in a range
lower=100
upper=2000
for n in range (lower,upper+1):
  order=len(str(n))
  sum=0
  temp=n
  while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10

  if n==sum:
    print(n)

#To find sum of first 'n' natural numbers
n=int(input("enter the number "))
sum=0
i=1
while i<=n:
 sum=sum+i
 i=i+1

print("the sum of numbers is",sum)

#To find the factorial of a given number
n=int(input("enter the number "))
if n<0:
  print("enter the positive number")
elif n==0 and n==1:
  print("factorial is 1")
else:    
 fac=1
 i=1
 while i<=n:
  fac=fac*i
  i=i+1

print("factorial of the number is",fac)

#To print fibonacci series upto 'n' terms
n=int(input("enter the number of terms"))
a=0
b=1
count=0
if n<=0:
  print("enter a positive number")
elif n==1:
  print(a)
else:
  while count<n:
    print(a)
    sum=a+b
    a=b
    b=sum
    count=count+1

#To check year is leap year or not
year=int(input("enter the year "))
if year%400==0 and year%100==0:
  print("it is a leap year")
elif year%4==0 and year%100!=0:
  print("it is a leap year")
else:
  print("it is not a leap year")

#To print temperature in 'degree F' to 'degree C' and vice versa
temp=input("your temperature is in c or f ")
val=float(input("enter the temperature"))
if temp=='c':
  f=(val*1.8)+32
  print("the temperature in fahrenheit is ",f)
elif temp=='f':
  c=(val-32)/1.8  
  print("the temperature in celcius is ",c)
else:
  print("invalid entry")

#To print all factors of a given number by using function
def factor(num):
  if num<=0:
    print(num)
  else:
    print("factors of number",num)
    for i in range(1,num+1):
      if num%i==0:
        print(i)

n=int(input("enter the number "))
factor(n)

#To convert decimal to binary, octal and hexadecimal with library function
n=int(input("enter the decimal number "))
b=bin(n)
print("binary conversion is",b)
h=hex(n)
print("hexadecimal conversion is",h)
o=oct(n)
print("octal conversion is",o)

#To find factorial of a number by developing function
def fact(num):
  if num<0:
    print("enter a postive number")
  elif num==0:
    print(1)
  else:
    fac=1
    print("factorial of",num) 
    for i in range(1,num+1):
      fac=fac*i
    print(fac)  

n=int(input("enter a number "))
fact(n)

#To print fibonacci series using recursion
def fib(num):
  if num<=1:
    return(num)
  else:
    return(fib(num-1)+fib(num-2))

n=int(input("enter the number "))
print("fibonacii series upto",n)
for i in range(n):
  print(fib(i))

#To find factorial of a number using recursion
def fact(n):
  if n<0:
    print("enter a postive number")
  elif n==0:
    return(1)
  else:
    return(n*fact(n-1))

num=int(input("enter a number "))
print("factorial of number ",fact(num))

#To find sum of first 'n' natural numbers using recursion
def sum(n):
  if n<=1:
    return(n)
  else:
    return(n+sum(n-1))

num=int(input("enter a number "))
if num<0:
  print("enter a positive number ") 
else:
  print("sum of numbers upto",num,"is",sum(num))

#To convert decimal number to binary using recursion
def binary(n):
  if n>1:
    binary(n//2)
  print(n%2,end='')  
    
num=int(input("enter a decimal number "))
binary(num)

#To display power of 2 using anynomous function
num=int(input("enter the number "))
square=lambda num: num**2
print("the power of two of number is",square(num))

#To find area of triangle,circle,cylinder using lambda function
h=int(input("enter the height of the triangle "))
b=int(input("enter the base of the triangle "))
tri=lambda h,b: b*h/2
print("area of triangle is",tri(h,b))

r=int(input("enter the radius of the circle "))
cir=lambda r: 3.14*r*r
print("the area of circle is",cir(r))

rd=int(input("enter the radius of the cylinder "))
ht=int(input("enter the height of cylinder "))
cyl=lambda rd,ht: (2*3.14*rd*ht)+(2*3.14*rd*rd)
print("area of cylinder is",cyl(rd,ht))

#To add two matrices
x=[[1,2,3],
   [2,3,4],
   [3,4,5]]
y=[[1,1,1],
   [2,2,2],
   [3,3,3]] 
sum=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):
  for j in range(len(x[0])):
    sum[i][j]=x[i][j]+y[i][j]

print("sum of two matrices is")
for a in sum:
  print(a)

#To multiply two matrices
x=[[1,2,3],
   [2,3,4],
   [3,4,5]]
y=[[1,1,1],
   [2,2,2],
   [3,3,3]] 
multiply=[[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
   for j in range(len(y[0])):
       for k in range(len(y)):
           multiply[i][j] += x[i][k]*y[k][j]

for a in multiply:
   print(a)

#To transpose of matrices
x=[[12,7,2],
   [4 ,5,1],
   [3 ,8,4]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
   for j in range(len(x[0])):
       result[j][i]=x[i][j]

for a in result:
   print(a)

#To find average of a numeric list
l=[2,4,1,1,2]
sum=0
for i in range (len(l)):  
  sum=sum+l[i]
print(sum)  
avg=sum/len(l)
print("the average of list is",avg)

#To access member of list using different variations of slice operation
l=[2,4,1,1,2,5,6,7,8,9,3]
print(l[:])
print(l[2:])
print(l[:8])
print(l[2:9])
print(l[::2])
print(l[::-1])
print(l[3:9:2])

#To concatenate two lists
l1=['a','b','c',2,3]
l2=[3,4,1,2,'c']
l1.extend(l2)
print(l1)
l1.append(l2)
print(l1)
x=(l1)+(l2)
print(x)

#To find index of a specific elements and print number of occurences
l=[ 2, 3, 3, 4, 1, 2, 5, 4]
n=int(input("enter the element to be searched "))
a=l.index(n)
print("the index of the element is",a)
b=l.count(n)
print("the occurence of the element is",b)

#To identify duplicates in the list
l=[ 2, 3, 3, 4, 1, 2, 5, 4]
for i in range(0,len(l)):
  for j in range(i+1,len(l)):
    if l[i]==l[j]:
      print(l[j])

#To iterate over dictionary using for loop 
brands={"nescafe":"coffee","McDonald's":"fast food","nike":"apparel","pepsi":"drinks","sony":"electronics"}
for key,value in brands.items():
  print(key,"-",value)

#To illustrate nested dictionary
student={1: {"name": "John", "age": "17", "gender": "Male"},
         2: {"name": "Marie", "age": "12", "gender": "Female"}}

print(student)

#To sort the dictionary according to keys, according to values
student={"ravi": "10", "rajnish": "9", "sanjeev": "15", "yash": "12", "suraj": "11"}
print("dictionary before sorting",student)

sortk=sorted(student.items(),key=lambda x: x[0])
print("dictionary sorted according to keys",sortk)

sortv=sorted(student.items(),key=lambda x: x[1])
print("dictionary sorted according to values",sortv)
