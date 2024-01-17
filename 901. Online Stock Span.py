# 1. Use monotonic stack, when poping out an element, make sure to accumulate it into the latest element.
# 2. Pop out until we stuck.
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans
