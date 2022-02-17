# 問題1
#
# for文での繰り返しを正しく使えるようになりましょう。
#
#  1 から 1000までの整数の合計値を求めるプログラムを作成してください。
#
sum = 0
for i in range(1, 1001):
    sum += i
    i += 1
print(sum)

for i in range(1, 1001):
    i += 1
    print(i)