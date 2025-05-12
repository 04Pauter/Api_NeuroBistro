from pydantic import BaseModel
from typing import Optional, Literal



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







