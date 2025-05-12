from pydantic import BaseModel

# -------------------------
# CaracteristiquesDetallComanda
# -------------------------
class CaracteristicaDetallComandaSchema(BaseModel):
    idCDC: int
    idDetallComanda: int
    idCaracteristica: int

    class Config:
        from_attributes = True


class CaracteristicaDetallComandaCreateSchema(BaseModel):
    idDetallComanda: int
    idCaracteristica: int
