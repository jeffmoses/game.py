import random
#This is a commandline test python game.

attempts_list = []



def show_score():
    if not attempts_list:
        print('Currently no highscore')

    else:
        print(f'Your high score is'
              f'{min(attempts_list)}attempts')
        


def start_game():
    attempts = 0
rand_num =random.randint(1,10)
print('Hello dear! Thank you for choosing this game , enjoy!')
player_name = input('Can i have your name for the purposes of identification? ')
wanna_play = input(
    f'Hi,{player_name},would you like to play'
    f'This game? (Enter yeah/Nah):'
)



if wanna_play.lower() != 'yeah':
    print('Thank you and enjoy dear!')
    exit()

else:
    show_score()

while wanna_play.lower() == 'yeah':
    try:
         
         guess = int(input('Pick a number btwn 1 and 10'))
         if guess < 1 or guess >10:
             raise ValueError(
                 'Kindly guess a no. within the given range'
                )  


#attempts = attempts + 1, += means the same thing.
             attempts += 1 


             attempts_list.append(attempts) 

             if guess == rand_num:
               print('Nice! you got it!')
               print(f'It took you {attempts} attempts')
               wanna_play = input(
                     'would you like to play again? (Enter Yes/No):')  
               if wanna_play.lower() != 'yes':
                   print('Thats awsome, round two')
                   break

             else:
                 attempts = 0
                 rand_num = random.randint(1,10)
                 show_score()
                 continue



         else:
             if guess > rand_num:
                 print('Its lower')
             elif guess < rand_num:
              print('its higher')

    except ValueError as err:
     print('Oh no!, that is not a valid value. Try again...')
     print(err)




if __name__=='__main__':
    start_game()


        