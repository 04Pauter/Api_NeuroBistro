from pydantic import BaseModel
from typing import Optional
# -------------------------
# DetallComanda
# -------------------------
class DetallComandaSchema(BaseModel):
    idDetall: int
    comanda_id: int
    plat_id: int
    Plat_propietats: Optional[str]

    class Config:
        from_attributes = True


class DetallComandaCreateSchema(BaseModel):
    comanda_id: int
    plat_id: int
    Plat_propietats: Optional[str]


