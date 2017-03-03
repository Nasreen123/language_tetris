def is_game_done(block):
    if block.active == False and block.y < 50:
        print 'GAME OVER'
        return True
    else:
        return False
