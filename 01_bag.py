import numpy as np
import pandas as pd

def bag(p,w,W):
## p物品的利润，w:物品的重量，W背包容量
    m = len(p)+1
    W +=1
    w.sort()
##    初始化DP数组
    FF = pd.DataFrame(
        np.zeros((m,W))
        )
    print(FF)
##    初始化第一行
##    if w[0] <= W:
##        FF[0][w[0]:-1] = p[0]
##    if w[0] >= 1:
##        for i in range(1,m):
##            FF[i][0] = 

if __name__ == '__main__':
    W = 5
    p = [1,2,3]
    w = [3,2,1]
    bag(p,w,W)
    
