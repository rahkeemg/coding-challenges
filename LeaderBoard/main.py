def leaderboard_sort(leaderboard, changes):
    new_board = leaderboard[:]
    
    for item in changes:
        update = item.split()
        old_pos = new_board.index(update[0])
        new_pos = old_pos - int(update[-1])
        
        del new_board[old_pos]
        new_board.insert(new_pos, update[0])
        
    return new_board