from sqlalchemy import create_engine
import psycopg2
from sqlalchemy_utils import database_exists, create_database
from local_settings import DB_CON

USER_NAME = 'postgres'
PASSWORD = 'passer123'
HOST_NAME = 'localhost'
PORT = 5432
DB_NAME ='datawarehouse_mp'

def get_engine(user,passwd, host, port,db) :
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    try:
        if not database_exists(url) :
            create_database(url)

            print('db est crée avec succés ')
        engine = create_engine(url,pool_size=50,echo=False)
        print(engine.url)
        return engine
    except:
        print('invalid connexion string')
        return False

en=get_engine(
    DB_CON['USER'],
    DB_CON['PASSWORD'],
    DB_CON['HOST'],
    DB_CON['PORT'],
    DB_CON['NAME'],
)
print(en)

en.execute("CREATE TABLE IF NOT EXISTS records (name text PRIMARY KEY, details text[])")