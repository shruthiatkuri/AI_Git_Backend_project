import os
from dotenv import load_dotenv

load_dotenv()

app_name= os.getenv("APP_NAME")
api_key= os.getenv("API_KEY")
debug= os.getenv("DEBUG")

print("App name:", app_name)
print("api_key:", api_key is not None)
print("Debug Mode", debug)