N = 20
N_str = str(N)
mojisu = len(N_str)
result_num = ""
result = 0

for i in range(N):
    i += 1
    N_str = str(i)
    mojisu = len(N_str)
    result_num = ""
    for k in range(mojisu):
        result_num = result_num + (N_str[mojisu-1-k])
    if i < int(result_num):
        result_num = int(result_num)
        print(str(i) + " -> " + str(result_num) + "ピコン!")
        result += 1
    else:
        result_num = int(result_num)
        print(str(i) + " -> " + str(result_num))
print(result)