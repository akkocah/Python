class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'

class StandardPlan(BasicPlan):
    has_HD = True
    has_UHD = False
    num_of_devices = 2
    price = '$12.99'
class PremiumPlan(StandardPlan):
    has_UHD = True
    num_of_devices = 4
    price = '$15.99'


print(StandardPlan.has_UHD)
print(BasicPlan.has_SD)
print(StandardPlan.has_HD)
print(PremiumPlan.price)
