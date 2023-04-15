from fastapi import FastAPI 
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings


app=FastAPI()
@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)



# Entry point
if __name__ == "__main__":
    import uvicorn
    import os
    
    start = "main:app"
    uvicorn.run(
        start, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", default=8000)), 
        reload=True)

"""
    Prender el VENV: source .env/bin/activate
    Prender el server: uvicorn main:app --reload

    ERRORES:
        -Cuando mando una orden, si pongo el tamnaño en minuscula entonces el servidor me manda un error
            peor aun asi registra la orden y de hecho me tumbo la base de datos, tuve que borrar esas entradas para que corriera de nuevo
        -Comentar el codigo y hacer el readme con html ❌
"""