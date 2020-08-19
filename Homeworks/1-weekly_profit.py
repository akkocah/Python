capital = 1000
day = 0

while day <7:
    capital*=1.07
    day+=1
    print(str(day) + ". gün sonunda toplam :" + str(round(capital,2)) + " $ nız bulunmaktadır." )
    
print("your capital reach " + str(round(capital,2)) + "now")
print(f"Your capital reach {round(capital,2)}$ now.")

money = 1000
time_periods = 7
daily_profit = 0.07
x = 0
while time_periods > x:
  money *= 1.07 # Calculate shortly during time_period change
                              # new money = "money + daily_profit = 1.07"
  x += 1
print("Your money", round(money, 2), "\b$ now.")

capital = 1000
daily_profit_rate = 1.07
days = 7
last_capital = capital * (daily_profit_rate ** days)
print("Your total capital will be " + str(int(last_capital))+" dollars after "+str(days)+" days.")

