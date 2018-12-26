#ask a user for a number, and then report whether the number is a multiple of ten.

ten = input("Please tell us a number: ")
ten = int(ten)

if ten % 10 == 0:
    print("\nThe number " + str(ten) + " is a multiple of ten.")
else:
    print("\nThe number " + str(ten) + " is not a multiple of ten.")

