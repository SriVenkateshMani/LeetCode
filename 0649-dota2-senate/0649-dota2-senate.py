class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        d, r = deque(), deque()
        for i, j in enumerate(senate):
            if j == "R":
                r.append(i)
            else:
                d.append(i)
        
        while d and r:
            d_turn = d.popleft()
            r_turn = r.popleft()

            if d_turn < r_turn:
                d.append(d_turn +len(senate))
            else:
                r.append(r_turn +len(senate))
            
        return "Radiant" if r else "Dire"
