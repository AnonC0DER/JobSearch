import psycopg2 as pgs
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to database and create the table

# You may need to use CREATE DATABASE dbname; before you create connection
## Get values from .env file
conn = pgs.connect(
    host=os.getenv('JOBS_HOST'),
    database=os.getenv('JOBS_DATABASE'),
    user=os.getenv('JOBS_USER'),
    password=os.getenv('JOBS_PASSWORD'),
)

# create jobs table and its columns if they don't exists
create_table = '''
    CREATE TABLE IF NOT EXISTS Jobs (
        job_title text NOT NULL,
        more_details_url text NOT NULL,
        company_name text,
        published_date text,
        city text,
        contract text
    );
'''

cur = conn.cursor()
cur.execute(create_table)
conn.commit()
cur.close()


######################################### Functions
def SearchIn_JobSearch_db(query):
    '''Search in JobSearch database and return results'''

    query = f'''SELECT * FROM jobs WHERE LOWER(job_title) LIKE '%{query.lower()}%';'''
    cur = conn.cursor()
    cur.execute(query)
    Get_results = cur.fetchall()
    cur.close()

    try:
        result = Get_results
        return result
    except:
        result = None
        return result


def Add_new_job(title, url, comp_name, date, city, contract=None):
    '''Add a new job into JobSearch database'''
    
    if contract:
        # Insert values into JobSearch table
        insert_into_table = f'''
        INSERT INTO Jobs (job_title, more_details_url, company_name, published_date, city, contract)
        VALUES ('{title}', '{url}', '{comp_name}', '{date}', '{city}', '{contract}');
        '''

    else:
        # Insert values into JobSearch table but contract
        insert_into_table = f'''
        INSERT INTO Jobs (job_title, more_details_url, company_name, published_date, city)
        VALUES ('{title}', '{url}', '{comp_name}', '{date}', '{city}');
        '''

    cur = conn.cursor()
    cur.execute(insert_into_table, ('Jobs',))
    conn.commit()
    cur.close()