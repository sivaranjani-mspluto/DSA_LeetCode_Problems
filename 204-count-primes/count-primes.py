class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0

        sieve=[True]*n #[false,false,true,true,..]
        sieve[0],sieve[1]=False,False
        i=2
        while i<n:
            if sieve[i]: #if index i present in the list
                for j in range(i*2,n,i):
                    sieve[j]=False
            i+=1
        return sum(sieve)

        