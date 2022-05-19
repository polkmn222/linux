#! /usr/bin/python3

import sys

for line in sys.stdin:

        line = line.strip()
        values = line.split(',')
        for n in range(0,len(values)):
                try:
                        num = int(values[n])
                except:
                        continue
                print('{}\t{}'.format(num, 1958+n-1))
