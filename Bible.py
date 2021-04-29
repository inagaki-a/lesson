import os
import re
import collections


def isInteger(value):
    return re.match(r"^\d+$", value) is not None

def isAlpha(value):
    """
    半角英字チェック
    :param value: チェック対象の文字列
    :rtype: チェック対象文字列が、全て半角英字の場合 True
    """
    return re.match(r"^[a-zA-Z]+$", value) is not None

def read(value):
    file = os.path.abspath("bible.txt")
    f = open(file, 'r')
    data = f.read()

    f.close
    list_word = re.split(r'[^a-zA-Z]+', data)
    cnt = list_word.count(value)

    #対象単語があった場合
    if cnt != 0:
        print(str(value) + "は" + str(cnt) + "回")

        rank = input("単語出現ランキングの表示順位を入力:")
        if isInteger(rank) == True:
            c = collections.Counter(list_word)
            result = c.most_common(int(rank))
            k = 1
            for i in result:
                jyuni = str(k) + "位"
                print(str(k) + "位" + (i[0]) + ":"+ str((i[-1])) + "回" )
                k += 1

        else:
            print("ランキングは半角数字で入力してください。")
    #対象単語がなかった場合
    else:
        return print("その単語はありません。")