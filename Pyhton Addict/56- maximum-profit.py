# QUESTION:
# This is an interview question asked by Facebook.
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

lst = [9, 11, 8, 5, 7, 10]
maxdif = 0
for i in range(len(lst)):
	for y in range(len(lst)):
		if lst[y]-lst[i] > maxdif and y > i:
			maxdif = lst[y]-lst[i]
print(maxdif)

#########################################
lst = [1, 6, 19, 59, 30, 60]
def buy_and_sell(lst):
    max_profit = 0
    min_price = lst[0]
    for price in lst:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit
print(buy_and_sell(lst))

##########################################
