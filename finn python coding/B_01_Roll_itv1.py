
#functions
def yes_no(question):

    while True:

        response =input(question).lower()
                # check the user says yes / no
        if response == "yes" or response == "y":
                    return "yes"
        elif response == "no" or response == "n":
                    return "no"
        else:
                    print("say yes/no or i will find you")


def instructions():
    """prints instructions"""

    print("""
    *** Instructions ****
    
 Roll the dice and try to win!
    
    """)


def int_check():


    error = "please enter a number more than / equal to 13"

    while True:
        try:
            response = int(input("What is your game goal? "))

            if response < 13:
                print(error)

            else:
              return response





        except ValueError:
            print(error)
#Main routine

# ask the users if they want instructions (check if they say yes / no)
want_instructions = yes_no("do you want to see the instructions?")
if want_instructions == "yes":
    instructions()
    print()
    game_goal = int_check()
    print(game_goal)