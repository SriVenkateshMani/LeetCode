class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        min_cost = prices[0] + prices[1]

        if min_cost <= money:
            return money-min_cost
        return money