from sqlalchemy import Table,Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String,Float,Text,Enum,Boolean
from db import engine,meta_data

taules = Table(
    "Taula",
    meta_data,
    Column("idTaula", Integer, primary_key=True, autoincrement=True),
    Column("nomTaula", String(100), nullable=False),
    Column("numClients", Integer),
)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
plats = Table(
    "Plat",
    meta_data,
    Column("idPlat", Integer, primary_key=True, autoincrement=True),
    Column("nomPlat", String(100), nullable=False),
    Column("preu", Float, nullable=False),
    Column("comentaris", Text),
    Column("propietats", Text),
    Column("tipus", Enum("1r", "2n", "Postres", "Begudes", name="tipus_enum"), nullable=False),
)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

comandes = Table(
    "Comanda",
    meta_data,
    Column("idComanda", Integer, primary_key=True, autoincrement=True),
    Column("taula_id", Integer, ForeignKey("Taula.idTaula")),
    Column("completa", Boolean, default=False),
    Column("pagada", Boolean, default=False),
)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
detalls_comanda = Table(
    "DetallComanda",
    meta_data,
    Column("idDetall", Integer, primary_key=True, autoincrement=True),
    Column("comanda_id", Integer, ForeignKey("Comanda.idComanda")),
    Column("postres_id", Integer, ForeignKey("Plats.idPlat")),
    Column("primer_id", Integer, ForeignKey("Plats.idPlat")),
    Column("segon_id", Integer, ForeignKey("Plats.idPlat")),
    Column("beguda_id", Integer, ForeignKey("Plats.idPlat")),
)

meta_data.create_all(engine)