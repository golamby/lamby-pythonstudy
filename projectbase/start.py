import sys
import os

sys.path.append(
    os.path.dirname(__file__)
)
print(os.path.dirname(__file__))
print(dir(__builtins__))
print(__name__)

# from core import src
#
# if __name__ == '__main__':
#     src.run()
