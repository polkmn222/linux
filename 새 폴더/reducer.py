#!/usr/bin/python3

# Reducer.py
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)  # split('separator', max_split=-1)

    try:
        count = int(count)
    except ValueError:
        # count 가 숫자가 아니면 아래 코드를 실행하지 않고 지나감
        continue

    if current_word == word:            # 동일 단어가 반복될 시
        current_count += count
    else:
        if current_word:                # 동일 단어가 반복 종료될 시, 지금까지 카운트 출력
            print( '%s\t%s' % (current_word, current_count) )
        current_count = count           # 새로 나온 단어가 시작될 시
        current_word = word

if current_word == word:                # 마지막 단어는 위의 루프 안에서 출력하지 못하므로 루프 종료 후 아래에서 출력
    print( '%s\t%s' % (current_word, current_count))
