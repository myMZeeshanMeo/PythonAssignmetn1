#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a Python program which accepts the radius of a circle from the user and compute the area

r=float (input("Enter radius"))
A=3.142*(pow(r,2))
print("Area of circle = ")
print(A)


# In[2]:


# Write a Python program to check if a number is positive, negative or zero

num=int(input("Enter your number = "))
if num>0:
    print("Positive Number Entered")
elif num<0:
        print("Negative Number Entered")
else:
            print("Your Number is Zero entered")


# In[3]:


# Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user

num = float(input('Enter the Numerator: '))
den = float(input('Enter the Denumerator: '))
if num % den == 0:
    print("Number {} is Completely divisible by {}".format(num, den))
else :
          print("Number {} is not Completely divisible by {}".format(num, den))


# In[5]:


# Write a Python program to calculate number of days between two dates

from datetime import datetime
date_format = "%d/%m/%Y"
e = input("Enter a date in (dd/mm/yy) Format: ")
f = input("Enter a date in (dd/mm/yy) Format: ")
a = datetime.strptime( e , date_format)
b = datetime.strptime( f , date_format)
delta = b - a
print ("There are", delta.days, "days in Between", e , "and" , f)


# In[6]:


#Calculate Volume of a sphere

import math

radius = int(input('Please Enter Your Radius = ' ))
Volume = 4/3 * math.pi* radius**3
print(Volume)
 


# In[7]:


#Copy string number of times¶

string = input('Enter a string : ')
count  = int(input('How many copy you want = '))
results = (string  , 'Copy in',  count , 'times is ', string*count )
print(results)
    


# In[8]:


# Even Or Odd Number
num = int(input("Enter a Number: "))

if  num%2 == 1:
    
    print(num, "is Odd")
else:
    print(num, "is Even")


# In[9]:


#Tester
Vowel = input('Enter a char: ')
if Vowel in ('a','A','e','E','i','I','o','O','u','U'):
   print(Vowel, 'is Vowel')
else:
   print(Vowel,'Not Vowel')


# In[10]:


#Write a Python program that will accept the base and height of a triangle and compute the area

base = int(input("Input the base : "))
height = int(input("Input the height : "))

area = base*height/2

print("area is = ", area)


# In[13]:


#Write a Python program that will accept the base and height of a triangle and compute the area
num1 = int(input("Please enter principal amount: "))
num2 = float(input("Please Enter Rate of interest in %: "))
num3= int(input("Enter number of years for investment: "))
d = 0
e = num1 * num2 * 10
while d < num3:
    e += e * num2
    d += 1
    
print("After",c,"years your principal amount",a,"over an interest rate of",b,"% will be",e)


# In[19]:


#Write a Python program that will accept the base and height of a triangle and compute the area
import math
x1=int(input('Enter X1 :'))
y1=int(input('Enter Y1 :'))
x2=int(input('Enter X2 :'))
y2=int(input('Enter Y2 :'))

distance = math.sqrt(( (x1-x2)**2)+((y1-y2)**2) )

print('Distance between points' ,(x1, y1) ,'and' ,(x2, y2) ,'is', distance)


# In[3]:


f = float(input("Enter Height In Feet : "))
print("There Are",30.48*f,"cm in",f,"feet")


# In[16]:


## Writea Python program to calculate body mass index
a = float(input("Enter Height In cm : "))
b = float(input("Enter Weight In Kg : "))
print("your BMI Is",b/pow(a/100,2))


# In[17]:


#Write a python program to sum of the first n positive integers
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum Of n Positive Integers Till",n,"Is",sum_num)


# In[18]:


#Write a Python program to calculate the sum of the digits in an integer
num = input("Enter a number: ")
sum = 0
for i in num:
    sum += int(i)
print("The sum of digits of number is",sum)


# In[19]:


#Write a Python program to convert an decimal integer to binary
number = int(input("Enter any decimal number: "))
print(" Binary Number: ", bin(number))


# In[21]:


#Write a program to convert binary number to Decimal number
bi = input("Enter a Binary number: ")
num = int(bi,2)
print("Decimal Reperesentation of",bi,"is",num)


# In[25]:


#Input a text and count the occurrences of vowels and consonant
str1 = input("Enter text: ")
vowels = 0
consonants = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print()
print("Vowels:",vowels)
print("Consonants:",consonants)


# In[31]:


#Write a program to check whether given input is palindrome or not
a = input("Enter text: ")
a = a.casefold()
b = reversed(a)

if list(a) == list(b):
   print("It is palindrome")
else:
   print("It is not palindrome")


# In[33]:


#Write a Python program that accepts a string and calculate the number of digits and letters
txt = input("Enter text: ")
a = 0
b = 0
c = 0
d = 0
for x in txt:
    if int(ord(x)) >= 65 and int(ord(x)) <= 122:
        a += 1
    elif int(ord(x)) >= 48 and int(ord(x)) <= 57:
        b += 1
    elif x == " ":
        d += 1
    else:
        c += 1
print("Numbers =",b)
print("Alphabets =",a)
print("Special Characters =",c)
print("Spaces =",d)


# In[34]:


#Write a Python program to construct the following pattern
num=5
for i in range(num):
    for j in range(i):
        print('* ', end="")
    print('')
        
for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[37]:


num = int(input("Enter a number: "))
for i in range(1,num):
    for j in range(1,i+1):
        print(j,end="")
    print('')
    
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print('')


# In[39]:


num = int(input("Enter row number: "))
count=1
for row in range(1,num+1):
    for col in range(1,row+count):
        print(row,end="")
    print('')


# In[ ]:




