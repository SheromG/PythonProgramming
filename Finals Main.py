for index in range(int(input())):
    n, p, k = map(int, input().split()) 
    ans = (p % k) * ((n - 1) // k) 
    ans +=  min((n - 1) % k + 1, p % k) 
    print(ans + (p // k) + 1)