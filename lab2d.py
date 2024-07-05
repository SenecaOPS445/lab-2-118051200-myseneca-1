#!/usr/bin/env python3
#Author: Ishtiak Islam
#Author Id: 118051200
#Date Created: 2024/07/05

import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + ' name' + ' age')
    sys.exit()
name = sys.argv[1]
age = sys.argv[2]
print('Hi ' + name + ', you are ' + str(age) + ' years old.')



