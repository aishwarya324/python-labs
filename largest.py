"largest"
n1=float(input("Enter the first number: "));
n2=float(input("Enter the second number: "));
n3=float(input("Enter the Third number: "));
def largest():      #function definition
     if(n1>=n2) and (n1>=n2):
         largest=n1
     elif(n2>=n1) and (n2>=n3):
         largest=num2
     else:
         largest=n3
         print("Largest number is",largest)
largest()
pass

"sum of digits"

n1=int(input("Enter the first number: "));
n2=int(input("Enter the second number: "));
n3=int(input("Enter the Third number: "));
def sum(a,b,c):
    sum=a+b+c
    return sum
print("the sum of three numbers is:",sum(n1,n2,n3))




"hcf of two numbers"
def hcf(a,b):
    if a>b:
        small=b
    else:
        small=a
    for x in range(1,small+1):
        if((a%x==0)and (b%x==0)):
            result=x
    return result  
n2=int(input("Enter the second number: "));
n1=int(input("Enter the first number: "));
print("the hcf of n1 and n2 is",hcf(n1,n2))

"LCM OF TWO NUM"  

def lcm(a,b):
    if a>b:
        big=a
    else:
         big=b   
    while(True):
        if((big % a==0) and (big % b==0)):
            lcm=big
            break
        big+=1
    return lcm
n1=int(input("enter n1:")) 
n2=int(input("enter n2:")) 
print("the lcm of two num is:",lcm(n1,n2))

"leap year"

def check(y):
    if(y % 100)==0:
        if(y % 4)==0:
            if(y % 400)==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
y=int(input("enetr the year")) 
if(check(y)):
    print("leap year")
else:
    print("not a leap year")           


"type of triangle"

s1=int(input("Enter the first number: "));
s2=int(input("Enter the second number: "));
s3=int(input("Enter the Third number: "));
def triangle(a,b,c):
    if(a==b and a==c):
        print("triangle is equilateral")
    elif(a==b or b==c or a==c):
        print("triangle is isosceles")
    else:
        print("trianle is scalar")
triangle(s1,s2,s3)

"roots of quadratic equation"


import math
def equation(a,b,c):
    dis=b*b-4*a*c
    sv=math.sqrt(abs(dis))
    if dis > 0:
        print("real and diff roots")
        print((-b + sv)/(2 * a))
        print((-b - sv)/(2 * a))
    elif dis==0:
        print("roots are same")
        print(-b/(2*a))
    else:
        print("complex roots")

s1=int(input("Enter the first number: "));
s2=int(input("Enter the second number: "));
s3=int(input("Enter the Third number: "));
equation(s1,s2,s3)

"vowel or consonent"


jch=input("enter a character")
def voc(l):
    if l in ('a','e','i','o','u'):
        print("%s is vowel:" %l)
    else:
        print("%s is consonent:" %l)
voc(ch)

"fibo series"

numterms = int(input("How many terms? "))
num1,num2 = 0, 1
c = 0
if numterms <= 0:
   print("Please enter a positive integer")
elif numterms == 1:
   print("Fibonacci sequence upto",numterms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while c < numterms:
       print(num1)
       nth = num1 + num2
       
       num1 = num2
       num2 = nth
       c+= 1

"factors of number"

def fact(n):
    if n== 1:
        return n
    else:
        return n* fact(n- 1)
n = int(input("Enter a Number: "))
if n< 0:
    print("Factorial cannot be found for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", n, "is: ", fact(n))
 
 
 "prime number within in a range"

l  = 900
u= 1000
print("Prime numbers between", l, "and", u, "are:")
for n in range(l, u+ 1):
   # all prime numbers are greater than 1
   if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n)

 "choice based arithmetic"


c= int(input("Enter your choice:n"))  
if (c>=1 and c<=4):
  print("Enter two numbers: ")
  n1 = int(input())
  n2 = int(input())

  if c == 1: # To add two numbers
    res = n1 + n2
    print("Result = ", res)

  elif c== 2: # To subtract two numbers
    res = n1 - n2
    print("Result = ", res)

  elif c== 3: # To multiply two numbers
    res = n1 * n2
    print("Result = ", res)

  elif  c== 4: # To get quotient with decimal value
    res = n1 / n2
    print("Result = ", res)

  elif c == 5:
    exit()
else:
  print("Wrong input..!!")

'sum of triangle'


a=int(input("enter the num"))
def tri(n):
    res=0
    while n>0:
        i=1
        while i<=n:
            res+=i
            i+=1
        n==1
    return res   
tri(a)    

#digital root
def dig(n):
    m=n
    res=0
    while  m>0:
        rem=m%10
        m//=10
        res+=rem
    while res // != 0:
        res = dig(n)
     return res  
n=int(input("enter n"))     

#to find ncr   

def nCr(n, r): 
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
def fact(a): 
   k= 1
   for i in range(2, a+1): 
       k = k* i 
   return k
n = int(input("enyet n"))
r = int(input("enter r"))
print(int(nCr(n, r))) 

#find the missing element

l1=[1,2,3,4]
l2=[1,2,3,4,5]
l3=set(l2) - set(l1)
print(l3)


#mean of the list

l1=[1,2,3,4,5]
def mean(l1):
    return sum(l1)/len(l1)
