import sys
import string

text = sys.stdin.read()
count = {char: text.count(char) for char in set(text) if char not in string.whitespace}
chars = sorted(count.keys())
max_count = max(count.values())

for i in range(max_count, 0, -1):
    print(''.join(['#' if count[char] >= i else ' ' for char in chars]))

print(''.join(chars))



