def judge(player, cpu):
    if player == cpu:
        return "draw"
    elif (player == 1 and cpu == 2) or (player == 2 and cpu == 3) or (player == 3 and cpu == 1):
        return "player"
    else:
        return "cpu"