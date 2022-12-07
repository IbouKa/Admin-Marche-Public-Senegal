# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE MET
import sqlalchemy as db
# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'mp_datawarehouse'


# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return db.create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
print(get_connection().url)
# Create the Metadata Object
metadata_obj = db.MetaData()

# Define the profile table

# database name
profile = db.Table(
	'mp_table',
	metadata_obj,
	db.Column('id', db.String(18),primary_key=True),
	db.Column('Type', db.String(18)),
	db.Column('Numero', db.String(18)),
	db.Column('Gestion', db.String(18), ),
	db.Column('Titre', db.String(18)),
	db.Column('Type', db.String(18)),
	db.Column('Autorite_Contractante', db.String(18)),
	db.Column('Mode_passation', db.String(18)),
	db.Column('Montant_cfa', db.Integer),
    db.Column('Clean_Date', db.Integer),
    db.Column('Year', db.Integer),
    db.Column('Month', db.Integer),
    db.Column('Day', db.Integer),
)

# Create the profile table
metadata_obj.create_all(get_connection())


if __name__ == '__main__':

    try:

        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)