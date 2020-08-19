sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

total_cost = sales["cost_value"]*sales["inventory"]
total_sell = sales["sell_value"]*sales["inventory"]
total_profit = round(total_sell-total_cost)
#Aşağıda toplam karın değrinin int değerinden farkı 0.5 den büyükse
# int değerini yukarıya yuvarlıyoruz. 

# int_control = (total_profit - int(total_profit) >= 0.5)*1
# total_profit = int(total_profit) + (int_control)

# print(int_control)
# print(total_cost)
# print(total_sell)
# print(total_profit)

print(f"Toplam {sales['inventory']} adet malzemenin : \nAlış maliyeti :\
 {total_cost:0.2f}$\nSatış Tutarı  : {total_sell:0.2f}$ ve\nToplam Karı ise :{total_profit}$ dır.")



