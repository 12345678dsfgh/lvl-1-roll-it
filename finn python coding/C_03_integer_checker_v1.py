def int_check():


    error = "please enter a number more than / equal to 13"


    try:
        response = int(input("What is your game goal? "))

        if response < 13:
            print(error)

        else:
          return response





    except ValueError:
        print(error)
#main routine starts here
game_goal = int_check()
print(game_goal)