import os, platform, sys
os.system('xdg-open https://github.com/TEAM-KRS/')
bit = platform.architecture()[0]
if bit == '64bit':
 import setup
elif bit == '32bit':
 import setup32
