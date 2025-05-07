
from fastapi import FastAPI
from router import router



app = FastAPI()
app.include_router(router)

# Monta la carpeta 'uploads' en /uploads
#app.mount("/imatges", StaticFiles(directory="imatges"), name="imatges")



#@app.get("/")
#def read_root():
#    return {"message": "API NeuroBistro activa"}