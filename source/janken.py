import player
import computer
import janken_judge
1
def janken_main():
    player_win = 0
    cpu_win = 0
    draw_janken = 0    

    while player_win + cpu_win + draw_janken < 3:
        player_hand = player.human_pon()
        cpu_hand = computer.computer_pon()
        print(f"あなたの手：{player_hand}\nコンピュータの手：{cpu_hand}")

        result = janken_judge.judge(player_hand, cpu_hand)

        if result == "draw":
            print("<><><><><><><><><><><>\n引き分けです!\n<><><><><><><><><><><>")
            draw_janken += 1
        elif result == "player":
            print("<><><><><><><><><><><>\nあなたの勝ちです！\n<><><><><><><><><><><>")
            player_win += 1
        else:
            print("<><><><><><><><><><><>\nコンピュータの勝ちです！\n<><><><><><><><><><><>")
            cpu_win += 1

    print("【最終結果】")
    print(f'あなた：{player_win}勝 \nコンピューター：{cpu_win}勝\n{draw_janken}引き分け')
    if player_win > cpu_win:
        print("お前の勝ち❣")
    elif player_win == cpu_win:
        print("引き分け")
    else:
        print("お前の負け❣")

if __name__ == '__main__':
    janken_main()
