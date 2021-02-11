fibbo = 1
fibbolast = 1
done = False

print("Check if a number is in the Fibonacci sequence.")
i = int(input("Enter a number: "))
if(i==0):
    print(i," is in the sequence.")
    done = True
if(i<0):
    print(i," is not in the sequence.")
    done = True
if(isinstance(i,str)):
    print(i," is not a number.")
    done=True
    
while not done:
    if(fibbo > i):
        print(i," is not in the sequence.")
        done = True
    if(fibbo == i):
        print(i, " is in the sequence.")
        done = True
    if(fibbo < i and fibbo < 3):
        temp=fibbo
        fibbo+=1
        fibbolast=temp
    elif(fibbo < i and fibbo >=3):
        temp=fibbo
        fibbo+=fibbolast
        fibbolast=temp
    
