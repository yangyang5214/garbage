# -*- coding: UTF-8 -*-

def max_profit(prices):
    """
    简化为：只要第二天比第一天的价格高，那就达成一次交易
    :type prices: List[int]
    :rtype: int
    """
    if not prices or len(prices) == 1:
        return 0
    max_profit_result = 0
    pre = prices[0]
    for price in prices[1:]:
        profit = price - pre
        if profit > 0:
            max_profit_result = max_profit_result + profit
        pre = price
    return max_profit_result


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
