import os
from dotenv import load_dotenv

load_dotenv()

SHAREPOINT_URL = os.getenv("SHAREPOINT_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SHAREPOINT_FOLDER = os.getenv("SHAREPOINT_FOLDER")
LOCAL_PATH = os.getenv("LOCAL_PATH")
