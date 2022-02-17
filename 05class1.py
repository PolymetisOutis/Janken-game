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


hand_list = []


for i in range(len(user_list)):
    user_list[i] = Player()
    user_list[i].name = user_name_list[i]
    user_list[i].hand = user_list[i].hand_func()
    hand_list.append(user_list[i].hand)

print(hand_list)
pc_hand = []

for i in range(len(pc_list)):
    pc_list[i] = PC()
    pc_list[i].name = pc_name_list[i]
    pc_list[i].hand = pc_list[i].hand_func()
    pc_hand.append(pc_list[i].hand)

print(pc_hand)
hand_list.extend(pc_hand)
user_list.extend(pc_list)
print(user_list)

temp_hand = []
for i in range(len(user_list)):
    user_list[i].hand = user_list[i].hand_func()
    temp_hand.append(user_list[i].hand)
print(temp_hand)