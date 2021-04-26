import re

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

def isenglish(value):
    """
    半角英分チェック
    :param value: チェック対象の文字列
    :rtype: チェック対象文字列が、全て半角英字と　' . ␣ の場合 True
    """
    return re.match(r"^[A-Za-z\s.']+[\s'.-]", value) is not None

def isephone(value):
    """
    電話番号チェック
    :param value: チェック対象の文字列
    :rtype: チェック対象文字列が、全て半角英字と　' . ␣ の場合 True
    """
    return re.match(r"[0-9]+[0-9-]+[0-9]", value) is not None

comment = input("文字を入力してください")

#すべてが半角数字（第1条件）
int_result = isInteger(comment)
alfanum_result = isAlphaNumeric(comment)
eibuncheck_result = isenglish(comment)
phonechek_result = isephone(comment)

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