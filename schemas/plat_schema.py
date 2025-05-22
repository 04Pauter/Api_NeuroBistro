from pydantic import BaseModel
from typing import Optional, Literal, List


# -------------------------
# Plat
# -------------------------
class PlatSchema(BaseModel):
    idPlat: int
    nomPlat: str
    caracteristiques: Optional[str]
    imatge: Optional[str]
    propietats: Optional[str]
    tipus: Literal['1r', '2n', 'Postres', 'Begudes']

    class Config:
        from_attributes = True


class PlatCreateSchema(BaseModel):
    nomPlat: str
    caracteristiques: Optional[str]
    imatge: Optional[str]
    propietats: Optional[str]
    tipus: Literal['1r', '2n', 'Postres', 'Begudes']



class PlatCuiner(BaseModel):
    nom: str
    estat: str
    tipus: str

class ComandaCuinerResponse(BaseModel):
    idComanda: int
    taulaId: int
    plats: List[PlatCuiner]





