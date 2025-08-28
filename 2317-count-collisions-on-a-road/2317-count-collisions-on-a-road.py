class Solution:
    def countCollisions(self, directions: str) -> int:

        stack = []
        res = 0

        for i in directions:
            if i == 'L':
                if stack and stack[-1] == 'R':
                    res += 2
                    stack.pop()

                    while stack and stack[-1] == 'R':
                        res += 1
                        stack.pop()
                    stack.append('S')

                elif stack and stack[-1] == 'S':
                    res += 1
                    stack.append('S')

                else:
                    stack.append(i)

            elif i == 'S':
                while stack and stack[-1] == 'R':
                    res += 1
                    stack.pop()
                stack.append('S')

            else:  
                stack.append('R')

        return res

        