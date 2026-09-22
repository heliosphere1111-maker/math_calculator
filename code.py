import math

A= input("input value for A: ")
B = input("input value for B: ")
C = input("input value for C: ")
denominator = 2*int(A)
intermidiet = (int(B)**2 - 4*int(A)*int(C))
if intermidiet < 0:
    print(" square root is less than 0 please try again")
    exit()
sqrt_root = math.sqrt(intermidiet)
nominator = 0 - int(B) + sqrt_root

intermidiet = (int(B)**2 - 4*int(A)*int(C))
if intermidiet < 0:
    print(" square root is less than 0 please try again")
    exit()
sqrt_root = math.sqrt(intermidiet)
nominator2 = 0 - int(B) - sqrt_root

print("x1 =" + str(nominator / denominator))
print("x2 =" + str(nominator2 / denominator))
