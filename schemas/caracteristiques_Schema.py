from pydantic import BaseModel

# -------------------------
# Caracteristiques
# -------------------------
class CaracteristicaSchema(BaseModel):
    idCaracteristica: int
    idPlat: int
    Caracteristica: str

    class Config:
        from_attributes = True


class CaracteristicaCreateSchema(BaseModel):
    idPlat: int
    Caracteristica: str