# 問題3
#
# 1～12
# の範囲で月を入力すると、日本での季節を表示するプログラムを以下のタプルを用いて作成してください。
# （1, 2, 12
# 月は冬、3, 4, 5
# 月は春、6, 7, 8
# 月は夏、9, 10, 11
# 月は秋、を表示）。
#
# seasons = ('冬', '春', '夏', '秋')

month = int(input('1～12の範囲で月を入力してください。'))
seasons = ('冬', '春', '夏', '秋' )
# （1,2,12月は冬、3,4,5月は春、6,7,8月は夏、9,10,11月は秋、を表示）。
month_element = (month) // 3
month_element2 = month // 12
season = seasons[month_element - month_element2 * 4]
print(season)