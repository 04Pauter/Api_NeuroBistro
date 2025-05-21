
from db import engine

from sqlalchemy import Table, Column, Integer, String, Text, Enum, ForeignKey, MetaData

meta_data = MetaData()

# -------------------------
# Taula
# -------------------------
Taula = Table(
    "taula",
    meta_data,
    Column("idTaula", Integer, primary_key=True, autoincrement=True),
    Column("nomTaula", String(100), nullable=False),
    Column("numClients", Integer)
)

# -------------------------
# Plat
# -------------------------
Plat = Table(
    "plat",
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
    "comanda",
    meta_data,
    Column("idComanda", Integer, primary_key=True, autoincrement=True),
    Column("taula_id", Integer, ForeignKey("taula.idTaula")),
    Column("estat", Enum("Solicitada", "Preparada", "Pagada"), nullable=False)
)

# -------------------------
# DetallComanda
# -------------------------
DetallComanda = Table(
    "detall_comanda",
    meta_data,
    Column("idDetall", Integer, primary_key=True, autoincrement=True),
    Column("comanda_id", Integer, ForeignKey("comanda.idComanda")),
    Column("plat_id", Integer, ForeignKey("plat.idPlat")),
    Column("plat_propietats", String(255))
)

# -------------------------
# Caracteristica
# -------------------------
Caracteristica = Table(
    "caracteristica",
    meta_data,
    Column("idCaracteristica", Integer, primary_key=True, autoincrement=True),
    Column("idPlat", Integer, ForeignKey("plat.idPlat")),
    Column("caracteristica", Text, nullable=False)
)

# -------------------------
# CaracteristicaDetallComanda
# -------------------------
CaracteristicaDetallComanda = Table(
    "caracteristica_detall_comanda",
    meta_data,
    Column("idCDC", Integer, primary_key=True, autoincrement=True),
    Column("idDetallComanda", Integer, ForeignKey("detall_comanda.idDetall")),
    Column("idCaracteristica", Integer, ForeignKey("caracteristica.idCaracteristica"))
)

# -------------------------
# Usuari
# -------------------------
Usuari = Table(
    "usuari",
    meta_data,
    Column("idUsuari", Integer, primary_key=True, autoincrement=True),
    Column("nomUsuari", String(100), nullable=False),
    Column("contrasenya", String(255), nullable=False)
)

# Crear les taules a la base de dades
meta_data.create_all(engine)

