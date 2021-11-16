# -*- coding: UTF-8 -*-

def max_profit(prices):
    """
    尝试找到 min_price, 然后再找是否还有更大的利润
    :type prices: List[int]
    :rtype: int
    """
    if not prices or len(prices) == 1:
        return 0
    max_profit_result = 0
    min_price = prices[0]
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit_result = max(price - min_price, max_profit_result)
    return max_profit_result


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
