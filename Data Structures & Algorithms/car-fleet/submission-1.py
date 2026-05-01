class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        road = [0] * target

        for pos, speed in zip(positions, speeds):
            road[pos] = (target - pos) / speed
        
        fleets = 0
        max_time = 0
        for time in reversed(road):
            if time > max_time:
                max_time = time
                fleets+=1

        return fleets