mean=mean(l1)
print("mean of the given list",round(mean,2))

# In a given list, count no.of elements smaller than their mean



l1=[1,2,3,4,5]
def mean(l1):
    return sum(l1)/len(l1)
mean=mean(l1)
a=round(mean,2)
print("mean of the given list",a)

for item in l1:
    if item<a:
       print(item)

#  Find the no.of people in a bus, given the data of people onboarding & alighting at each station

def bus(n,t):
    for i in t:
        n+=i[1]-i[2]
        print(n)
bus(25,((1,2,3),(2,3,3)))


#Find the average speed of vehicle, given the distance travelled for fixed time intervals

l1=[2,3,4,5]
total=0
k=len[l1]
def dist(l1):
    for i in l1:
       total+=i
       average=(total/k)*60
    return average

#pascal triangle //
def pascal_triangle(n):
    for i in range(0, m):
        for j in range(0, i+1):
            print(int(ncr(i,j)), end=' ')
        print("\n")

#digital root //
def dr(m):
    i = m
    r =0
    while i> 0:
        rm = i%10
        i//= 10
        r += rm
    while r// 10 != 0:
        r = dr(r)
    return r


#maximum nos by deleting a single digit //
def max(n):
    
    l = []
    m= str(n)
    for i in m:
        l.append(int(m.replace(i, '')))
    return max(n)


#number pyramid //
def np(l):

    k = l - 1

    for m in range(1, l+1):
        for n in range(0, k):
            print(end=" ")
        k-= 1
        for n in range(1, m+1):
            print(j, end=".")
        
        print("\n")

#isogram

def iso(a):
    return len(a) == len(set(a.lower()))

print(iso("animal"))
print(iso("malayalam"))
print(iso("fruits"))

#Compute the word frequency in given message

def wc(str):  
    wds = str.split()
    c = dict()
    for w in wds:
        if w in c:
            c[w] += 1
        else:
            c[w] = 1

    return c

print( wc('one plus one gives two'))

#Given a number, find the largest number by shuffling the digits

def max_num(inm):

    s = str(num) 
    c = [0 for x in range(10)] 
    for i in range(len(s)): 
        c[int(s[i])] = c[int(s[i])] +  1
    r = 0
    mul = 1

    for i in range(10): 
        while c[i] > 0: 
            r = r + ( i * mul) 
            c[i] = c[i] - 1
            mul = mul* 10
  
    
    return r
    
num =int(input("enter the number"))
print (max_num(num) )

#ip into integer //
def fun(ipt):
    s = ""
    
    if type(ipt) == str:
        result = ipt.split(".")
        for x in result:
            n += x
        return int(n)
    elif type(ipt) == int:
         lst = []
         i= ipt
         while n > 0:
             if n%1000 > 255:
                 return 0
             else:
                 lst.append(n%1000)
                 n //= 1000
         for y in lst:
             i+= str(y) + "."
         return n[::-1] 




#malformed time string //
def m_t(t_s):
    st = ""
    l1 = t_s.split(":")
    l2 = []
    for i in l1:
        l2.append(int(i))
    
    if l2[2] >= 60:
        l2[1] += l2[2] // 60
        l2[2] %= 60
    if l2[1] >= 60:
        l2[0] += l2[1] // 60
        l2[1] %= 60
    if l2[0] > 23:
        return None
    
    for i in l2:
        st += str(i) + ":"
    return st[:-1]


#malformed date string //
def m_d(d_s):
    a = ""
    l = d_s.split("/")
    l2 = []
    for i in l:
        l2.append(int(i))
    if l2[2] < 0 or l2[2] > 9999:
        return None
    if l2[1] > 12:
        l2[2] += 2[1] // 12
        l2[1] %= 12
    if (l2[0] > 30 and l2[1] in [4,6,9,11]) or (l2[0] > 31 and l2[1] in [1,3,5,7,8,10,12]) or (l2[0] > 28 and l2[1] == 2):
        l2[1] += l2[0] // 30
        l2[0] %= 30

    for i in l2:
        a+= str(i) + "/"
    return a[:-1]


#mexican wave //
def mex(s):
    l = []
    for i in range(len(s)):
          a=s[:i].lower() + st[i].upper() + s[i+1:].lower()
          l.append(a)
    return l  

#largest number by deleting the single digit //

def m_delete(n):
    l = []
    m = str(n)
    for i in m:
        l.append(int(m.replace(i, '')))

#accumulated strings //
def acc_string(s):
    a = ""
    m= 0
    for i in s:
        a += i.upper() + i.lower()*m
        a += "-"
        m +=1 
    return a[:-1]
    return max(l) 



#RGB TO HEX //
def rth(value):
    n1 = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    x = "0X"
    flag = 0
    for y in value:
        if y > 255:
            return None
        elif y == 0:
            x += "00"

        while y>0 and y < 256:
            if y < 16 and flag == 0:
                r = y%16
                if r>= 10:
                    x += "0" + n1[r]
                else:
                    x+=  "0" + str(r)
                y //= 16
            elif y< 256:
                flag = 1
                r= y%16
                if r >= 10:
                    x += n1[r]
                else:
                    x+= str(r)
                y //= 16
            
    return x
    




