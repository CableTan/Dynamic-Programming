import time
import random


##def TEST_dg(M):
##    k = len(M)
##    if k == 1:
##        f = M[0]
##    elif k == 2:
##        f = max(M[0],M[1])
##    else:
##        M_1 = M[0:k-1]
##        M_2 = M[0:k-2]
##        f = max(TEST(M_1),TEST(M_2) +M[k-1])
##    return f


def TEST_dp(M):
    k = len(M)
    if k == 1:
        f = M[0]
        IND = 1
    elif k==2:
        f = max(M[0].M[1])
        IND = M.index(f)
    else:
        l = [1 for i in range(0,k)]
        l[0] = M[0]
        l[1] = max(M[0],M[1])
        for j  in range(2,k):
            l[j] = max(l[j-1],l[j-2]+M[j])
        f= l[k-1]
        IND = []
        ind = l.index(l[-1])
        IND.append(ind)
        while l[ind] > M[ind]:
            ind = l.index(l[ind]-M[ind])
            IND.append(ind)
            IND.sort()
        return (f,IND)

##def TEST_ys(M):
##    k = len(M)
##    if k == 1:
##        f = M[0]
##    elif k== 2:
##        f = max(M[0],M[1])
##    else:
##        pre1 = M[0]
##        pre2 = max(M[0],M[1])
##        for i in range(2,k):
##            cur = max(pre1, pre2+M[i])
##            pre2 = pre1
##            pre1 = cur
##        f = cur
##    return f

if __name__ == '__main__':
##    N = [random.randint(1,100) for i in range(1,3000)]
    N = [3,2,5,8,4] 
    t1 = time.time()
##    TEST_dg(N)
    TEST_dp(N)
##    TEST_ys(N)
    t2 = time.time()
##    print(TEST_dg(N))
    print(TEST_dp(N))
##    print(TEST_ys(N))
    print(t2-t1)
        
    
