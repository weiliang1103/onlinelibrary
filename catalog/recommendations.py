import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Database config
NAME = 'a155603'
USER: 'a155603'
PASSWORD: '1Uz%3Le'
HOST: 'lrgs.ftsm.ukm.my'
PORT: ''
# /Database config

TABLE_NAME = 'catalog_history'
engine = create_engine('mysql://{0}:{1}@{2}[:{3}]/{4}').format(USER, PASSWORD, HOST, PORT, NAME)
data = pd.read_sql_table(TABLE_NAME. engine)

# Item-item collaborative filtering
def get_recommendations():
    data
