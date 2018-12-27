#write a program that polls users on their dream vacation.  include a block of code that prints out the result.

responses = {}

#Set flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would your dream vacation take you? ")

    #Store the response in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")