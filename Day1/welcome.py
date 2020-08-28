'This is a docstring in green and written in quotes'
# name = input('Enter your name: ')
# print('Hello' , name.upper())
#
# 'Scan a log file from a NASA server'

# Demonstration of how Python works

# import collections
# import glob
# import re
# import pprint
#
# visited = collections.Counter()
# for filename in glob.glob('data/*.log'):
#     with open(filename) as f:
#         for line in f:
#             mo = re.search(r'GET\s+(\S+)\s+200', line)     #() in regex is making a group that part inside the group will be returned as onject
#             if mo is not None:
#                 url = mo.group(1)
#                 visited[url] += 1
#
# pprint.pprint(visited.most_common(20))
# >>> mo.group(0)
# 'GET\t/images/whatsnew.gif    200'
# >>> mo.group(1)
# '/images/whatsnew.gif'

#regex
#   + means one or more
#   * means zero or more
#   ? means zero or one


class Corolla:
    cost = 'economy'
    safety = 8

harshita = Corolla()
raymond = Corolla()

harshita.color = 'white'


#Shared information goes in class
#Unique inf goes in the instance
#Data stored in dictionaries
#Visible with the fucntion: vars()

vars(raymond)  #unique information
vars(harshita)

vars(Corolla) #Common all data


#You can call a Class ans it will make an insatnce

#by convention , Classes usually have a Upper case letter and function have lower case howeevr actually lanugua doescare

import collections






