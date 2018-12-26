#write a program that asks the user how many people are in the dinner group.  If the answer is more than 8, print a message saying theyll have to wait for a table.  otherwise, report their table is ready.

dinner_seating = input("How many people will be in the dinner party? ")
dinner_seating = int(dinner_seating)

if dinner_seating > 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready!")