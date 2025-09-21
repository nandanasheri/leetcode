class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp_cache = []
    
        vowels = ['a', 'e', 'i', 'o', 'u']
        relations = {}
        # if a is the last character what came before it? (reverse thinking)
        relations['a'] = ['e', 'i', 'u']
        relations['e'] = ['a', 'i']
        relations['i'] = ['e', 'o']
        relations['o'] = ['i']
        relations['u'] = ['i', 'o']
        a,e,i,o,u = 0,1,2,3,4

        dp_cache.append([0,0,0,0,0])
        dp_cache.append([1,1,1,1,1])

        mod = 10 ** 9 + 7
        
        for j in range(2, n+1):
            dp_cache.append([0,0,0,0,0])

            dp_cache[j][a] = (dp_cache[j-1][e] + dp_cache[j-1][i] + dp_cache[j-1][u]) % mod
            dp_cache[j][e] = (dp_cache[j-1][a] + dp_cache[j-1][i]) % mod
            dp_cache[j][i] = (dp_cache[j-1][e] + dp_cache[j-1][o]) % mod
            dp_cache[j][o] = dp_cache[j-1][i] % mod
            dp_cache[j][u] = (dp_cache[j-1][i] + dp_cache[j-1][o]) % mod
        
        total = sum(dp_cache[n])
        return total % mod