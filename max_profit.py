def max_profit(prices):

    curr_min = float('inf')
    max_prof = 0
    n = len(prices)

    i = 0

    while i<n:
        if prices[i]<curr_min:
            curr_min = prices[i]

        while i<n-1 and prices[i+1]>prices[i]:
            i += 1

        max_prof += prices[i] - curr_min
        curr_min = prices[i]
        i += 1
        
    return max_prof

prices = [7,1,5,3,6,4]
max_profit(prices)

prices = [1,2,3,4,5]
max_profit(prices)

prices = [7,6,4,3,1]
max_profit(prices)