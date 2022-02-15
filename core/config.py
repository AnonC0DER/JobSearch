import os
from dotenv import load_dotenv
load_dotenv()

# I'd rather use two databases for this project, one of them for inserting and getting jobs
# And the other one for Django tables (registration, tokens etc.).
# If you want to use one database, just fill all values in .env file like the same

# Get values
## Jobs database
JOBS_HOST = os.getenv('JOBS_HOST')
JOBS_DATABASE = os.getenv('JOBS_DATABASE')
JOBS_USER = os.getenv('JOBS_USER')
JOBS_PASSWORD = os.getenv('JOBS_PASSWORD')
# Django database
JS_HOST = os.getenv('JS_HOST')
JS_DATABASE = os.getenv('JS_DATABASE')
JS_USER = os.getenv('JS_USER')
JS_PASSWORD = os.getenv('JS_PASSWORD')