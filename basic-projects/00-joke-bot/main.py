#joke Bot:

#constants:

Prompt:str = "What do you want?"
Joke:str = "Here is a joke for you! Why did the scarecrow win an award? Because he was outstanding in his field!"


# Define function:
def joke_Bot():

    # Get user input:
    user_input: str = input(Prompt)
    print(user_input)

    # If else statement:
    if (user_input.lower() == "Joke"):
        print(Joke)
    else:
        print("Sorry, i only tells Joke")

joke_Bot()

