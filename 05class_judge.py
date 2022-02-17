import random

user_list = ['uno', 'sasaki', 'kondo']
user_name_list = user_list.copy()
pc_list = ['PC1号', 'PC2号']
pc_name_list = pc_list.copy()


class Player:

    name = None
    hand = None

    def hand_func(self):
        hand_num = int(input('{}さんの手を選んでください。'.format(self.name)))
        return hand_num


class PC(Player):

    def hand_func(self):
        hand_num = random.randint(0, 2)
        return hand_num


def list_pickup(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


for i in range(len(user_list)):
    user_list[i] = Player()
    user_list[i].name = user_name_list[i]

for i in range(len(pc_list)):
    pc_list[i] = PC()
    pc_list[i].name = pc_name_list[i]

user_list.extend(pc_list)
print(user_list)

while True:
    temp_user_list = []
    hand_list = []

    for i in range(len(user_list)):
        user_list[i].hand = user_list[i].hand_func()
        hand_list.append(user_list[i].hand)

    print(user_list)
    print(hand_list)

    if hand_list.count(0) != 0 and hand_list.count(1) != 0 and hand_list.count(2) != 0:
        print('あいこ')
        temp_user_list = user_list.copy()
    elif hand_list.count(0) == len(hand_list) or hand_list.count(1) == len(hand_list) or hand_list.count(2) == len(
            hand_list):
        print('あいこ')
        temp_user_list = user_list.copy()
    elif 0 in hand_list and 1 in hand_list:
        print(list_pickup(hand_list, 0))
        for i in list_pickup(hand_list, 0):
            print(user_list[i].name, end='さん ')
        for i in list_pickup(hand_list, 0):
            temp_user_list.append(user_list[i])

    elif 1 in hand_list and 2 in hand_list:
        print(list_pickup(hand_list, 1))
        for i in list_pickup(hand_list, 1):
            print(user_list[i].name, end='さん ')
        for i in list_pickup(hand_list, 1):
            temp_user_list.append(user_list[i])

    elif 2 in hand_list and 0 in hand_list:
        print(list_pickup(hand_list, 2))
        for i in list_pickup(hand_list, 2):
            print(user_list[i].name, end='さん ')
        for i in list_pickup(hand_list, 2):
            temp_user_list.append(user_list[i])
    print()
    user_list = temp_user_list
    print(user_list)
    if len(user_list) == 1:
        print('優勝は{}さん！'.format(user_list[0].name))
        break
