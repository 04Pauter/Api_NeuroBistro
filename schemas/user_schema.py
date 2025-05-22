from pydantic import BaseModel, EmailStr
from typing import Optional, List

from pydantic import BaseModel
from typing import Optional

class UsuariSchema(BaseModel):
    idUsuari: int
    nomUsuari: str
    contrasenya: str

    class Config:
        from_attributes = True

class UsuariCreateSchema(BaseModel):
    nomUsuari: str
    contrasenya: str

class LoginSchema(BaseModel):
    nomUsuari: str
    contrasenya: str



class PlatCuiner(BaseModel):
    nom: str
    estat: str
    tipus: str
    imatge: str  # afegim el camp imatge

class ComandaCuinerResponse(BaseModel):
    idComanda: int
    taulaId: int
    plats: List[PlatCuiner]
