
def ClimbStairs(n):
    
    if n == 0:
        return 0
    elif n==1:
        return 1
    FF=[1]*(n+1)
    FF[2] = 2
    
    for i in range(3,n+1): 
        FF[i] =FF[i-1]+FF[i-2]
    print(FF[n])
    print(FF)
if __name__ == '__main__':
    ClimbStairs(10)
    
        
