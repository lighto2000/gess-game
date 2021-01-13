import random 

def play():

    x = True
    while x:
        user = input('rock [r] paper [p] scissors [s]  ')
        computer = random.choice(['r','p','s'])
        if user == computer or user == 's' and computer =='r' or user == 'r' and computer == 'r' or computer =='s' and user == 'r':
            print('equal !! Again ')
            print(f'user {user}  computer {computer}')
        elif user == 'p' and computer == 'r':
            print('user win ')
            print(f'user {user}  computer {computer}')

        elif user == 's' and computer == 'p':
            print('user win ')
            print(f'user {user}  computer {computer}')

        elif user == 'p' and computer =='s':
            print("computer win ")
            print(f'user {user}  computer {computer}')

        elif user == 'r' and computer == 'p':
            print(f'computer is win ')
            print(f'user {user} computer {computer}')


        elif user == 'e':
            x = False
        
