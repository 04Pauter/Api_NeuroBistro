from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymsyql://pau:1234@localhost:3306/NeuroBistro")
conn = engine.connect()
meta_data = MetaData()

