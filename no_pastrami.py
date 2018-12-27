#make a list of sandwiches and include pastrami multiple times.  Tell the users you are out of pastrami and remove it from the list

sandwich_orders = ['peanut butter & jelly', 'pastrami', 'ham', 'turkey', 'pastrami']

print("These are the sandwich orders:")
print(sandwich_orders)
print("\nWe are out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nNew sandwich orders:")
print(sandwich_orders)