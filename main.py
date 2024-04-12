str_length = input("Please type Length:\n")
str_width = input( "Please type Width:\n")
str_meter_price = input("How much for 1 meter?\n")
length = float(str_length)
width = float(str_width)
meter_price = float(str_meter_price)
area = length * width
str_area = str(area)
total_price = area * meter_price
str_total_price = str(total_price)
print("The total area is: " + str_area)
print("Give the guy: " + "$" + str_total_price)