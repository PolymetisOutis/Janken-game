# 問題4
# 関数
#
# 整数型の引数一個を受け取り、合否判定結果をbool型で返す関数を、
# judgeという名前で定義してください。
# judge関数では引数が80以上なら「true」、それ以外は「false」を返してください。
#
# キーボード入力された点数をjudgeメソッドで合否判定し、結果を出力してください。
# 実行例_1
# 点数を整数で入力してください
# 79
# 79点は不合格です
#
# 実行例_2
# 点数を整数で入力してください
# 80
# 80点は合格です

score = int(input('点数を整数で入力してください'))


def judge(number):
    if number < 80:
        result = False
    else:
        result = True
    return result


if judge(score):
    print('{}点は合格です'.format(score))
else:
    print('{}点は不合格です'.format(score))
