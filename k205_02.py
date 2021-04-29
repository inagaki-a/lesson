test = 'The scientific name persica, along with the word "peach" itself and its cognates in many European languages, derives from an early European belief that peaches were native to Persia (modern-day Iran).'
print(test)
mojisu = len(test)
test_list = []
check_moji = ""
tuika_moji = ""

for i in range(mojisu):
    check_moji = (test[i])
    if check_moji == " ":
        test_list.append(tuika_moji)
        tuika_moji = ""
    elif i == mojisu-1:
        tuika_moji += check_moji
        test_list.append(tuika_moji)
        tuika_moji = ""
    else:
        tuika_moji += check_moji

for moji in test_list:
    print(moji)