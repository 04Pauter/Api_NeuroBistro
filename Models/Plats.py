from sqlalchemy import Table, Column, Integer, String, Text, Enum, ForeignKey, MetaData
from db import engine

meta_data = MetaData()

# -------------------------
# Taula
# -------------------------
Taula = Table(
    "Taula",
    meta_data,
    Column("idTaula", Integer, primary_key=True, autoincrement=True),
    Column("nomTaula", String(100), nullable=False),
    Column("numClients", Integer)
)

# -------------------------
# Plat
# -------------------------
Plat = Table(
    "Plat",
    meta_data,
    Column("idPlat", Integer, primary_key=True, autoincrement=True),
    Column("nomPlat", String(100), nullable=False),
    Column("caracteristiques", Text),
    Column("imatge", Text),
    Column("propietats", Text),
    Column("tipus", Enum("1r", "2n", "Postres", "Begudes"), nullable=False)
)

# -------------------------
# Comanda
# -------------------------
Comanda = Table(
    "Comanda",
    meta_data,
    Column("idComanda", Integer, primary_key=True, autoincrement=True),
    Column("taula_id", Integer, ForeignKey("Taula.idTaula")),
    Column("Estat", Enum("Solicitada", "Preparada", "Pagada"), nullable=False)
)

# -------------------------
# DetallComanda
# -------------------------
DetallComanda = Table(
    "DetallComanda",
    meta_data,
    Column("idDetall", Integer, primary_key=True, autoincrement=True),
    Column("comanda_id", Integer, ForeignKey("Comanda.idComanda")),
    Column("plat_id", Integer, ForeignKey("Plat.idPlat")),
    Column("Plat_propietats", Text)
)

# -------------------------
# Caracteristica
# -------------------------
Caracteristica = Table(
    "Caracteristiques",
    meta_data,
    Column("idCaracteristica", Integer, primary_key=True, autoincrement=True),
    Column("idPlat", Integer, ForeignKey("Plat.idPlat")),
    Column("Caracteristica", Text, nullable=False)
)

# -------------------------
# CaracteristicaDetallComanda
# -------------------------
CaracteristicaDetallComanda = Table(
    "CaracteristiquesDetallComanda",
    meta_data,
    Column("idCDC", Integer, primary_key=True, autoincrement=True),
    Column("idDetallComanda", Integer, ForeignKey("DetallComanda.idDetall")),
    Column("idCaracteristica", Integer, ForeignKey("Caracteristiques.idCaracteristica"))
)

Usuari = Table(
    "Usuaris",
    meta_data,
    Column("idUsuari", Integer, primary_key=True, autoincrement=True),
    Column("nomUsuari", String(100), nullable=False),
    Column("contrasenya", String(255), nullable=False)
)
#TODO CODI NO FUNCIONAL

#comanda = Table(
#    "comanda", meta_data,
#    Column("id", Integer, primary_key=True),
#    Column("taula_id", Integer),
#    Column("estat", String),
#)

#detall_comanda = Table(
#    "detall_comanda",
#    meta_data,
#    Column("id", Integer, primary_key=True),
#    Column("comanda_id", ForeignKey("comanda.id")),
#    Column("plat_id", ForeignKey("plat.id")),
#    Column("plat_propietats", String(255)),  # ✅ LONGITUD DEFINIDA
#)

#plat = Table(
#    "plat", meta_data,
#    Column("id", Integer, primary_key=True),
#    Column("nom", String),
#    Column("tipus", String),
#)

# Crear tablas si no existen
meta_data.create_all(engine)
