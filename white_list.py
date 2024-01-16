import json
import os
from config import USERS_WHITELIST
def check_whitelist(user_id):
    if user_id in USERS_WHITELIST: 
        return True
    else:
        return False
