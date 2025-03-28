"""
Алгоритм Кнута-Морриса-Пратта (Прямой алгоритм)
Сложность: O(n*m)
Реализация:
1) Воспроизвести массив p
2) Произвести поиск =)
"""

a = "ab"
t = "abcd"

p = [0] * len(t)

j = 0
i = 1

""" O(len(t)) """
while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:  # t[i] != t[j]
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]


i = 0
j = 0
flag = True

""" O(len(a)) """
while i < len(a):
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == len(t):
            print("Нашли!")
            break
    else:  # a[i] != t[j]
        if j > 0:
            j = p[j - 1]
        else:
            i += 1


if i == len(a):
    print("Не нашли((")
