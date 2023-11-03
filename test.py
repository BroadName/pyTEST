n_list = list(map(int, input().split()))
if len(n_list) % 2 != 0:
    for i in range(1, len(n_list), 2):
        n_list[i - 1], n_list[i] = n_list[i], n_list[i - 1]
else:
    for i in range(0, len(n_list), 2):
        n_list[i], n_list[i + 1] = n_list[i + 1], n_list[i]
print(n_list)