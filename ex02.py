# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

q_list = []

while True:
    i_string = input('Input next value or Enter for exit')
    if i_string == '':
        break
    else:
        q_list.append(i_string)

print('Original list:', q_list)
n_list = []
for i in range(0, len(q_list) // 2):
    n_list.append(q_list[i * 2 + 1])
    n_list.append(q_list[i * 2])
if len(q_list) % 2 != 0:
    n_list.append(q_list.pop())
print('New list:', n_list)
