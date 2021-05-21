import numpy as np
import pandas as pd
"""
creste a 2th array, calculate how many methods to arrive the terminal
"""
def Robot(m,n):
    FF = pd.DataFrame(
        np.zeros((m,n))
                      )
    for i in range(0,m):
        FF[0][i] = 1
    for j in range(0,n):
        FF[j][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            FF[i][j] = FF[i-1][j]+FF[i][j-1]

    f = FF[n-1][m-1]
    print(FF)
    print(f)
if __name__ == '__main__':
    Robot(5,5)
