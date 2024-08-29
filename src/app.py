import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(connection_string, execution_options={"autocommit": True})

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
with open('src/sql/create.sql', 'r') as file:
    sql_create = file.read()
with engine.connect() as connection:
    connection.execute(sql_create)
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
with open('src/sql/insert.sql', 'r') as file:
    sql_insert = file.read()
with engine.connect() as connection:
    connection.execute(sql_insert)

# 4) Use pandas to print one of the tables as dataframes using read_sql function

query = 'SELECT * FROM books'
df = pd.read_sql(query, engine)

print(df)