import os
from dotenv import load_dotenv


load_dotenv("F:/bongodev-class-content/python-practice-problems/advanced-level/Problem-10/.env")


db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
api_key = os.getenv("API_KEY")

print(f"DB_USER: {db_user}")
print(f"DB_PASS: {db_pass}")
print(f"API_KEY: {api_key}")
