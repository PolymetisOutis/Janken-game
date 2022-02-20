import random

hand_type = {0: 'ぐー', 1: 'ちょき', 2: 'ぱー'}
print('**じゃんけん大会ゲーム**')
print('ゲームを選んでください')
print('0:	一人プレイ')
print('1:	マルチプレイ ')
game_select = int(input('>>'))


class Player:

    name = None
    hand = None

    def hand_func(self):
        print('{}さんの手を選んでください。'.format(self.name))
        print('0:ぐー 1:ちょき 2:ぱー')
        hand_num = int(input('>>'))
        return hand_num


class PC(Player):

    def hand_func(self):
        hand_num = random.randint(0, 2)
        return hand_num


def list_pickup(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


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

    user_name_list = user_list.copy()
    pc_name_list = pc_list.copy()

    for i in range(len(user_list)):
        user_list[i] = Player()
        user_list[i].name = user_name_list[i]

    for i in range(len(pc_list)):
        pc_list[i] = PC()
        pc_list[i].name = pc_name_list[i]

    user_list.extend(pc_list)
    print(user_list)

    times = 1

    while True:
        print('{}回戦!'.format(times))

        temp_user_list = []
        hand_list = []

        for i in range(len(user_list)):
            user_list[i].hand = user_list[i].hand_func()
            hand_list.append(user_list[i].hand)

        print(user_list)
        print(hand_list)
        for i in range(len(user_list)):
            print('{}さんは {}'.format(user_list[i].name, hand_type[user_list[i].hand]))
        if hand_list.count(0) != 0 and hand_list.count(1) != 0 and hand_list.count(2) != 0:
            print('あいこ')
            temp_user_list = user_list.copy()
        elif hand_list.count(0) == len(hand_list) or hand_list.count(1) == len(hand_list) or hand_list.count(2) == len(
                hand_list):
            print('あいこ')
            temp_user_list = user_list.copy()
        elif 0 in hand_list and 1 in hand_list:
            print(list_pickup(hand_list, 0))
            print('勝利者は、')
            for i in list_pickup(hand_list, 0):
                print(user_list[i].name, end='さん ')
            print('\nです。')
            for i in list_pickup(hand_list, 0):
                temp_user_list.append(user_list[i])

        elif 1 in hand_list and 2 in hand_list:
            print(list_pickup(hand_list, 1))
            print('勝利者は、')
            for i in list_pickup(hand_list, 1):
                print(user_list[i].name, end='さん ')
            print('\nです。。')
            for i in list_pickup(hand_list, 1):
                temp_user_list.append(user_list[i])

        elif 2 in hand_list and 0 in hand_list:
            print(list_pickup(hand_list, 2))
            print('勝利者は、')
            for i in list_pickup(hand_list, 2):
                print(user_list[i].name, end='さん ')
            print('\nです。')
            for i in list_pickup(hand_list, 2):
                temp_user_list.append(user_list[i])
        print()
        user_list = temp_user_list
        print(user_list)
        if len(user_list) == 1:
            print('ゲーム終了です。優勝者は{}さんでした！'.format(user_list[0].name))
            break
        times += 1
elif game_select == 0:
    solo_user = Player()
    solo_user.name = input('ユーザーの名前を入力してください')
    solo_pc = PC()
    solo_pc.name = 'PC1号'
    print(solo_pc.name)
    user_name_list = [solo_user.name, solo_pc.name]
    user_list = [solo_user, solo_pc]
    while True:
        hand_list = []
        solo_user.hand = solo_user.hand_func()
        solo_pc.hand = solo_pc.hand_func()
        result_element = solo_user.hand - solo_pc.hand
        for i in range(len(user_list)):
            print('{}さんは {}'.format(user_list[i].name, hand_type[user_list[i].hand]))

        if result_element == 0:
            print('あいこ')
        elif result_element % 3 == 2:
            print('勝利者は')
            print('{}さん'.format(solo_user.name))
            break
        elif result_element % 3 == 1:
            print('勝利者は')
            print('{}さん'.format(solo_pc.name))
            break