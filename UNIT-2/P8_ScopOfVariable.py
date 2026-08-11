value1="HJ"

def Diplay():
    global value1
    print("Inside the loop",value1)
    value1=20
 
Diplay()
print("Outside the loop ",value1)

print()
#nonlocal 
def outer():
    count=0
    
    def inner():
        nonlocal count
        count=count+1
        print("Inear counter : ",count)
    inner()
    print("Outer counter : ",count)       
outer()