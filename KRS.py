import os, platform, sys
bit = platform.architecture()[0]
if bit == '64bit':
 import setup
elif bit == '32bit':
 import setup32
