n = int(input())
n_list = []
for i in str(n):
	n_list.append(i)
	max_num = ''.join(sorted(n_list)[::-1])
print(max_num)