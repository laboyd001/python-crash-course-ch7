#write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.  As they enter each topping, print a message saying you'll add that to their pizza.

prompt = "\nPlease enter the name of a topping you'd like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I'll add " + topping + " to your pizza!")