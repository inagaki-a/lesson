moji = "サクサクのクッキー"
moji2 = moji.replace('サ', 'キ')
moji3 = moji.replace('キ', 'サ')

for i in range(len(moji)):
    print(moji(i))

    