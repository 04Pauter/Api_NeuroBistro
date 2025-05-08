from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from schemas.plat_schema import *
from Models.Plats import *
from db import conn 
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi.responses import FileResponse
import os

# Obtiene la ruta absoluta del directorio del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "imatges")

# Crea el directorio de uploads si no existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()

@router.get("/")
def root(): return{"message":"Test"

}
# =============================================================================
#                                TAULES
# =============================================================================

# ---------- INSERT ----------
@router.post("/afegir/taula")
def create_taula(data_taula: TaulaCreateSchema): 
    new_taula = data_taula.dict()
    print(data_taula)
    print(new_taula)
    conn.execute(taules.insert().values(new_taula))
    conn.commit()
    return "Success"

# ---------- SELECT BY ID ----------
@router.get("/api/taula/{taula_id}", response_model=TaulaSchema)
def get_taula(taula_id: str):
    with engine.connect() as conn:
        result = conn.execute(taules.select().where(taules.c.idTaula == taula_id)).first()
        print(result)
    return result

# ---------- SELECT ALL ----------
@router.get("/api/taules", response_model=list[TaulaSchema])
def get_all_taules():
    with engine.connect() as conn:
        result = conn.execute(taules.select()).fetchall()
        return result

# ---------- UPDATE (pendiente) ----------

# ---------- DELETE (pendiente) ----------


# =============================================================================
#                                PLATS
# =============================================================================

# ---------- INSERT ----------
@router.post("/afegir/plats")
def create_plat(data_plat: PlatCreateSchema): 
    new_plat = data_plat.dict()
    print(data_plat)
    print(new_plat)
    conn.execute(plats.insert().values(new_plat))
    conn.commit()
    return "Success"

# ---------- SELECT BY ID ----------
@router.get("/api/plat/{plat_id}", response_model=PlatSchema)
def get_plat(plat_id: str):
    with engine.connect() as conn:
        result = conn.execute(plats.select().where(plats.c.idPlat == plat_id)).first()
        return result

# ---------- SELECT ALL ----------
@router.get("/api/plats", response_model=list[PlatSchema])
def get_all_plats():
    with engine.connect() as conn:
        result = conn.execute(plats.select()).fetchall()
        return result

# ---------- UPDATE (pendiente) ----------

# ---------- DELETE (pendiente) ----------


# =============================================================================
#                                COMANDES
# =============================================================================

# ---------- INSERT ----------
@router.post("/afegir/comanda")
def create_comanda(data_comanda: ComandaCreateSchema): 
    new_comanda = data_comanda.dict()
    print(data_comanda)
    print(new_comanda)
    conn.execute(comandes.insert().values(new_comanda))
    conn.commit()
    return "Success"

# ---------- SELECT BY ID ----------
@router.get("/api/comanda/{comanda_id}", response_model=ComandaSchema)
def get_comanda(comanda_id: str):
    with engine.connect() as conn:
        result = conn.execute(comandes.select().where(comandes.c.idComanda == comanda_id)).first()
        return result

# ---------- SELECT ALL ----------
@router.get("/api/comandes", response_model=list[ComandaSchema])
def get_all_comandes():
    with engine.connect() as conn:
        result = conn.execute(comandes.select()).fetchall()
        return result

# ---------- UPDATE (pendiente) ----------

# ---------- DELETE (pendiente) ----------


# =============================================================================
#                                DETALLS COMANDA
# =============================================================================

# ---------- INSERT ----------
@router.post("/afegir/detall_comanda")
def create_detall_comanda(detall_comanda: DetallComandaCreateSchema): 
    new_detall = detall_comanda.dict()
    print(detall_comanda)
    print(new_detall)
    conn.execute(detalls_comanda.insert().values(new_detall))
    conn.commit()
    return "Success"

# ---------- SELECT BY ID ----------
@router.get("/api/detall_comanda/{detall_id}", response_model=DetallComandaSchema)
def get_detall_comanda(detall_id: str):
    with engine.connect() as conn:
        result = conn.execute(detalls_comanda.select().where(detalls_comanda.c.idDetall == detall_id)).first()
        return result

# ---------- SELECT ALL ----------
@router.get("/api/detalls_comanda", response_model=list[DetallComandaSchema])
def get_all_detalls_comanda():
    with engine.connect() as conn:
        result = conn.execute(detalls_comanda.select()).fetchall()
        return result

# ---------- UPDATE (pendiente) ----------

# ---------- DELETE (pendiente) ----------


# =========================================================================================================================================================
# =========================================================================================================================================================
# ===========================================================================================================================================================================
#                                IMATGES                                     
# ===========================================================================================================================================================================

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = os.path.join(UPLOAD_DIR, file.filename)

    # Lee el contenido del archivo y lo guarda en el directorio
    content = await file.read()
    with open(save_path, "wb") as f:
        f.write(content)

    # Devuelve el nombre del archivo y el estado de la carga
    return {"filename": file.filename, "status": "uploaded"}

@router.get("/file/{filename}")
async def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    print(file_path)

    # Verifica si el archivo existe, si no, lanza una excepción 404
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    # Devuelve el archivo
    return FileResponse(file_path)