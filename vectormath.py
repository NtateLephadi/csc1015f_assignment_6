from math import *
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
A = A.split()
B = B.split()

def addition(A, B):
    C = ['', '', '']
    for i in range(3):
        C[i] = int(A[i]) + int(B[i])
    return C

def dot_product(A, B):
    product = 0
    for i in range(3):
        product += int(A[i]) * int(B[i])
    return product

def norm(A):
    answer = 0
    for i in A:
        answer += int(i) * int(i)
    return sqrt(answer)

print("A+B = " + str(addition(A, B)))
print("A.B = " + str(dot_product(A, B)))
print("|A| = " + str(round(norm(A), 2)))
print("|B| = " + str(round(norm(B), 2)))