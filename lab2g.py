#!/usr/bin/env python3
#Author: Ishtiak Islam
#Author Id: iislam
#Date Created: 2024/07/05

import sys

if len(sys.argv) <= 1:
    timer = 3
    while timer != 0:
        print(timer)
        timer -= 1
    print("blast off!")
else:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer -= 1
    print('blast off!')

'''

import sys
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")

'''


