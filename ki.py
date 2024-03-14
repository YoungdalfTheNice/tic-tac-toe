from random import randint
from board import draw_board, check_if_valid 



def make_random_move(position):
    valid_move = False
    while not valid_move:
        ki_random = randint(0,8)
        valid_move = check_if_valid(position, ki_random)
        return ki_random





