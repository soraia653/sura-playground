import os
from dotenv import load_dotenv

load_dotenv()

user = os.gentenv('USER')
pw = os.getenv('PASSWORD')

print(f"{user}'s password is {pw}")
