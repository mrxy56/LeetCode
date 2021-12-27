# Learned the split and join operations
class LogSystem:

    def __init__(self):
        self.store = defaultdict(list)
        self.gra = {"Year": 1, "Month": 2, "Day": 3, "Hour": 4, "Minute": 5, "Second": 6}

    def put(self, id: int, timestamp: str) -> None:
        self.store[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        s = start.split(":")
        e = end.split(":")
        for i in range(self.gra[granularity], 6):
            s[i] = "00"
            e[i] = "59"
        s = ':'.join(s)
        e = ':'.join(e)
        return [Id for Id, t in self.store.items() if s<=t<=e]