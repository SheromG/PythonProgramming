# Solution 1

T = int(input())  
for _ in range(T):
    n, p, k = map(int, input().split()) 
    ans = 0  
    
    a = p % k - 1  
    b = ((n - 1) // k) * k  
    b = n - 1 - b  
    
    if a > b:
        ans += (b + 1) * ((n - 1) // k + 1) + (a - b) * ((n - 1) // k)
    else:
        ans += ((n - 1) // k + 1) * (a + 1)
        
    for i in range(a + 1, n, k):
        ans += 1
        if i == p:
            print(ans)
            break
    
# Solution 2
        
print("Input how many test case:")                     
testCase = int(input())                                 
for index in range( testCase ):                         
    print("Input N P and K")                            
    n, p, k = map(int, input().split())                 
    ans = 0                                            
    a = p % k - 1                                   
    b =  (n - 1) % k                                   
    if a > b: ans += max(b, a - b) * (n - 1) // k + 1  
    else: ans += (a + 1) * (n // k)  

    for i in range(a + 1, n, k):
        ans += 1  
        if i == p: print(ans)                         