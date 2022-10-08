## Basic errors we came accross so far.

# 1. Using the keywords as variables name
print = 23
del = "Rishav" 

# 2. Keywords are generally lower case, using them in uppercase can throw error.
Print("Hello Ineuron")
Input("Enter your name")

# 3. Not using triple quote for multiple lines string.
print("Hello world
I am Rishav
I from Bihar 
I wanna be data scientist")

# 4.Using quotes inside a string 
print("Hello, my name is "Rishav"")

# 5. Using special characters(^ % $ ! @ # ^ & * ( )) in variable name.
a* = 23
ris@ ="Boy" ,etc 

# 6.Starting variables name with numbers though it can be used in variable. 
10_ris="data scientist"
2a= 90 

# 7.User input is always a string, taking it as other type without tycasting.
a = input("Enter the value of a")
b = input("Enter the value of b")
c=a+b
print (c)

# 8.Concatenation of string and integers/float. 
"Rishav"+ 11
78.9 + "lord"
'' 88'' + 56

# 9.Not using f in the following case. 
lang= "python"
print("I will be data scientist using {lang}")

# 10.Typecasting into float using int can throw error. 
a = int(input("Enter the value of a"))
b = float(input("Enter the value of b"))
and now entering a= 10.3 and b= 23 can throw error.
