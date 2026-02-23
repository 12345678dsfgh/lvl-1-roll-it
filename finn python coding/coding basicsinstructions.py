
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


#Main routine

# ask the users if they want instructions (check if they say yes / no)
want_instructions = yes_no("do you want to see the instructions?")
if want_instructions == "yes":
    instructions()
    print()
    print("Program continues")