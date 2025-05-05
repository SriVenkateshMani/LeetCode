class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        max_capacity = capacity
        for i in range(len(plants)):
            if max_capacity < plants[i]:
                steps += 2*i +1
                max_capacity = capacity
                max_capacity -= plants[i]
            
            else:
                steps += 1
                max_capacity -= plants[i]
        return steps

            