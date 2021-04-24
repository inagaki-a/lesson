total = 2
while len(str(total)) <= 9:
    total = total * 2
    if len(str(total)) == 10:
        break
    else:
        print(total)