import re
def isInteger(self):
    return re.match(r"^\d+$", self) is not None

class tashizan:
    total = 0

    def totalsum(self):
        total_sum = int(tashizan.total) + int(self)
        tashizan.total = total_sum
        return total_sum

value = 0
while True:
    #合計を出力
    print(tashizan.totalsum(value))
    value = input("数値を入力してください")
    if isInteger(value) == False:
        '''
        文字が入力された時の処理
        '''
        print("終わります")
        break
    else:
        continue