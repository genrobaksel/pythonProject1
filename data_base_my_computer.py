import sys
import platform
info = 'OS info is \n {}\n \n Python version is {}{}'.format(
    platform.uname(),sys.version, platform.architecture())
print(info)

with open('enot1.txt','w') as enot:
    enot.write(info)


