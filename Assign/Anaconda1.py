import random
import pandas as pd
import numpy as np

#Cau 1
L1 = [random.randint(-100, 100) for i in range(0, int(input("Nhap n: ")))]
print(L1)
S1 = pd.Series(L1)
print(S1[1])
L2 = []
L2 = S1
print(L2.dtype)

#Cau 2
L3 = [random.randint(-100, 100) for i in range(0, int(input("Nhap n: ")))]
S2 = pd.Series(L3)

print("Cong\n",S1 + S2, "\nTru\n", S1 - S2, "\nNhan\n", S1 * S2, "\nChia\n", S1 / S2)

#Cau 3
print(["False" for i in S1 if i != [j for j in S2]])

#Cau 4
mydict = {}
listn = [str(input("Nhap ky tu: ")) for i in range (0, int(input("Nhap kich thuoc: ")))]
for i in listn:
    mydict[i] = random.randint(1, 50)
print(mydict)

S3 = pd.Series(mydict)
print(S3)

#Cau 5
A1 = np.array([random.randint(-10, 20) for i in range(0, int(input("Nhap n: ")))])

S4 = pd.Series(A1)
print(S4)

#Cau 6
S1[4] = "Python"
S1[8] = "True"
pd.to_numeric(S1, float)

print("Cau 6\n", S1)

#Cau 7
D1 = {'col1': [random.randint(0, 20) for i in range(0,6)], 'col2': [random.randint(0, 20) for i in range(0,6)], 'col3': [random.randint(0, 20) for i in range(0,6)]}

print(D1)

DF1 = pd.DataFrame(D1)

print(DF1)

temp = pd.DataFrame(D1)

S4 = temp.iloc[:, 0]
S5 = temp.iloc[:, 1]
S6 = temp.iloc[:, 2]
print("\n", S4,"\n", S5, "\n", S6)

#Cau 8 
cau8arr = np.array(S1)
print(cau8arr)

#Cau 9
S7 = pd.DataFrame({'col1': [i for i in range(0, 10)], 'col2': [i for i in range(0, 10)], 'col3': [i for i in range(0,10)]})
S8 = pd.Series(S7.stack().reset_index(drop= True))
print(S8)

#Cau 10
print(S8.sort_values())

#Cau 11
print(pd.concat([S8, pd.Series([input("Nhap gia tri tuy y: ") for i in range(0,3)])]))

#Cau 12
S1A = pd.Series([S1[i] for i in range(0, int(input("Nhap so nguyen m: ")))])
print(S1A)

S1B = pd.Series([S1A[i] for i in range(int(input("Nhap so nguyen k(k < m): ")), S1A.count())])
print(S1B)

S1C = pd.Series([int(v) for k,v in S1.items() if int(v) <= 0])
print(S1C)

#Cau 13
