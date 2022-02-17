# '0:ぐー 1:ちょき 2:ぱー'
hand_dict = {0:'ぐー', 1:'ちょき', 2:'ぱー'}
pc1 = 2
pc2 = 0
user1 = 0
user2 = 2
user3 = 2
user_list = ['user1', 'user2', 'user3']
pc_list = ['pc1', 'pc2']
hand_list = [user1, user2, user3, pc1, pc2]
if user_list:
    for i in range(len(user_list)):
        print('{}さんは、{}'.format(user_list[i], hand_dict[hand_list[i]]))
if pc_list:
    for i in range(len(user_list), len(hand_list)):
        print('{}さんは、{}'.format(pc_list[i - len(user_list)], hand_dict[hand_list[i]]))

if hand_list.count(0) != 0 and hand_list.count(1) != 0 and hand_list.count(2) != 0:
    print('あいこ')
elif hand_list.count(0) == len(hand_list) or hand_list.count(1) == len(hand_list) or hand_list.count(2) == len(hand_list):
    print('あいこ')
else:
    pass


# '0:ぐー 1:ちょき 2:ぱー'
def list_pickup(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


user_list.extend(pc_list)
print(user_list)
temp_user_list = []
if user_list:
    for i in range(len(user_list)):
        print('{}さんは、{}'.format(user_list[i], hand_dict[hand_list[i]]))

if 0 in hand_list and 1 in hand_list:
    print(list_pickup(hand_list, 0))
    for i in list_pickup(hand_list, 0):
        print(user_list[i], end='さん ')
    for i in list_pickup(hand_list, 0):
        temp_user_list.append(user_list[i])

elif 1 in hand_list and 2 in hand_list:
    print(list_pickup(hand_list, 1))
    for i in list_pickup(hand_list, 1):
        print(user_list[i], end='さん ')
    for i in list_pickup(hand_list, 1):
        temp_user_list.append(user_list[i])

elif 2 in hand_list and 0 in hand_list:
    print(list_pickup(hand_list, 2))
    for i in list_pickup(hand_list, 2):
        print(user_list[i], end='さん ')
    for i in list_pickup(hand_list, 2):
        temp_user_list.append(user_list[i])
print()
user_list = temp_user_list
print(user_list)
print('pc' in user_list)
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list1 = list2
# print(list1)
# temp_user_list = []
# for i in list_pickup(hand_list, 2):
#     temp_user_list.append(user_list[i])
#     print(user_list[i])
# print(temp_user_list)
# user_list = temp_user_list
# print(user_list)

# if pc1 == pc2 == user1 == user2:
#     print('おあいこ')
# elif
