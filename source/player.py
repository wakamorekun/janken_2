def human_pon():
    while True:
        janken = int(input("1.グー\n2.チョキ\n3.パー\nあなたの手を選択してください。> "))
        if janken in [1, 2, 3]:
            return janken
        else:
            print("正しい数値で入力してください。")