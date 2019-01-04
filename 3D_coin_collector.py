import numpy as np

import random
random.seed(1)
np.random.seed(1) #랜덤으로 난수 1개 생성.

def generate_3D_map(m):
    array = np.zeros((m,m,m))
#     print(array) # 10x10 -10개 / 6x6 - 6개
    for i in range(m):
        for j in range(m):
            for k in range(m):
                array[i][j][k] = np.random.choice([0,1],p=[.9,.1]) #0과 1
    return array

def coin_collect_3D(array):
    coin_collected = 0
    # Fill in this section
    for i in range(0, len(array)):
        for j in range(1,len(array[0])):
            for k in range(1,len(array[0][0])):
                array[i][j][k]+=max(array[i-1][j][k],array[i][j-1][k],array[i][j][k-1]);
#     print(array);        
                
    coin_collected= array[i][j][k];
#     print("Value=")
#     print(coin_collected)


    return coin_collected


A = generate_3D_map(6)

B = generate_3D_map(10)
# print(len(A))
# print(len(A[0]))
# print(len(A[0][6]))
print(int(coin_collect_3D(A)))
# print("SPACE\n")
print(int(coin_collect_3D(B)))