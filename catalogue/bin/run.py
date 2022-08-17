
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(fr'{BASE_DIR}')

from core.core import main
from conf import settings
from db import db_handle

if __name__ == '__main__':
    main()