import re

#数値チェック
def isInteger(value):
    return re.match(r"^\d+$", value) is not None

def isAlphaNumeric(value):
    """
    半角英数字チェック
    :param value: チェック対象の文字列
    :rtype: チェック対象文字列が、全て半角英数字の場合 True
    """
    return re.match(r"^\w+$", value) is not None

def isAlpha(value):
    """
    半角英字チェック
    :param value: チェック対象の文字列
    :rtype: チェック対象文字列が、全て半角英字の場合 True
    """
    return re.match(r"^[a-zA-Z]+$", value) is not None

def eibuncheck(value):
    '''
    英文チェック 半角英文　or ␣　or . or '
    '''
    i = len(value)#文字数取得
    for k in range(i):
        moji = value[k]
        if isAlpha(moji) == True or moji == " " or moji == '.' or moji == "'":
            if k == i - 1:
                return not None
        else:
            return None
            break

def phonechek(value):
    '''
    電話チェック 半角数字
    '''
    i = len(value)#文字数取得
    for k in range(i):
        moji = value[k]
        if k == 0 or k == i - 1:
            if isInteger(moji) == None:
                return False
                break
            elif k == i - 1:
                return not None
        elif isInteger(moji) == None:
            return None
            break
            
        
comment = input("文字を入力してください")

#すべてが半角数字（第1条件）
int_result = isInteger(comment)
alfanum_result = isAlphaNumeric(comment)
eibuncheck_result = eibuncheck(comment)
phonechek_result = phonechek(comment)

if int_result == True:
    print("The character strings are all half-width numbers.")

#すべてが半角英数字（第2条件）
elif alfanum_result == True:
    print("The character strings are all alphanumeric characters.")

#半角英文　or ␣　or . or '　(第3条件)
elif eibuncheck_result == True:
    print("The character string is half-width English.")

#電話番号　半角数字 or - and 最初と最後は数字
elif phonechek_result == True:
    print("The string is a phone number.")

#それ以外
else:
    print("The string is neither.")