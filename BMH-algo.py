"""
Алгоритм Бойера-Мура-Хорспула

1) Формирование таблицы смещения
2) Поиск образа

Лучший вариант: O(n/m)
Худший вариант: O(n*m)
"""

t = "данные"

seq = set()
m = len(t)
d = {}

for i in range(m - 2, -1, -1):
    if t[i] not in seq:
        d[t[i]] = m - i - 1
        seq.add(t[i])

if t[m - 1] not in seq:
    d[t[m - 1]] = m

d["*"] = m

print(d)


a = "большие метеоданные"
n = len(a)

if n >= m:
    i = m - 1

    while i < n:
        k = 0
        for j in range(m - 1, -1, -1):
            if a[i - k] != t[j]:
                if j == m - 1:
                    off = d[a[i]] if d.get(a[i], False) else d["*"]
                else:
                    off = d[t[j]]

                i += off
                break

            k += 1

        if j == 0:
            print(f"образ найден по индексу {i-k+1}")
            break

else:
    print("образ не найден!")
