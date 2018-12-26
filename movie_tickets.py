#a movie theatre charges different ticket prices depending on a persons age.  if a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.  write a loop in which you ask their age, and then tell them the cost of the ticket.

prompt = "\nPlease enter your age so we can tell you the price of the ticket:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Since you are " + str(age) + " the cost of the movie ticket is Free!")
    elif age > 3 and age <= 12:
        print("Since you are " + str(age) + " the cost of the movie ticket is $10.")
    else:
        print("Since you are " + str(age) + " the cost of the movie ticket is $15.")