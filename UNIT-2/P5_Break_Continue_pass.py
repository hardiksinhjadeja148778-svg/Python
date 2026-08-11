'''Write a program to demonstrate the use of 
break continue and pass statements.'''

#Break Loop
for i in range(1,11):
    if i==3:
        break
    print(i,end="")
print()


#Contiue
for i in range(1,11):
    if i==3:
        continue
    print(i,end="")
print()

#Pass
for i in range(1,11):
    if i==3:
        pass
    print(i,end="")
print()
