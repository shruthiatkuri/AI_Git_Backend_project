import os
from dotenv import load_dotenv

load_dotenv()

app_name= os.getenv("APP_NAME")
api_key= os.getenv("API_KEY")

if app_name is None:
    print("ErroR: App_name is missing")
    raise SystemExit(1)

if api_key is None:
    print("Error: API_KEY is mussing")
    raise SystemExit(1)

print("App name:", app_name)
print("api_key:", api_key is not None)
