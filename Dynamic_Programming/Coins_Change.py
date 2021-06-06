import  random
import math


## given  a list and a target ,
## find a sum equal to the target
##  and use the fewest elements of the list

def coins_change(coins,S):
    
    FF = [1000  for i in range(S+3)]
    l = coins
    FF[S+2] = 0

    for i in range(0,S+1):
        l = [0 for s in range(len(coins))]
        for j in range(len(coins)): 
            tmp = i - coins[j]

            if tmp < 0 :
                l[j] = S+1
            if tmp == 0:
                l[j] = S+2
            if tmp > 0:
                l[j] = tmp
        
        m = [FF[l[k]]for k in range(len(l))]
   
        FF[i] = min(m)+1
     
    if FF[S] < 1000:
        f =  FF[S]
    else:
        f = -1
    print(f)
    print(FF)

if __name__ == '__main__':
    S , coins = 19 , [1,2,5,7,13,15,20]
    coins_change(coins,S)
    
