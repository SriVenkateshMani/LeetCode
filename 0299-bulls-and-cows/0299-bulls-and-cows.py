class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = {}
        guess_map = {}
        cows = 0
        bulls = 0
        for j,k in zip(secret, guess):
            if j == k:
                bulls += 1
                
            else:
                secret_map[j] = secret_map.get(j,0) + 1
                guess_map[k] = guess_map.get(k,0) + 1

        for c in secret_map:
            if c in guess_map:
                cows += min(secret_map[c], guess_map[c])

        return f"{bulls}A{cows}B"