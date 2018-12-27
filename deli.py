#make a list called sandwich_orders and fill it with names of various sandwiches.  Then make an empty list called finished_sandwiches.  Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.  As each sandwich is made move it to the list of finished sandwiches.  After all teh sandwiches have been made print a message listing each sandwhich that was made.

sandwich_orders = ['peanut butter & jelly', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print("Verifying sandwich: " + finished_sandwich.title())
    finished_sandwiches.append(finished_sandwich)

#Display all finished sandwiches.
print("\nThe following sandwiches have been built:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())