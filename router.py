from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from schemas.plat_schema import *
import os

#FIXME VEURE IMATGE http://127.0.0.1:7500/uploads/Sprigatito.jpg
#FIXME PUJAR IMATGE http://127.0.0.1:7500/upload
router = APIRouter()

@router.get("/")
def root(): return{"message":"Test"

}


@router.post("/afegir/plats")
def create_plat(data_plat:PlatCreateSchema): 
    print(data_plat)

@router.post("/afegir/taula")
def create_taula(data_taula:TaulaCreateSchema): 
    print(data_taula)

@router.post("/afegir/comanda")
def create_comanda(data_comanda:ComandaCreateSchema): 
    print(data_comanda)

@router.post("/afegir/detall_comanda")
def create_comanda(detall_comanda:DetallComandaCreateSchema): 
    print(detall_comanda)
