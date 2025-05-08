from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://pau2:1234@localhost:3306/NBistro")
conn = engine.connect()
meta_data = MetaData()

