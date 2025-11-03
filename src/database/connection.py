from sqlalchemy import create_engine , MetaData
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")
metadata=MetaData()
metadata.bind(engine)