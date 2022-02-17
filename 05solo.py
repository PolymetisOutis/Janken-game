import random
# 0:ぐー 1:ちょき 2:ぱー
pc_hand = random.randint(0, 2)
print(pc_hand)
user_hand = int(input('0~2 >>'))
print(user_hand)
result_element = user_hand - pc_hand
# result_element 判定
# 1 → 負け
# 2 → 負け
# -1 → 勝ち
# -2 → 勝ち
# 0 → あいこ
# list_sample = [1, 2, 3, 4, 5]
# print(list_sample[-1])
result_judge = ('あいこ', '負け', '負け', '勝ち', '勝ち')
print(result_judge[result_element])