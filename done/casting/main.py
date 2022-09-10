# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print('Leek is ' + str(leek_price), 'euro per kilo.')

# Part 2
total_order = "leek 4"
locate_four = total_order.find("4")
num_orders = total_order[locate_four]

sum_total = leek_price * int(num_orders)
print(sum_total)

# Part 3
broccoli_price = 2.34
broccoli_order = 1.6

broccoli_total = str(round(broccoli_price * broccoli_order, 2)) + 'e'

broccoli_string = str(broccoli_order) + 'kg broccoli costs ' + (broccoli_total)
print(broccoli_string)