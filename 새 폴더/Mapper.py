#!/usr/bin/python3

# mapper.py

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()  # 한개의 공백이나 연속된 공백을 한개의 구분자로 간주함

    for word in words:
        print( '%s\t%s' % (word, 1) )     # 단어와 숫자 1을 매핑하여 출력
