'''Write a program to find the sum of digits of a 
number using a while loop. '''

Num=input("Enter value : ")

S=0

i=0;
while i < len(Num):
    S=S+int(Num[i])
    i=i+1

print("Sum is ",S)
