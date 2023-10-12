A=int(input("entre la valeure de le première variable A: "))
B=int(input(" entre la valeure de la deuxième variable B: "))
Z=A*B
if Z>0 :
    C=A
    A=B
    B=C
    print("A devient:",A)
    print("B devient:",B)
elif Z<0 :
    C=A
    A=C+B
    B=Z
    print("A devient:",A)
    print("B devient:",B)
