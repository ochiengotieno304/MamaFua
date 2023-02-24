
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv('API_KEY')
USERNAME=os.getenv('USERNAME')
