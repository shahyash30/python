import random 

p = int(input("Choose 1 for snake, 2 for water, 3 for gun : "))
c = random.randint(1,3)
print("Computer has chosen : ",c)

if(p==c):
    print("match draw")
elif(p==1 and c==2 or p==2 and c==3 or p==3 and c==1):
    print("You won ")
else:
    print("You loose")
