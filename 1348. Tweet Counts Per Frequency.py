# Direct application of dictionary, notice the:
# ans[(time - startTime + 1)//seconds] += 1
# ans = [0 for i in range(startTime, endTime + 1, seconds)]
class TweetCounts:

    def __init__(self):
        self.store = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.store[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if not tweetName in self.store:
            return 0
        if freq == 'minute':
            seconds = 60
        elif freq == 'hour':
            seconds = 3600
        elif freq == 'day':
            seconds = 86400
        ans = [0 for i in range(startTime, endTime + 1, seconds)]
        for time in self.store[tweetName]:
            if time >= startTime and time <= endTime:
                ans[(time - startTime + 1)//seconds] += 1
        return ans

