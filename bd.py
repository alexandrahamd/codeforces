import pandas as pd
from sqlalchemy import create_engine

from functions import get_data
from sqlalchemy.orm import Session

# create SQL Alchemy DB connection
# conn = create_engine('postgresql://user:password@host:port/dbname')
conn = create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/codeforces')

# create Pandas DataFrame from the list of records
df = pd.DataFrame(get_data())

# write DF into SQL table
df.to_sql('table_name', conn, if_exists='replace', index=False)
