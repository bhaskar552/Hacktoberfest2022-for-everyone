var1=int(input("enter a value"))
print("enter the operation ")
faulty={"45*3":"555","59+6":"77","56/6":"4"}
opr=input("enter your operation (+,*,/,-)")
var2=int(input("enter 2nd value"))
eqn=str(var1)+opr+str(var2)
if eqn in faulty :
    print(faulty[eqn])
else :
    print(eval(eqn))
