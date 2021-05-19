

## find the biggest value

def max_gift_value(M):
    m,n  = len(M) , len(M[0])
    FF = M
  
    for i in range(1,len(M[0])):
        FF[0][i] += FF[0][i-1]
    for j in range(1,len(M)):
        FF[j][0] += FF[j-1][0]
    for i in range(1,m):
        for j  in range(1,n):
            tem1 = FF[i][j-1]+M[i][j]
            tem2 = FF[i-1][j]+M[i][j]
            FF[i][j] = max(tem1,tem2)
    f= FF[m-1][n-1]
    
    ##  output  the road to terminal 
    l = []
    x = m-1
    y = n-1
    l.append([x,y])
    a = f
    
    while a != M[0][0]:

        if x  == 0 and y>0:
            l.append('—>')
            l.append([0,y-1])
            a = FF[x][y-1]
            y-=1
        elif y == 0 and x>0:
            l.append('—>')
            l.append([x-1,0])
            a = FF[x-1][y]
            x-=1
        elif FF[x-1][y]>=FF[x][y-1]:
            a=FF[x-1][y]
            l.append('—>')
            l.append([x-1,y])
            x-=1
            
        elif FF[x-1][y]< FF[x][y-1]:
            a = FF[x][y-1]
            l.append('—>')
            l.append([x,y-1])
            y-=1
        else:
            break

    print(f)
    print(FF)
    print(l)

if  __name__ == '__main__':
    N = [[1,3,6,1,7],
            [1,4,2,5,2],
            [5,2,8,1,2],
            [7,1,1,3,1]]
    max_gift_value(N)

