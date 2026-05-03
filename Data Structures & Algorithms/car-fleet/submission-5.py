class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        times = []
        pos_speeds = list(zip(positions, speeds))
        pos_speeds.sort(reverse=True)
        for pos, spd in pos_speeds:
            times.append((target- pos) / spd)
        print(times)
        prev = 0
        fleets = 0
        while times:
            l = times.pop(0)
            if prev < l:
                fleets+=1
                prev = l
        return fleets

