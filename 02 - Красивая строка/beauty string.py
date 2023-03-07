k = int(input())
s = input()

n = len(s)
cnt = 1
max_cnt = 1
prev = s[0]

# макс одинаковых символов в тексе
for i in range(1, n):
    if s[i] == prev:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1
        prev = s[i]

max_cnt = max(max_cnt, cnt)

# если разрешено производить достаточно замен, чтобы заменить все символы в строке,
# выводим длину строки, иначе выполняем замены, чтобы увеличить количество одинаковых символов
if k >= n:
    print(n)
else:
    l, r = 0, 0
    freq = {s[l]: 1}
    max_freq = 1
    res = max_cnt

    while r < n - 1:
        r += 1

        if s[r] not in freq:
            freq[s[r]] = 1
        else:
            freq[s[r]] += 1
        max_freq = max(max_freq, freq[s[r]])

        if r - l + 1 - max_freq > k:            # если количество замен, необходимых для получения подстроки с одинаковыми
                                                # символами, больше, чем разрешено, сдвигаем левую границу подстроки
            freq[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    print(res)
