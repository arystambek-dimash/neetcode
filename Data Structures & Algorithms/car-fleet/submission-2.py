class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        road = [0] * target

        for pos, spd in zip(positions, speeds):
            road[pos] = (target - pos) / spd
        
        fleets = 0
        mn = 0
        for i in range(len(road) - 1, -1, -1):
            if road[i] > mn:
                fleets+=1
                mn = road[i]
        
        return fleets