import psycopg2
import os

# Fetch environment variables for database connection
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DB_PORT = os.environ.get('DB_PORT')

# url = 'postgres://raj:YTDz4j8qlITR9etxzzWeNZ6nV4Lr02ER@dpg-cih699tgkuvojj9dkc1g-a.singapore-postgres.render.com/techrs'
# postgres://raj:QcC9ayYK2SaZ9KtqYeU0PzsUc7ng2ie1@dpg-ckl2l42v7m0s73dccbbg-a.oregon-postgres.render.com/pgdb_29nf

# Construct the database URL
url = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# url = os.environ.get('DATABASE_URL')
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    url
    # host=DB_HOST,
    # database=DB_NAME,
    # user=DB_USER,
    # password=DB_PASSWORD,
    # port=DB_PORT
)
