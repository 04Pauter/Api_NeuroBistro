from pydantic import BaseModel
from typing import Optional,Literal

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

class PlatSchema(BaseModel):
    idPlat: int
    nomPlat: str
    preu: float
    comentaris: Optional[str] = None
    propietats: Optional[str] = None
    tipus: Literal["1r", "2n", "Postres", "Begudes"]
#-------------------------------------------------------------------------------
class PlatCreateSchema(BaseModel):
    nomPlat: str
    preu: float
    comentaris: Optional[str] = None
    propietats: Optional[str] = None
    tipus: Literal["1r", "2n", "Postres", "Begudes"]

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

class TaulaSchema(BaseModel):
    idTaula: int
    nomTaula: str
    numClients: Optional[int] = None
#-------------------------------------------------------------------------------
class TaulaCreateSchema(BaseModel):
    nomTaula: str
    numClients: Optional[int] = None


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

class ComandaSchema(BaseModel):
    idComanda: int
    taula_id: int
    completa: bool
    pagada: bool
#-------------------------------------------------------------------------------
class ComandaCreateSchema(BaseModel):
    taula_id: int
    completa: Optional[bool] = False
    pagada: Optional[bool] = False


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class DetallComandaSchema(BaseModel):
    idDetall: int
    comanda_id: int
    postres_id: Optional[int] = None
    primer_id: Optional[int] = None
    segon_id: Optional[int] = None
    beguda_id: Optional[int] = None
#-------------------------------------------------------------------------------
class DetallComandaCreateSchema(BaseModel):
    comanda_id: int
    postres_id: Optional[int] = None
    primer_id: Optional[int] = None
    segon_id: Optional[int] = None
    beguda_id: Optional[int] = None
