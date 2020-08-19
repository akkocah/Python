# Your boss wants you to prepare the payrolls of the workers in your 
# department. You have to convert the amount of dollars into payroll 
# format. In order to help move things along, you have volunteered to
#  write a code that will take a float and return the amount formatting 
#  in dollars and cents.
# Given Float Type amount	Desired Output
# 3	                    $3.00
# 29.99	                $29.99
# 4.1	                    $4.10

payroll = float(input("Lütfen Maaşınızı Giriniz: "))

print(f"Bu aya ait maaşınız : ${payroll:.2f}")
print(f"Bu aya ait maaşınız : ${payroll:^25.2f}")
print(f"Bu aya ait maaşınız : ${payroll:>40.2f}")
print(f"Bu aya ait maaşınız : ${payroll:<250.2f}")


sales = {
    "cost_value": 31.87,
    "sell_value": 45.58,
    "inventory": 1001
}
total_profit = (sales["sell_value"] - sales["cost_value"]) * sales["inventory"]
print("Total Profit = ", (total_profit), "\b$")
print("Total Profit = ", round(total_profit), "\b$")