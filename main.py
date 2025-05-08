
from fastapi import FastAPI
from router import router
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/imatges", StaticFiles(directory="imatges"), name="imatges")
app.include_router(router)

# Monta la carpeta 'uploads' en /uploads
#app.mount("/imatges", StaticFiles(directory="imatges"), name="imatges")



#@app.get("/")
#def read_root():
#    return {"message": "API NeuroBistro activa"}