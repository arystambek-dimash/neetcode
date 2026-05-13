class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (timestamp, value) in self.d[key]:
            self.d[key].remove((timestamp, value))
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.d.get(key)
        if not values:
            return ""
        l = 0
        r = len(values)
        res = ""
        while l < r:
            m = (l + r) // 2
            if values[m][0] > timestamp:
                r-=1
            else:
                l+=1
        if values[m][0] > timestamp:
            return ""
        return values[m][1]