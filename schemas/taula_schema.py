from pydantic import BaseModel
from typing import Optional

# -------------------------
# Taula
# -------------------------
class TaulaSchema(BaseModel):
    idTaula: int
    nomTaula: str
    numClients: Optional[int]

    class Config:
        from_attributes = True


class TaulaCreateSchema(BaseModel):
    nomTaula: str
    numClients: Optional[int]

