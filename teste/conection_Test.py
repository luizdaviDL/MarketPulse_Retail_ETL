import sys
import os

# add the pather path past
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import get_db_engine
get_db_engine()