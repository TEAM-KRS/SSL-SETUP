import os, platform, sys
os.system('xdg-open https://GitHub.com/TERM-KRS/')
bit = platform.architecture()[0]
if bit == '64bit':
 import setup
elif bit == '32bit':
 import setup32
