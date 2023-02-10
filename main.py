from fastapi import FastAPI 
from auth_routes import auth_router
from order_routes import order_router

app=FastAPI()
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
        port=int(os.getenv("PORT", default=8080)), 
        reload=True)

"""
"""