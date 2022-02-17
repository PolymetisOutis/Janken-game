user_list = ['uno', 'sasaki', 'kondo']
name_list = user_list.copy()
pc_list = ['PC1号', 'PC2号']

hand_type = ('ぐー', 'ちょき', 'ぱー')


class User:

    name = None
    hand = None

    # def __init__(self, name, hand):
    #     self.name = name
    #     self.hand = hand

    def hand_func(self, number):
        return hand_type[number]


user_list[0] = User()
user_list[0].name = name_list[0]
print(user_list[0])
print(user_list)
user_list[0].hand = 1
print(user_list[0].name)
print(user_list[0].hand)
print(user_list[0].hand_func(user_list[0].hand))
uno = User()
uno.name = 'uno'
uno.hand = 1
print(uno.name)
print(uno.hand)
print(uno.hand_func(1))
