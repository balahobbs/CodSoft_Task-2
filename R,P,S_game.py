import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    # r>s, s>p. p>r
    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return 'You won'
    
    return 'You lost!'


def is_win(user, opponent):
     
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or \
    (user == 'p'and opponent == 'r'):
        return True
    else:
        print('Wrong Input!')
    

print(play())
    