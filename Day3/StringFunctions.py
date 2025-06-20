"""
mutable- cannot change the value of variable
immutable- can change the value of variable

"""
#Declaring the String in different ways

s='welcome'
s1="welcome"
s=str('welcome')
s1=str("welcome")

#Declaring empty values to string
name=''
name=""
name=str()

#example1
str1="welcome"
print(id(str1))   # string id will be displayed-1666561451584
str1=str1+" python"
print(str1)
print(id(str1))  # string id value is changed -1666561535856

#example2: + and *
str2= "welcome"
str2=str2+ "java"
print(str2)
str3="python"
str3=str3*3  # here 3 times str3 value is repeated
print(str3) #o/p: pythonpythonpython

#example3: slicing function: []
s="welcome"
print(s[1:3])  #o/p:el
print(s[:5])   #o/p: welco
print(s[3:])   #o/p: come
print(s[1:-1])  #o/p: elcom
print(s[1:-2])  #o/p: elco

#example4: ord()  and chr()

print(ord('A')) #it returns the ascii value of that char -o/p: 65
print(chr(65))  #it returns the char of that Ascii value -o/p: A

#example5: min() , max(), len()

print(max('abc'))  #o/p: c
print(min('abc'))  #o/p: a
print(len('welcome'))  #o/p: 7 ,starts from 1

#example6: in , not in operators
s="welcome"
print("come" in s)  #returns True/False , it checks whether come is present in given string or not
print("lone" in s)  #o/p: False

print("come" not in s) #o/p: False
print("lone" in s)  #o/p: True

#example7: String comparison

print("tim"=="tie")  #False
print("free"!="freedom") #True
print("arrow">"aron")  #True
print("right" >="left")  #True
print("teeth" <"tee") #False
print("yellow"<="fellow") #False
print("abc" >"") #true


#example8: testing Strings TRUE/FALSE
S="welcome to python"
print(s.isalnum)  #False  -it checks string contains all numbers
print("welcome".isalpha())  #True  -it checks string contains all alphabets or not
print("2012".isdigit()) #True  - it checks string contains all digits or not
print("first Number".isidentifier()) #False - it checks the string contains the reserved keywords in python
print(s.islower()) #True - it checks the string contains the lower case characters
print(s.isupper()) #False --it checks the string contains the upper case characters
print(s.isspace()) #True -->it checks the string contains the any spaces

#Example9: searching for substrings

s="welcome to python"
print(s.endswith("thon"))  #TRUE
print(s.startswith("good"))  #False
print(s.find("come"))  #3  - it find where come is located in given string , exactly 3rd position it is started
print(s.find("become")) #-1  - if string not found in main string
print(s.count('t')) #2  - it gives count , how many number of time this particular char is repeated in given string

#Example10: Converting strings
s="String in PYTHON"
s1=s.capitalize()
print(s1)  #String in python  - first letter will be capitalize

s2=s.title()
print(s2)  #String In Python

s3=s.lower()
print(s3) #string in python

s4=s.upper()
print(s4)  #STRING IN PYTHON

s5=s.swapcase()
print(s5)  # sTRING IN python ->swaping the upper to lower and lower to upper

s6=s.replace("in","on")
print(s6)  # Strong on PYTHON

#Example11: reverse the string
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
    print("reverse the string",rev_str)  #emoclew

#Method2
s="welcome"
rev_str=s[::-1]
print(rev_str)  #emoclew









