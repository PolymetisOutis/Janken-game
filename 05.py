# 問題5（オプション）
#
# 高難度問題_1
#
# 以下の実行例を参考として、じゃんけん大会ゲームプログラムを完成させてください。
# 複数の人間と、複数のコンピュータが参加して、最後の一人になるまでじゃんけんを続けるゲームです。

print('**じゃんけん大会ゲーム**')
print('ゲームを選んでください')
print('0:	一人プレイ')
print('1:	マルチプレイ ')
game_select = int(input('>>'))


class User:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def hand(self, ):
        pass


if game_select == 1:
    print('じゃんけんゲームはじめるよ！')
    print('みんなで勝負です‼')
    user_num = int(input('参加ユーザーの人数を入力してください'))
    pc_num = int(input('参加PCの台数を入力してください'))
    user_list = []
    pc_list = []
    for i in range(user_num):
        user_list.append(input('{}番目のユーザーの名前を入力してください'.format(i + 1)))
    print(user_list)
    for i in range(pc_num):
        pc_list.append('PC{}号'.format(i + 1))
    print(pc_list)
    times = 1
    user_list_winner = user_list.copy()

    while True:
        print('{}回戦!'.format(times))
        for user in user_list_winner:
            print('{}さんの手を選んでください。'.format(user))
            print('0:ぐー 1:ちょき 2:ぱー')
            hand_user = int(input('>>'))
        times += 1
