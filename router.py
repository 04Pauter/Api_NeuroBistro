from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import select
from schemas.caracteristiques_Detall_Comanda_Schema import *
from schemas.plat_schema import *
from schemas.taula_schema import *
from schemas.detallComanda_schema import *
from schemas.comanda_Schema import *
from schemas.caracteristiques_Schema import *
from Models.Plats import *
from db import conn
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

@router.post("/afegir/taula", response_model=TaulaSchema)
def create_taula(data_taula: TaulaCreateSchema):
    result = conn.execute(Taula.insert().values(**data_taula.dict()))
    conn.commit()
    return {"idTaula": result.lastrowid, **data_taula.dict()}

@router.get("/api/taula/{taula_id}", response_model=TaulaSchema)
def get_taula(taula_id: int):
    result = conn.execute(select(Taula).where(Taula.c.idTaula == taula_id)).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Taula no trobada")
    return result

@router.get("/api/taules", response_model=list[TaulaSchema])
def get_all_taules():
    return conn.execute(select(Taula)).fetchall()

@router.put("/modificar/taula/{taula_id}", response_model=TaulaSchema)
def update_taula(taula_id: int, data: TaulaCreateSchema):
    result = conn.execute(Taula.update().where(Taula.c.idTaula == taula_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Taula no trobada")
    return {"idTaula": taula_id, **data.dict()}

@router.delete("/eliminar/taula/{taula_id}")
def delete_taula(taula_id: int):
    result = conn.execute(Taula.delete().where(Taula.c.idTaula == taula_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Taula no trobada")
    return {"message": "Taula eliminada correctament"}

# =============================================================================
#                                PLATS
# =============================================================================

@router.post("/afegir/plat", response_model=PlatSchema)
def create_plat(data_plat: PlatCreateSchema):
    result = conn.execute(Plat.insert().values(**data_plat.dict()))
    conn.commit()
    return {"idPlat": result.lastrowid, **data_plat.dict()}

@router.get("/api/plat/{plat_id}", response_model=PlatSchema)
def get_plat(plat_id: int):
    result = conn.execute(select(Plat).where(Plat.c.idPlat == plat_id)).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Plat no trobat")
    return result

@router.get("/api/plats", response_model=list[PlatSchema])
def get_all_plats():
    return conn.execute(select(Plat)).fetchall()

@router.put("/modificar/plat/{plat_id}", response_model=PlatSchema)
def update_plat(plat_id: int, data: PlatCreateSchema):
    result = conn.execute(Plat.update().where(Plat.c.idPlat == plat_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Plat no trobat")
    return {"idPlat": plat_id, **data.dict()}

@router.delete("/eliminar/plat/{plat_id}")
def delete_plat(plat_id: int):
    result = conn.execute(Plat.delete().where(Plat.c.idPlat == plat_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Plat no trobat")
    return {"message": "Plat eliminat correctament"}

# =============================================================================
#                                COMANDES
# =============================================================================

@router.post("/afegir/comanda", response_model=ComandaSchema)
def create_comanda(data_comanda: ComandaCreateSchema):
    result = conn.execute(Comanda.insert().values(**data_comanda.dict()))
    conn.commit()
    return {"idComanda": result.lastrowid, **data_comanda.dict()}

@router.get("/api/comanda/{comanda_id}", response_model=ComandaSchema)
def get_comanda(comanda_id: int):
    result = conn.execute(select(Comanda).where(Comanda.c.idComanda == comanda_id)).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Comanda no trobada")
    return result

@router.get("/api/comandes", response_model=list[ComandaSchema])
def get_all_comandes():
    return conn.execute(select(Comanda)).fetchall()

@router.put("/modificar/comanda/{comanda_id}", response_model=ComandaSchema)
def update_comanda(comanda_id: int, data: ComandaCreateSchema):
    result = conn.execute(Comanda.update().where(Comanda.c.idComanda == comanda_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Comanda no trobada")
    return {"idComanda": comanda_id, **data.dict()}

@router.delete("/eliminar/comanda/{comanda_id}")
def delete_comanda(comanda_id: int):
    result = conn.execute(Comanda.delete().where(Comanda.c.idComanda == comanda_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Comanda no trobada")
    return {"message": "Comanda eliminada correctament"}

# =============================================================================
#                          DETALLS DE COMANDA
# =============================================================================

@router.post("/afegir/detall_comanda", response_model=DetallComandaSchema)
def create_detall_comanda(data: DetallComandaCreateSchema):
    result = conn.execute(DetallComanda.insert().values(**data.dict()))
    conn.commit()
    return {"idDetall": result.lastrowid, **data.dict()}

@router.get("/api/detall_comanda/{detall_id}", response_model=DetallComandaSchema)
def get_detall_comanda(detall_id: int):
    result = conn.execute(select(DetallComanda).where(DetallComanda.c.idDetall == detall_id)).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Detall no trobat")
    return result

@router.get("/api/detalls_comanda", response_model=list[DetallComandaSchema])
def get_all_detalls_comanda():
    return conn.execute(select(DetallComanda)).fetchall()

@router.put("/modificar/detall_comanda/{detall_id}", response_model=DetallComandaSchema)
def update_detall_comanda(detall_id: int, data: DetallComandaCreateSchema):
    result = conn.execute(DetallComanda.update().where(DetallComanda.c.idDetall == detall_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Detall no trobat")
    return {"idDetall": detall_id, **data.dict()}

@router.delete("/eliminar/detall_comanda/{detall_id}")
def delete_detall_comanda(detall_id: int):
    result = conn.execute(DetallComanda.delete().where(DetallComanda.c.idDetall == detall_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Detall no trobat")
    return {"message": "Detall eliminat correctament"}



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
# ===========================================================================================================================================================================
#                                Caracteristica
# ===========================================================================================================================================================================
@router.post("/afegir/caracteristica", response_model=CaracteristicaSchema)
def create_caracteristica(data: CaracteristicaCreateSchema):
    result = conn.execute(Caracteristica.insert().values(**data.dict()))
    conn.commit()
    return {"idCaracteristica": result.lastrowid, **data.dict()}

@router.get("/api/caracteristica/{caracteristica_id}", response_model=CaracteristicaSchema)
def get_caracteristica(caracteristica_id: int):
    result = conn.execute(select(Caracteristica).where(Caracteristica.c.idCaracteristica == caracteristica_id)).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Característica no trobada")
    return result

@router.get("/api/caracteristiques", response_model=list[CaracteristicaSchema])
def get_all_caracteristiques():
    return conn.execute(select(Caracteristica)).fetchall()

@router.put("/modificar/caracteristica/{caracteristica_id}", response_model=CaracteristicaSchema)
def update_caracteristica(caracteristica_id: int, data: CaracteristicaCreateSchema):
    result = conn.execute(Caracteristica.update().where(Caracteristica.c.idCaracteristica == caracteristica_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Característica no trobada")
    return {"idCaracteristica": caracteristica_id, **data.dict()}

@router.delete("/eliminar/caracteristica/{caracteristica_id}")
def delete_caracteristica(caracteristica_id: int):
    result = conn.execute(Caracteristica.delete().where(Caracteristica.c.idCaracteristica == caracteristica_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Característica no trobada")
    return {"message": "Característica eliminada correctament"}
# ===========================================================================================================================================================================
#                                CARACTERISTICA DETALL COMANDA
# ===========================================================================================================================================================================
@router.post("/afegir/caracteristica_detall", response_model=CaracteristicaDetallComandaSchema)
def create_caracteristica_detall(data: CaracteristicaDetallComandaCreateSchema):
    result = conn.execute(CaracteristicaDetallComanda.insert().values(**data.dict()))
    conn.commit()
    return {"idCDC": result.lastrowid, **data.dict()}


@router.get("/api/caracteristica_detall/{detall_id}", response_model=CaracteristicaDetallComandaSchema)
def get_caracteristica_detall(detall_id: int):
    result = conn.execute(
        select(CaracteristicaDetallComanda).where(CaracteristicaDetallComanda.c.idCDC == detall_id)
    ).first()

    if result is None:
        raise HTTPException(status_code=404, detail="Característica del detall no trobada")

    return dict(result._mapping)


@router.get("/api/caracteristiques_detall", response_model=list[CaracteristicaDetallComandaSchema])
def get_all_caracteristiques_detall():
    return conn.execute(select(CaracteristicaDetallComanda)).fetchall()

@router.put("/modificar/caracteristica_detall/{detall_id}", response_model=CaracteristicaDetallComandaSchema)
def update_caracteristica_detall(detall_id: int, data: CaracteristicaDetallComandaCreateSchema):
    result = conn.execute(CaracteristicaDetallComanda.update().where(CaracteristicaDetallComanda.c.idCaracteristicaDetall == detall_id).values(**data.dict()))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Característica del detall no trobada")
    return {"idCaracteristicaDetall": detall_id, **data.dict()}

@router.delete("/eliminar/caracteristica_detall/{detall_id}")
def delete_caracteristica_detall(detall_id: int):
    result = conn.execute(CaracteristicaDetallComanda.delete().where(CaracteristicaDetallComanda.c.idCaracteristicaDetall == detall_id))
    conn.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Característica del detall no trobada")
    return {"message": "Característica del detall eliminada correctament"}
