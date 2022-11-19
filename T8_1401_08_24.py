##################primeter of Triangle#############
a=int(input("Enter side1:"))
b=int(input("Enter side2:"))
c=int(input("Enter side3:"))
if((a+b>c)and(b+c>a)and(a+c>b)):
    print("This is Triangle!")
    primeter=a+b+c
    print("primeter: ",primeter)
else:
    print("This isn't Triangle!")
###################################################
