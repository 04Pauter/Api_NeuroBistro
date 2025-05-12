from pydantic import BaseModel
from typing import Optional, Literal

# -------------------------
# Comanda
# -------------------------
class ComandaSchema(BaseModel):
    idComanda: int
    taula_id: Optional[int]
    Estat: Literal['Solicitada', 'Preparada', 'Pagada']

    class Config:
        from_attributes = True


class ComandaCreateSchema(BaseModel):
    taula_id: Optional[int]
    Estat: Literal['Solicitada', 'Preparada', 'Pagada']

