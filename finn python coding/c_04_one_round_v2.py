import random

from c_04_one_round_v1 import comp_points


def initial_points(which_player):
    """roll the dice twice and return total / if double points apply"""
    double= ("no")



    # roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double_user = "yes"
    double = "yes"
    total= roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll2: {roll_two} \t| Total: {total} ")

    return total, double


#Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

print("Initial User", initial_user)
print("Initial Comp", initial_comp)


# Retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user [1]
double_comp = initial_comp

# # let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win you will earn double points!")
