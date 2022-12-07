import sqlalchemy as db

# Defining the Engine

url = 'mysql://root:@127.0.0.1/db_datawarehouse'
engine = db.create_engine(url, echo=True)

# Create the Metadata Object
metadata_obj = db.MetaData()

# Define the profile table

# database name
profile = db.Table(
	'profile',
	metadata_obj,
	db.Column('email', db.String, primary_key=True),
	db.Column('name', db.String),
	db.Column('contact', db.Integer),
)

# Create the profile table
metadata_obj.create_all(engine)
