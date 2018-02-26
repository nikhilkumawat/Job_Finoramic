class Solution:
    def pow(self, x, n, d):
        a = x % d;
        total = 1
        if x==0:
            return 0;
        if n==0:
            return 1
        while n>0:
            if n&1:
                total=(total*a)%d;
            n = n>>1
            a = (a*a)%d
                
        return total
