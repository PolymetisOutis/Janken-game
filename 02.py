# 問題2
#
# 繰り返しと条件分岐の複合問題
#
#  以下の実行結果例となるような、試験結果集計プログラムを作成してください。
# なお、全員の点数がマイナスの場合も正しく処理できるように注意してください。

total = int(input('生徒の人数を整数で入力してください'))
# total = 3
score = []
for i in range(total):
    score.append(int(input('{}番目の生徒の点数を入力してください。'.format(i+1))))
print(score)
print('4人の生徒の平均点は、{}点です。'.format(sum(score)))
print('最高点は、{}点です。'.format(max(score)))
print('最低点は、{}点です。'.format(min(score)))