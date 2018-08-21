import os, sys
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
FRONTEND = os.path.abspath(os.path.join(ABSPATH, sys.argv[0]))

print('1', ABSPATH)
print('2', FRONTEND)
print('3', sys.argv[0])
print('4', os.path.join(__file__))
print('5', os.path.abspath(__file__))
print('6', os.path.dirname(__file__))
print('7', os.path.realpath(os.path.dirname(__file__)))