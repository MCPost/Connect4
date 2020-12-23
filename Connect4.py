# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:28:49 2020

@author: Christopher
"""


"""
Import Packages
"""
import sys
import time
import numpy as np


"""
General Parameters
"""
cols = 7
rows = 6
max_depth = 3
start_player = True
disp_score = False


"""
Subroutines
"""
def drawboard(game_matrix, list_of_choices):
    grid2print = separator1.join(game_matrix)
    sys.stdout.write('\033[H\033[J')
    sys.stdout.write(grid2print)
    if(disp_score):
        score_list = []
        for i in range(len(save_score)):
            if(save_score[i][0] == '-'):
                score_list.append(save_score[i])
                score_list.append(' ' * (5-len(save_score[i])))
            else:
                score_list.append(' ' + save_score[i])
                score_list.append(' ' * (4-len(save_score[i])))         
        sys.stdout.write(separator1.join(score_list) + '\n\n')
    sys.stdout.write(' ' + separator2.join(list_of_choices) + '\n\n')


def checkgame(cur_pos, game_matrix, list_of_choices, own, opp, second):
    
    if(own == ' X   '):
        cur_sign = 1
    else:
        cur_sign = -1
    
    if(cur_pos <= cols+1):
        list_of_choices[cur_pos-1] = ' '
    
    check4 = np.array([[0,0,0,0]] * len(game_matrix))
    cur_payout_low = 0
    
    if((cur_pos % (1 + cols)) == np.median(range(1,cols+1))):
        cur_payout_low += cur_sign*payout_list[0][1]
    
    x_dir = 1
    y_dir = 0
    for y in range(4):
        own_tok = 0
        index_list = [cur_pos]
        z = 1
        for p in range(1,4,1):
            if(1 < (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir) < len(game_matrix)):
                if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == '\n\n' or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp):
                    break
                if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == second):
                    index_list.append((1 + cols)*(p*y_dir) + cur_pos + (p*x_dir))
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own and z == p):
                        own_tok += 1
                        z += 1
        
        z = -1
        for p in range(-1,-4,-1):
            if(1 < (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir) < len(game_matrix)):
                if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == '\n\n' or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp):
                    break
                if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == second):
                    index_list.insert(0, (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir))
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own and z == p):
                        own_tok += 1
                        z -= 1
        
        if(own == second):
            own_tok += 1
            check4[index_list,y] = own_tok
        else:
            if(len(index_list) > 3):
                if(own_tok == 3):
                    cur_payout_low += cur_sign*payout_list[4][1]
                elif(own_tok == 2):
                    cur_payout_low += cur_sign*payout_list[2][1]
                    if(y == 0 and matrix[cur_pos-1] == own and matrix[cur_pos-2] == second and matrix[cur_pos+1] == own and matrix[cur_pos+2] == second):
                        cur_payout_low += cur_sign*payout_list[3][1]
                elif(own_tok == 1):
                    cur_payout_low += cur_sign*payout_list[1][1]
                    
            oth_tok = 0
            index_list = [cur_pos]
            for p in range(1,4,1):
                if(1 < (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir) < len(game_matrix)):
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == '\n\n' or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own):
                        break
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == second):
                        index_list.append((1 + cols)*(p*y_dir) + cur_pos + (p*x_dir))
                        if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp):
                            oth_tok += 1
                    
            for p in range(-1,-4,-1):
                if(1 < (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir) < len(game_matrix)):
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == '\n\n' or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == own):
                        break
                    if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp or game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == second):
                        index_list.insert(0, (1 + cols)*(p*y_dir) + cur_pos + (p*x_dir))
                        if(game_matrix[(1 + cols)*(p*y_dir) + cur_pos + (p*x_dir)] == opp):
                            oth_tok += 1
                            
            if(len(index_list) > 3):
                if(oth_tok == 3):
                    cur_payout_low += cur_sign*payout_list[8][1]
                elif(oth_tok == 2):
                    cur_payout_low += cur_sign*payout_list[6][1]
                    if(y == 0 and matrix[cur_pos-1] == opp and matrix[cur_pos-2] == second and matrix[cur_pos+1] == opp and matrix[cur_pos+2] == second):
                        cur_payout_low += cur_sign*payout_list[7][1]
                elif(oth_tok == 1):
                    cur_payout_low += cur_sign*payout_list[5][1]
            
        
        if(y == 1 or y == 2):
            x_dir -= 1
        elif(y == 0):
            y_dir += 1    
            
    if(own == second):
        if(np.any(check4 > 3)):
            return True
        else:
            return False
    else:
        return cur_payout_low
                


def bestMove(game_matrix, list_of_choices, max_depth):
    score = depth = 0
    if(disp_score):
        save_score = np.array([0]* len(list_of_choices))
    move = 1
    bestscore = -1000000
    for ch_ind, x in enumerate(list_of_choices):
        if(x != ' '):
            pos_ind = max(loc for loc, val in enumerate(game_matrix[ch_ind+1:len(game_matrix):cols+1]) if val == '---  ')*(cols+1)+(ch_ind+1)
            game_matrix[pos_ind] = ' X   '
            if(checkgame(pos_ind, game_matrix, list_of_choices, ' X   ', ' O   ', ' X   ')):
                    move = ch_ind+1
                    game_matrix[pos_ind] = '---  '
                    if(disp_score):
                        return move, save_score
                    else:            
                        return move
            if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = ' '
            if(depth < max_depth):
                score = _mini_max(pos_ind, game_matrix, list_of_choices, maximizing = False, depth = depth + 1 , max_depth = max_depth)
            else:
                score = checkgame(pos_ind, game_matrix, list_of_choices, ' X   ', ' O   ', '---  ')
            if((pos_ind % (1 + cols)) == np.median(range(1,cols+1))):
                score += payout_list[0][1]
            if(disp_score):
                save_score[ch_ind] = score
            if(score > bestscore):
                bestscore = score
                move = ch_ind+1
            game_matrix[pos_ind] = '---  '
            if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = str(pos_ind)
    if(disp_score):
        return move, save_score
    else:            
        return move

def _mini_max(pos_ind, game_matrix, list_of_choices, maximizing, depth, max_depth):
    
    if(maximizing):
        cur_payout = -10000000
        for ch_ind, x in enumerate(list_of_choices):
            if(x != ' '):
                pos_ind = max(loc for loc, val in enumerate(game_matrix[ch_ind+1:len(game_matrix):cols+1]) if val == '---  ')*(cols+1)+(ch_ind+1)
                game_matrix[pos_ind] = ' X   '
                if(checkgame(pos_ind, game_matrix, list_of_choices, ' X   ', ' O   ', ' X   ')):
                    cur_payout = payout_list[4][1]
                    game_matrix[pos_ind] = '---  '
                    if(pos_ind <= cols+1):
                        list_of_choices[pos_ind-1] = str(pos_ind)
                    return cur_payout
                if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = ' '
                if(depth < max_depth):
                    temp_score = _mini_max(pos_ind, game_matrix, list_of_choices, maximizing = False, depth = depth + 1, max_depth = max_depth)
                    cur_payout = np.max([temp_score, cur_payout])
                else:
                    temp_score = checkgame(pos_ind, game_matrix, list_of_choices, ' X   ', ' O   ', '---  ')
                    cur_payout = np.max([temp_score, cur_payout])
                game_matrix[pos_ind] = '---  '
                if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = str(pos_ind)
                    
    else:    
        cur_payout = 10000000
        for ch_ind, x in enumerate(list_of_choices):
            if(x != ' '):
                pos_ind = max(loc for loc, val in enumerate(game_matrix[ch_ind+1:len(game_matrix):cols+1]) if val == '---  ')*(cols+1)+(ch_ind+1)
                game_matrix[pos_ind] = ' O   '
                if(checkgame(pos_ind, game_matrix, list_of_choices, ' O   ', ' X   ', ' O   ')):
                    cur_payout = payout_list[8][1]
                    game_matrix[pos_ind] = '---  '
                    if(pos_ind <= cols+1):
                        list_of_choices[pos_ind-1] = str(pos_ind)
                    return cur_payout
                if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = ' ' 
                if(depth < max_depth):
                    temp_score = _mini_max(pos_ind, game_matrix, list_of_choices, maximizing = True, depth = depth + 1, max_depth = max_depth)
                    cur_payout = np.min([temp_score, cur_payout])
                else:
                    temp_score = checkgame(pos_ind, game_matrix, list_of_choices, ' O   ', ' X   ', '---  ')
                    cur_payout = np.min([temp_score, cur_payout])
                game_matrix[pos_ind] = '---  '
                if(pos_ind <= cols+1):
                    list_of_choices[pos_ind-1] = str(pos_ind)
                
    return cur_payout            
    

"""
Important Parameters and Engine
"""
rounds = int(0.5*rows*cols)
nl_size = 2
separator1 = ''
separator2 = '    '

allowed_list = ['q']
for i in range(cols):
    allowed_list.append(str(i+1))
choices = allowed_list[1:]

matrix = ['\n' * nl_size]
for i in range(rows):
    for j in range(cols):
        matrix.append('---  ')
    matrix.append('\n' * nl_size)

payout_list = [('Center',4),('TwoLine',2),('ThreeLine',5),('createC22',150),('Connect4',1000),('OppTwoLine',-2),('OppThreeline',-10),('preventC22',-200),('OppConnect4',-600)]

if(disp_score):
    save_score = ['0']* len(choices)

inp = [0] * rounds   
for j in range(rounds):
    
    if((j + max_depth + 1) > rounds):
        max_depth = np.max([0, max_depth-1])
    
    if(not start_player):
        """
        Machine's turn
        """
        if(disp_score):
            machine_choice, save_score = bestMove(game_matrix = matrix[:], list_of_choices = choices[:], max_depth = max_depth)
            save_score = [str(x) for x in save_score]
        else:
            machine_choice = bestMove(game_matrix = matrix[:], list_of_choices = choices[:], max_depth = max_depth)
        
        cur_pos = max(loc for loc, val in enumerate(matrix[machine_choice:len(matrix):cols+1]) if val == '---  ')*(cols+1)+(machine_choice)
        matrix[cur_pos] = ' X   '
        
        endgame = checkgame(cur_pos, matrix[:], choices, ' X   ', ' O   ', ' X   ')
                
        if(endgame):
            drawboard(matrix, choices)
            print('\nSorry! You lost! :(\n')
            break
    
        
    
    """
    Draw Board
    """
    drawboard(matrix, choices)
    
    
    """
    Player's turn
    """
    time.sleep(0.2)
    cur_inp = input('Choose a column: ')
    time.sleep(0.1)
      
    if(cur_inp in choices or cur_inp == 'q'):
        if(cur_inp == 'q'):
            break
        else:
            inp[j] = int(cur_inp)
    else:
        while True:
            drawboard(matrix, choices)
            time.sleep(0.2)
            cur_inp = input('Choose a column (only integers on screen are allowed, exit with q): ')
            time.sleep(0.1)
            if(cur_inp in allowed_list):
                if(cur_inp != 'q'):
                    inp[j] = int(cur_inp)
                break
    
    if(cur_inp == 'q'):
        break
    
    cur_pos = max(loc for loc, val in enumerate(matrix[inp[j]:len(matrix):cols+1]) if val == '---  ')*(cols+1)+(inp[j])
    matrix[cur_pos] = ' O   '
    
    endgame = checkgame(cur_pos, matrix[:], choices, ' O   ', ' X   ', ' O   ')
    
    if(endgame):
        drawboard(matrix, choices)
        print('\nYou won! Congratulations! :)\n')
        break
    
    
    
    if(start_player):
        """
        Machine's turn
        """
        if(disp_score):
            machine_choice, save_score = bestMove(game_matrix = matrix[:], list_of_choices = choices[:], max_depth = max_depth)
            save_score = [str(x) for x in save_score]
        else:
            machine_choice = bestMove(game_matrix = matrix[:], list_of_choices = choices[:], max_depth = max_depth)
        
        cur_pos = max(loc for loc, val in enumerate(matrix[machine_choice:len(matrix):cols+1]) if val == '---  ')*(cols+1)+(machine_choice)
        matrix[cur_pos] = ' X   '
        
        endgame = checkgame(cur_pos, matrix[:], choices, ' X   ', ' O   ', ' X   ')
                
        if(endgame):
            drawboard(matrix, choices)
            print('\nSorry! You lost! :(\n')
            break
    

if(not endgame):
    drawboard(matrix, choices)
    print('\nThat´s a tie! Try again!\n')
        
        
    
    
    
    
    
    