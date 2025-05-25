class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count_map = {}
        pairs = 0
        used_center = False
        visited = set()

        # Step 1: Count frequencies
        for word in words:
            count_map[word] = count_map.get(word, 0) + 1

        # Step 2: Count valid pairs
        for word in count_map:
            rev = word[::-1]
            
            if word == rev:
                pairs += (count_map[word] // 2) * 2  # each pair is 2 words
                if not used_center and count_map[word] % 2 == 1:
                    pairs += 1  # center piece
                    used_center = True
            elif rev in count_map and word not in visited and rev not in visited:
                pairs += min(count_map[word], count_map[rev]) * 2
                visited.add(word)
                visited.add(rev)
        
        return (pairs*2)